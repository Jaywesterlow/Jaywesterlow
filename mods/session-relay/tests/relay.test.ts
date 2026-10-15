import { expect, test } from 'claude-code/testing'

test('/handoff writes a brief and sends it to the named session', async ($, on) => {
  const sent: { to: unknown; text: string }[] = []
  on('model.fork', () => ({ value: { isAnswered: true, text: 'Goal: ship the dashboard.', usage: { input_tokens: 1, output_tokens: 1, cache_creation_input_tokens: 0, cache_read_input_tokens: 0 } } }))
  on('session.send', ($, e) => {
    sent.push({ to: e.to, text: e.text })
    return { isDelivered: true }
  })
  const out = await $.command.run({ command: 'handoff', args: 'builder check the tests' })
  expect(out.text).toBe('Handoff sent to builder.')
  expect(sent[0]?.to).toBe('builder')
  expect(sent[0]?.text).toContain('Note: check the tests')
  expect(sent[0]?.text).toContain('Goal: ship the dashboard.')
})

test('/handoff without a target says how to use it and sends nothing', async ($, on) => {
  let sends = 0
  on('session.send', () => {
    sends++
    return { isDelivered: true }
  })
  const out = await $.command.run({ command: 'handoff', args: '' })
  expect(out.text).toContain('Usage')
  expect(sends).toBe(0)
})

test('/handoff reports a session that is not running', async ($, on) => {
  on('model.fork', () => ({ value: { isAnswered: true, text: 'brief', usage: { input_tokens: 1, output_tokens: 1, cache_creation_input_tokens: 0, cache_read_input_tokens: 0 } } }))
  on('session.send', () => ({ isDelivered: false, reason: 'no session named ghost is running' }))
  const out = await $.command.run({ command: 'handoff', args: 'ghost' })
  expect(out.text).toContain('Not sent')
})
