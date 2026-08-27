"""Shared state schema — the single object every agent reads from and writes to.
No agent calls another agent directly (Section 4.3 of the proposal)."""
from typing import TypedDict, Optional, List


class AgentState(TypedDict):
    user_input: dict
    idea_validation: Optional[dict]
    market_research: Optional[dict]
    business_model: Optional[dict]
    marketing_strategy: Optional[dict]
    financial_analysis: Optional[dict]
    validation_result: Optional[dict]
    final_report: Optional[dict]
    feedback_loop_count: int
    agents_to_rerun: List[str]
    execution_log: List[dict]
