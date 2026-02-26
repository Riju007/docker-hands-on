from fastapi import FastAPI
import httpx

app = FastAPI(debug=True, title="Polyglot FAST API APP")


@app.get("/health")
def health():
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
