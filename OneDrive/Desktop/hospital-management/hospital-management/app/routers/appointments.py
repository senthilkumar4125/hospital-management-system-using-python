from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.appointment import AppointmentCreate
from app.services.appointment_service import book_appointment
from app.core.dependencies import role_required

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", dependencies=[Depends(role_required("patient"))])
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    status = book_appointment(data, db)
    return {"appointment_status": status}

