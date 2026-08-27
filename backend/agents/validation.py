"""
Agent 6 — Validation
Independently cross-checks every upstream agent's output for consistency
(7 checks per Section 4 of the proposal: market vs revenue, pricing vs
competitors, LTV:CAC ratio, cost structure, marketing budget vs funding,
SWOT vs risk, overall coherence). On failure, flags the specific agent
to re-run via the Orchestrator's feedback loop (max 2 rounds).
"""


def validation_agent(state):
    # TODO: run the 7 consistency checks
    # TODO: on failure, set state["agents_to_rerun"] and return early
    # TODO: on pass, assign confidence scores per agent
    return state
