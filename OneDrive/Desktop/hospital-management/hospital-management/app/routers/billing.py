from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.billing import Billing
from app.schemas.billing import BillCreate, PaymentUpdate
from app.core.dependencies import role_required

router = APIRouter(prefix="/billing", tags=["Billing"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", dependencies=[Depends(role_required("admin"))])
def create_bill(data: BillCreate, db: Session = Depends(get_db)):
    bill = Billing(
        patient_name=data.patient_name,
        doctor_name=data.doctor_name,
        amount=data.amount,
        status="UNPAID"
    )
    db.add(bill)
    db.commit()
    return {"message": "Bill created"}

@router.get("/", dependencies=[Depends(role_required("patient"))])
def view_bills(db: Session = Depends(get_db)):
    return db.query(Billing).all()

@router.put("/{bill_id}", dependencies=[Depends(role_required("admin"))])
def update_payment(bill_id: int, data: PaymentUpdate, db: Session = Depends(get_db)):
    bill = db.query(Billing).get(bill_id)
    bill.status = data.status
    db.commit()
    return {"message": "Payment updated"}

