"""Full pipeline integration test — runs 5 structurally different sample
startup ideas (B2B SaaS, marketplace, consumer product) end-to-end through
all 8 agents, and injects a known inconsistency to verify the Validation
Agent's feedback loop triggers and resolves correctly."""


def test_full_pipeline_happy_path():
    # TODO: app_graph.invoke(sample_idea), assert final_report is produced
    pass


def test_feedback_loop_triggers_on_bad_unit_economics():
    # TODO: inject artificially low CAC, assert re-run occurs, capped at 2 rounds
    pass
