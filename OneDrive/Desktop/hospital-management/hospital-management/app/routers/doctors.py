from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate
from app.core.dependencies import role_required

router = APIRouter(prefix="/doctors", tags=["Doctors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", dependencies=[Depends(role_required("admin"))])
def add_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    doctor = Doctor(**data.dict())
    db.add(doctor)
    db.commit()
    return {"message": "Doctor added"}

@router.get("/")
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

