"""Session / report data models (Pydantic) for Supabase persistence."""
from pydantic import BaseModel


class Session(BaseModel):
    session_id: str
    user_input: str
    status: str
