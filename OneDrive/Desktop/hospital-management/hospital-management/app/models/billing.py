from sqlalchemy import Column, Integer, String
from app.database import Base

class Billing(Base):
    __tablename__ = "billing"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    doctor_name = Column(String)
    amount = Column(Integer)
    status = Column(String)

