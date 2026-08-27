"""
Agent 0 — Orchestrator (Supervisor)
Parses the user's startup idea, builds the execution plan, dispatches each
specialist agent in the correct order (including the parallel Business Model
/ Marketing Strategy step), monitors progress, and manages the Validation
Agent's feedback loop (max 2 retries per Section 4.3 of the proposal).
"""


def orchestrator_agent(state):
    # TODO: parse user_input -> industry, product_type, target_market
    # TODO: build task dependency plan
    # TODO: route to idea_validator first
    return state
