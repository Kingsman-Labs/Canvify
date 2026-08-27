"""Centralized LLM prompt templates — one constant per agent, kept here
so prompt tuning never requires touching agent logic."""

IDEA_VALIDATOR_PROMPT = """Startup idea: {idea}
Market search results: {results}
Score viability 0-100. Return ONLY valid JSON: {{"score": <n>, "reasoning": "<text>"}}"""

# TODO: add prompt templates for the other 7 agents
