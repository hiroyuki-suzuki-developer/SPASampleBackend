from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("Users.id"))
    created_datetime = Column(DateTime, default=datetime.now)
    created_user_id = Column(Integer, default=None)
    updated_datetime = Column(DateTime, default=datetime.now)
    updated_user_id = Column(Integer, default=None)
    deleted_datetime = Column(DateTime, default=None)
    deleted_user_id = Column(Integer, default=None)

    owner = relationship("Users", back_populates="items")
