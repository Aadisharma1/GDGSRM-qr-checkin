# app/models/registration.py
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.database import Base

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    checked_in = Column(Boolean, default=False)
