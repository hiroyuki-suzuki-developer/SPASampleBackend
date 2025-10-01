from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from core.config import get_env

Engine = create_engine(
    get_env().database_url,
    echo=False,
    pool_pre_ping=True
)

BaseModel = declarative_base()
