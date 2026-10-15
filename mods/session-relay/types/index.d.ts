export type RelayMessage = { kind: 'in' | 'out'; peer: string; text: string; at: number }

declare module 'claude-code' {
  interface PluginState {
    'session-relay': { inbox: RelayMessage[] }
  }
}
