"""
FastAPI application entry point.
Wires together the API Gateway, REST routes, and WebSocket handler,
and exposes the compiled LangGraph workflow to the outside world.
"""
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="Canvify")


@app.get("/health")
def health():
    return {"status": "ok", "message": "Canvify backend is running"}


# TODO: include routers from api/routes.py and api/websocket.py
# TODO: mount api/gateway.py middleware (auth, rate limiting, input validation)
