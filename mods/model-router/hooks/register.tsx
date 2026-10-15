import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { RouteDecision, RouteMode } from '../types'

const mode = atom({ plugin: 'model-router', key: 'mode' } as const, 'auto' as RouteMode)
const decision = atom({ plugin: 'model-router', key: 'decision' } as const, null as RouteDecision | null)
const stats = atom({ plugin: 'model-router', key: 'stats' } as const, { cheapTurns: 0, mainTurns: 0, cheapAgents: 0 })

// Words that mean the turn needs real reasoning. Anything matching stays on the session's model.
const HARD =
  /\b(build|implement|refactor|architect|design|debug|fix|bug|why|plan|review|audit|migrate|optimi[sz]e|security|test|deploy|compare|analy[sz]e|research|write (a|the) (skill|spec|plan))\b/i
// Small, mechanical asks: lookups, renames, formatting, one-line answers.
const EASY =
  /^(what|which|where|when|who|list|show|rename|format|translate|summari[sz]e|explain briefly|convert|count|spell|typo|grammar|reword|shorten|commit)\b/i

export function classify(text: string): Omit<RouteDecision, 'isActive'> {
  const t = text.trim()
  const prompt = t.slice(0, 80)
  if (t.length > 600) return { tier: 'main', reason: 'long prompt', prompt }
  if (HARD.test(t)) return { tier: 'main', reason: 'reasoning keyword', prompt }
  if (/```|\n.*\n.*\n/.test(t)) return { tier: 'main', reason: 'code or multi-line', prompt }
  if (EASY.test(t) || t.length < 120) return { tier: 'cheap', reason: EASY.test(t) ? 'simple ask' : 'short prompt', prompt }
  return { tier: 'main', reason: 'default', prompt }
}

// Read-only search agents rarely need the big model.
const CHEAP_AGENTS = new Set(['Explore', 'claude-code-guide', 'statusline-setup'])

export const register: Register = (on, options) => {
  const cheapModel = String(options.cheapModel ?? 'haiku')

  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'route',
      description: 'Model routing: /route auto | off | cheap, or /route to see the last decision',
      argumentHint: '[auto|off|cheap]',
    })
    return next(e)
  })

  on('command.run', { command: 'route' }, async ($, e) => {
    const arg = e.args.trim()
    if (arg === 'auto' || arg === 'off' || arg === 'cheap') {
      await update($, mode, () => arg)
      return { text: `Routing: ${arg}.` }
    }
    const [m, d, s] = await Promise.all([read($, mode), read($, decision), read($, stats)])
    const last = d ? `last turn: ${d.tier} (${d.reason})` : 'no turn routed yet'
    return { text: `Routing ${m}, cheap model ${cheapModel}; ${last}; ${s.cheapTurns} cheap / ${s.mainTurns} main turns, ${s.cheapAgents} cheap agents.` }
  })

  // Decide once per prompt the person types; slash commands and hidden prompts keep the session's model.
  on('prompt.submit', async ($, e, next) => {
    if (e.command === undefined && e.isMeta === undefined) {
      const m = await read($, mode)
      const picked = m === 'off' ? { tier: 'main' as const, reason: 'routing off', prompt: '' } : m === 'cheap' ? { tier: 'cheap' as const, reason: 'forced', prompt: '' } : classify(e.text)
      const d: RouteDecision = { ...picked, isActive: true }
      await update($, decision, () => d)
      await update($, stats, s => (d.tier === 'cheap' ? { ...s, cheapTurns: s.cheapTurns + 1 } : { ...s, mainTurns: s.mainTurns + 1 }))
      $.ui.status(d.tier === 'cheap' ? `routed: ${cheapModel} (${d.reason})` : undefined)
    }
    return next(e)
  }).catch(($, e, next) => next(e))

  // Every model request of the main loop in that turn goes to the model the decision named.
  on('turn.step', async function* ($, e, next) {
    const d = e.agentId === undefined ? await read($, decision) : null
    return yield* next(d?.isActive && d.tier === 'cheap' ? { ...e, model: cheapModel } : e)
  })

  // The decision covers the one turn the prompt started; turns a notification or a timer starts keep the session's model.
  on('turn.complete', async ($, e, next) => {
    const done = await next(e)
    await update($, decision, d => (d ? { ...d, isActive: false } : d))
    $.ui.status(undefined)
    return done
  })

  // Search subagents with no model of their own run on the cheap model.
  on('agent.spawn', async ($, e, next) => {
    if (e.model === undefined && CHEAP_AGENTS.has(e.subagentType) && (await read($, mode)) !== 'off') {
      await update($, stats, s => ({ ...s, cheapAgents: s.cheapAgents + 1 }))
      return next({ ...e, model: cheapModel })
    }
    return next(e)
  }).catch(($, e, next) => next(e))
}
