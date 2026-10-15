export type RouteTier = 'cheap' | 'main'
export type RouteMode = 'auto' | 'off' | 'cheap'
export type RouteDecision = { tier: RouteTier; reason: string; prompt: string; isActive: boolean }
export type RouteStats = { cheapTurns: number; mainTurns: number; cheapAgents: number }

declare module 'claude-code' {
  interface PluginState {
    'model-router': { mode: RouteMode; decision: RouteDecision | null; stats: RouteStats }
  }
}
