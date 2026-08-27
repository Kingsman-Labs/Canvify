"""
API Gateway — sits between the frontend and the Orchestrator.
Handles: authentication, per-session rate limiting, and input validation /
sanitization (10-2000 chars, strip HTML/script) before any agent runs.
See Section 10 (Safety, Guardrails, and Responsible AI) of the proposal.
"""


def authenticate(request):
    # TODO: verify session / API key
    pass


def check_rate_limit(session_id: str):
    # TODO: Redis-backed rate limit (50 searches, 100k tokens per session)
    pass


def validate_input(idea_text: str) -> bool:
    # TODO: length check, strip HTML/script, LLM harmful-content screen
    pass
