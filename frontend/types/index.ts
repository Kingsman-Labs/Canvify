// Shared TypeScript interfaces mirroring backend/graph/state.py
export interface AgentState {
  userInput: string;
  ideaValidation?: Record<string, unknown>;
  marketResearch?: Record<string, unknown>;
  // TODO: mirror remaining fields from AgentState (Python)
}
