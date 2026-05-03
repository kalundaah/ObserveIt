import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

database_url = os.getenv("DATABASE_URL")

Base = declarative_base()
engine = create_engine(database_url)
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)