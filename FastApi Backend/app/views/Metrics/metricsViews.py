from app.views.Metrics import metricsRouter
from app.services.MetricsService import SendToRabbit,GetFromRabbit

@metricsRouter.post("/send")
async def ingest_metrics(data: dict):
    await SendToRabbit(data)
    return {"status": "ok"}

@metricsRouter.post("/get")
async def get_metrics():
    data = await GetFromRabbit()
    return {data,200}
   