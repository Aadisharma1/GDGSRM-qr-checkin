# app/routes/events.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.event import EventCreate, EventResponse
from app.models.event import Event
from app.database import SessionLocal
from app.utils.auth import get_current_user, admin_only
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventResponse, dependencies=[Depends(admin_only)])
def create_event(event: EventCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("/", response_model=list[EventResponse])
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).all()
