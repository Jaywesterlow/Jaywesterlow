import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { DashAgent, DashUsage, DashVault } from '../types'

const PANE = 'agent-dashboard'
const agents = atom({ plugin: 'agent-dashboard', key: 'agents' } as const, [] as DashAgent[])
const usage = atom({ plugin: 'agent-dashboard', key: 'usage' } as const, { contextPercent: null, costUsd: null, limits: [] } as DashUsage)
const messages = atom({ plugin: 'agent-dashboard', key: 'messages' } as const, [])
const vault = atom({ plugin: 'agent-dashboard', key: 'vault' } as const, { lines: [], at: 0, error: null } as DashVault)

const ago = (at: number) => {
  const s = Math.round((Date.now() - at) / 1000)
  return s < 60 ? `${s}s` : s < 3600 ? `${Math.round(s / 60)}m` : `${Math.round(s / 3600)}h`
}

async function refreshAgents($: EngineInterface) {
  const list = await $.agent.list()
  await update($, agents, () =>
    list.map(a => ({ id: a.id, name: a.name ?? a.description, type: a.type, status: a.status })),
  )
  const u = await $.session.usage()
  await update($, usage, () => ({
    contextPercent: u.context.percent ?? null,
    costUsd: u.cost?.usd ?? null,
    limits: u.rateLimits.map(l => `${l.kind} ${Math.round(l.percentUsed)}%`),
  }))
}

async function refreshVault($: EngineInterface, server: string, tool: string) {
  try {
    const r = await $.mcp.call(server, tool, {})
    const text = r.content.map(c => ('text' in c && typeof c.text === 'string' ? c.text : '')).join('\n')
    const lines = text.split('\n').map(l => l.trim()).filter(Boolean).slice(0, 8)
    await update($, vault, () => ({ lines, at: Date.now(), error: r.isError ? 'the tool answered an error' : null }))
  } catch (err) {
    await update($, vault, v => ({ ...v, at: Date.now(), error: `${server} not reachable` }))
  }
}

export const register: Register = (on, options) => {
  const server = String(options.vaultServer ?? 'JW AI Vault')
  const tool = String(options.vaultTool ?? 'room_read')

  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'dash', description: 'Open the agent dashboard pane' })
    $.clock.every(5_000, () => void refreshAgents($))
    $.clock.every(120_000, () => void refreshVault($, server, tool))
    void refreshAgents($)
    void refreshVault($, server, tool)
    return next(e)
  })

  on('command.run', { command: 'dash' }, async $ => {
    await refreshAgents($)
    await $.ui.open({ id: PANE, title: 'Dashboard' })
    return { text: 'Dashboard opened.' }
  })

  on('session.receive', async ($, e, next) => {
    if (e.origin.kind === 'peer-send-message') {
      await update($, messages, list => [...list, { from: 'peer', text: e.text.replace(/\s+/g, ' ').slice(0, 120), at: Date.now() }].slice(-20))
    }
    return next(e)
  }).catch(($, e, next) => next(e))

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const [a, u, m, v] = await Promise.all([read($, agents), read($, usage), read($, messages), read($, vault)])
    const width = Math.max(20, (e.props.bodyColumns ?? 60) - 2)
    const cut = (s: string) => (s.length > width ? `${s.slice(0, width - 1)}…` : s)
    const running = a.filter(x => x.status === 'running' || x.status === 'pending' || x.status === 'waiting')

    return (
      <Box flexDirection="column" gap={1}>
        <Box flexDirection="column">
          <Text bold>Session</Text>
          <Text>
            context {u.contextPercent === null ? '?' : `${Math.round(u.contextPercent)}%`} · cost{' '}
            {u.costUsd === null ? '?' : `$${u.costUsd.toFixed(2)}`}
          </Text>
          {u.limits.length > 0 && <Text dimColor>{cut(u.limits.join(' · '))}</Text>}
        </Box>
        <Box flexDirection="column">
          <Text bold>
            Agents ({running.length} active / {a.length})
          </Text>
          {a.length === 0 && <Text dimColor>No agents yet.</Text>}
          {a.slice(-10).map(x => (
            <Text dimColor={!running.includes(x)}>{cut(`${x.status.padEnd(9)} ${x.type}: ${x.name}`)}</Text>
          ))}
        </Box>
        <Box flexDirection="column">
          <Text bold>Messages from other sessions</Text>
          {m.length === 0 && <Text dimColor>None yet.</Text>}
          {m.slice(-5).map(x => (
            <Text>{cut(`${ago(x.at)} ${x.text}`)}</Text>
          ))}
        </Box>
        <Box flexDirection="column">
          <Text bold>Second brain ({server})</Text>
          {v.error !== null && <Text dimColor>{v.error}</Text>}
          {v.lines.map(l => (
            <Text dimColor>{cut(l)}</Text>
          ))}
        </Box>
      </Box>
    )
  })
}
