import { atom, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { RelayMessage } from '../types'

const inbox = atom({ plugin: 'session-relay', key: 'inbox' } as const, [])

const BRIEF = [
  'Write a handoff brief for another Claude Code session that will continue this work.',
  'Sections: Goal, Decisions made, Done so far (files touched), Next steps (numbered, concrete), Open questions, Gotchas.',
  'Plain text, no preamble, at most 400 words.',
].join('\n')

const log = ($: EngineInterface, msg: RelayMessage) =>
  update($, inbox, list => [...list, msg].slice(-50))

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'handoff',
      description: 'Send a brief of this session to another session: /handoff <session name or id> [extra note]',
      argumentHint: '<to> [note]',
    })
    return next(e)
  })

  on('command.run', { command: 'handoff' }, async ($, e) => {
    const [to, ...rest] = e.args.trim().split(/\s+/)
    if (!to) return { text: 'Usage: /handoff <session name or id> [note]. Ask me to run ListAgents to see the names.' }

    const brief = await $.model.fork({ prompt: BRIEF })
    if (!brief.isAnswered) return { text: `Could not write the brief (${brief.reason}). Nothing was sent.` }

    const note = rest.join(' ')
    const text = `HANDOFF from another session.${note ? `\nNote: ${note}` : ''}\n\n${brief.text}`
    const address = to.startsWith('session_') || /^[0-9a-f-]{36}$/.test(to) ? { sessionId: to } : to
    const sent = await $.session.send({ to: address, text })
    if (!sent.isDelivered) return { text: `Not sent to ${to}: ${sent.reason}` }
    await log($, { kind: 'out', peer: to, text: brief.text.slice(0, 280), at: Date.now() })

    return { text: `Handoff sent to ${to}.`, context: [`The brief you sent:\n${brief.text}`] }
  })

  // Every message another session or agent sends here: keep a copy for the inbox and the dashboard.
  on('session.receive', async ($, e, next) => {
    const isPeer = e.origin.kind === 'peer-send-message'
    if (isPeer) {
      const peer = /from[=: "]+([\w@.-]+)/i.exec(e.text)?.[1] ?? 'peer'
      await log($, { kind: 'in', peer, text: e.text.slice(0, 280), at: Date.now() })
      $.ui.toast(`Message from ${peer}`)
    }
    return next(e)
  }).catch(($, e, next) => next(e))
}
