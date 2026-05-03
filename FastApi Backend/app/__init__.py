import os
from config import ProductionConfig, DevelopmentConfig
from db import engine, Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.views.Metrics import metricsRouter


def create_app(test_config=None):
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_routes(app)

    return app


def register_routes(app: FastAPI):
    app.include_router(metricsRouter)
