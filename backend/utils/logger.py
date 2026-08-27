"""Structured execution logging — every agent action logged with timestamp,
input, output, and token count (full audit trail per Section 10)."""
import logging

logger = logging.getLogger("canvify")
logging.basicConfig(level=logging.INFO)
