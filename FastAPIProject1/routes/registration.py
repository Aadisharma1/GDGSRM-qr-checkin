# app/routes/registration.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.registration import Registration
from app.models.event import Event
from app.database import SessionLocal
from app.services.qr import generate_qr_code
from app.services.email import send_qr_email
from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{event_id}")
def register_for_event(event_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if db.query(Registration).filter_by(user_id=user.id, event_id=event_id).first():
        raise HTTPException(status_code=400, detail="Already registered")

    registration = Registration(user_id=user.id, event_id=event_id)
    db.add(registration)
    db.commit()
    db.refresh(registration)

    qr_data = {"user_id": user.id, "event_id": event_id}
    qr_image = generate_qr_code(qr_data)
    send_qr_email(user.email, event.title, qr_image)

    return {"message": "Registered and QR sent"}
