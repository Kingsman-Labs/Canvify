"""WebSocket handler — streams live per-agent progress events to the
frontend dashboard as each stage of the pipeline completes."""
from fastapi import WebSocket


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # TODO: subscribe to execution_log updates, push to client
