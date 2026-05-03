from fastapi import APIRouter, FastAPI

metricsRouter = APIRouter(prefix="/metrics",tags=["Metrics"])


from app.views.Metrics.metricsViews import ingest_metrics,get_metrics