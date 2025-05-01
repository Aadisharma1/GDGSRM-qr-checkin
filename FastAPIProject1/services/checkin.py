# app/services/checkin.py
import json
from fastapi import HTTPException
from app.models.registration import Registration
from sqlalchemy.orm import Session

def decode_qr_data(qr_data: str) -> dict:
    try:
        return json.loads(qr_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid QR code data")

def mark_checked_in(user_id: int, event_id: int, db: Session):
    reg = db.query(Registration).filter_by(user_id=user_id, event_id=event_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    if reg.checked_in:
        raise HTTPException(status_code=400, detail="Already checked in")
    reg.checked_in = True
    db.commit()
    return {"message": "Check-in successful"}
