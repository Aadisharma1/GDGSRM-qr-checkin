from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
