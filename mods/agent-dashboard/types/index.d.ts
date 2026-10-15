export type DashAgent = { id: string; name: string; type: string; status: string }
export type DashUsage = { contextPercent: number | null; costUsd: number | null; limits: string[] }
export type DashMessage = { from: string; text: string; at: number }
export type DashVault = { lines: string[]; at: number; error: string | null }

declare module 'claude-code' {
  interface PluginState {
    'agent-dashboard': {
      agents: DashAgent[]
      usage: DashUsage
      messages: DashMessage[]
      vault: DashVault
    }
  }
}
