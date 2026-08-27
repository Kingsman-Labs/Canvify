"""
Centralized settings loader.
Reads ANTHROPIC_API_KEY, TAVILY_API_KEY, SUPABASE_URL, REDIS_URL, etc.
from environment variables (see .env.example).
"""
import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
