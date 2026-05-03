from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
from app import create_app

app = create_app()
