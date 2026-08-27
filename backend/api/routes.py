"""REST endpoints — /analyze (submit idea), /report/{id} (fetch result)."""
from fastapi import APIRouter

router = APIRouter()


@router.post("/analyze")
def analyze(idea: str):
    # TODO: gateway.validate_input -> app_graph.invoke -> return result
    pass


@router.get("/report/{report_id}")
def get_report(report_id: str):
    # TODO: fetch saved report from Supabase
    pass
