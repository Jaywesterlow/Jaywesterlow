import { expect, test } from 'claude-code/testing'

for (const surface of ['terminal', 'desktop'] as const) {
  test(`the pane draws every section on ${surface}`, async ($, on) => {
    on('agent.list', () => [{ id: 'a1', name: 'scout', description: 'search', type: 'Explore', status: 'running' }])
    on('mcp.call', () => ({ content: [{ type: 'text', text: 'Jaymar: ship the router today' }], isError: false }))
    const ui = await $.ui.mount({ plugin: 'agent-dashboard', surface, component: 'Pane', props: { bodyColumns: 60 }, requestId: 'agent-dashboard' })
    const drawn = JSON.stringify(await ui.drawn())
    expect(drawn).toContain('Agents')
    expect(drawn).toContain('Messages from other sessions')
    expect(drawn).toContain('Second brain')
  })
}
