# API Reference

## POST /analyze
Body: `{ "idea": "string" }`
Returns: full AgentState JSON once the pipeline completes.

## GET /report/{report_id}
Returns: a previously saved report.

## WS /ws?session={id}
Streams live per-agent progress events.
