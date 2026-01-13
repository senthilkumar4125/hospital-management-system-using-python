from pydantic import BaseModel

class BillCreate(BaseModel):
    patient_name: str
    doctor_name: str
    amount: int

class PaymentUpdate(BaseModel):
    status: str

