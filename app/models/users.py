from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    gender = Column(String(10), nullable=True)
    created_datetime = Column(DateTime, default=datetime.now)
    created_user_id = Column(Integer, default=None)
    updated_datetime = Column(DateTime, default=datetime.now)
    updated_user_id = Column(Integer, default=None)
    deleted_datetime = Column(DateTime, default=None)
    deleted_user_id = Column(Integer, default=None)
