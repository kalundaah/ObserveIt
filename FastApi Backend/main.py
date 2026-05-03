from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

metrics_buffer = []

@app.post("/metrics")
async def ingest_metrics(data: dict):
    metrics_buffer.append(data)
    return {"status": "ok"}

@app.get("/presentResults")
async def get_metrics():
    return metrics_buffer