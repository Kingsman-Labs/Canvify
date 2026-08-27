"""
Agent 1 — Idea Validator
Pre-screens the startup idea for viability before deep research begins.
Computes a 0-100 viability score using Startup Genome Matching (ChromaDB)
and quick web searches; proposes pivot directions if score < 40.
"""


def idea_validator_agent(state):
    # TODO: tavily search for similar products / market saturation
    # TODO: query ChromaDB startup genome for similar past startups
    # TODO: LLM scores viability 0-100, returns risk_flags + recommendation
    return state
