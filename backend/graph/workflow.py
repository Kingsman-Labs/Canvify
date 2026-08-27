"""LangGraph StateGraph definition — wires all 8 agent nodes together,
including the parallel Business Model / Marketing Strategy step and the
Validation Agent's conditional feedback loop."""
from langgraph.graph import StateGraph, END
from graph.state import AgentState
# TODO: import all 8 agent functions from agents/

workflow = StateGraph(AgentState)

# TODO: workflow.add_node(...) for each of the 8 agents
# TODO: workflow.set_entry_point("orchestrator")
# TODO: workflow.add_conditional_edges(...) — see graph/routing.py

app_graph = workflow.compile()
