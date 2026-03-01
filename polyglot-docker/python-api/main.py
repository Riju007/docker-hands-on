import json
import httpx
import logging
from fastapi import FastAPI
from datetime import datetime, UTC

logger = logging.getLogger("python-service")
logging.basicConfig(level=logging.INFO)

app = FastAPI(debug=True, title="Polyglot FAST API APP")


def log_json(level, message, **kwargs):
    log_entry = {
        "service": "python",
        "level": level,
        "message": message,
        "timestamp": datetime.now(UTC).isoformat(),
        **kwargs,
    }
    print(json.dumps(log_entry))


@app.get("/health")
def health():
    log_json("info", "Health check called")
    data = {"service": "python", "status": "ok"}
    return data


@app.get("/aggregate")
async def aggregate():
    async with httpx.AsyncClient() as client:
        # node = await client.get("http://localhost:3000/info")
        # rust = await client.get("http://localhost:4000/info")
        node = await client.get("http://node:3000/info")
        rust = await client.get("http://rust:4000/info")

    payload = {
        "python": "Running",
        "node": node.json(),
        "rust": rust.json(),
    }
    return payload
