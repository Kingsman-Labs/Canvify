"""Input sanitization helpers shared across api/gateway.py and agents."""


def sanitize_text(text: str) -> str:
    # TODO: strip HTML/script tags, trim length
    return text.strip()
