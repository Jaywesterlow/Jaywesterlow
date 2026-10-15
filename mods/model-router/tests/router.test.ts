import { expect, test } from 'claude-code/testing'

import { classify } from '../hooks/register'

test('classify keeps reasoning on the main model and sends lookups to the cheap one', () => {
  expect(classify('what time zone is Amsterdam in?').tier).toBe('cheap')
  expect(classify('rename foo to bar in utils.ts').tier).toBe('cheap')
  expect(classify('debug why the deploy fails on Vercel').tier).toBe('main')
  expect(classify('implement the checkout flow with iDEAL').tier).toBe('main')
  expect(classify('x'.repeat(700)).tier).toBe('main')
})

async function stepModel($: any, on: any, prompt: string) {
  let seen = ''
  on('prompt.submit', ($: any, e: any) => ({ text: e.text }))
  on('turn.step', async function* ($: any, e: any) {
    seen = e.model
    return { turnId: e.turnId, index: e.index, answer: '', toolUses: [] }
  })
  await $.prompt.submit({ text: prompt })
  for await (const _ of $.turn.step({ turnId: 't1', index: 0, model: 'claude-opus-5-5', messageCount: 1 })) {
  }
  return seen
}

test('an easy prompt runs its turn on the cheap model', { options: { cheapModel: 'haiku' } }, async ($, on) => {
  expect(await stepModel($, on, 'list the files in src')).toBe('haiku')
})

test('a hard prompt keeps the session model', async ($, on) => {
  expect(await stepModel($, on, 'refactor the auth module and fix the race condition')).toBe('claude-opus-5-5')
})
