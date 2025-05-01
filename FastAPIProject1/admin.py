from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.registration import Registration
from app.models.event import Event
from app.database import SessionLocal
from app.utils.auth import admin_only
from fastapi.responses import JSONResponse
import csv
import io

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/attendees/{event_id}")
def attendees(event_id: int, db: Session = Depends(get_db), _=Depends(admin_only)):
    attendees = db.query(Registration).filter_by(event_id=event_id).all()
    return attendees

@router.get("/summary/{event_id}")
def summary(event_id: int, db: Session = Depends(get_db), _=Depends(admin_only)):
    total = db.query(Registration).filter_by(event_id=event_id).count()
    checked = db.query(Registration).filter_by(event_id=event_id, checked_in=True).count()
    return {"total": total, "checked_in": checked}

@router.get("/export/{event_id}")
def export(event_id: int, db: Session = Depends(get_db), _=Depends(admin_only)):
    registrations = db.query(Registration).filter_by(event_id=event_id).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "user_id", "event_id", "checked_in"])
    for reg in registrations:
        writer.writerow([reg.id, reg.user_id, reg.event_id, reg.checked_in])
    return JSONResponse(content={"csv": output.getvalue()})
