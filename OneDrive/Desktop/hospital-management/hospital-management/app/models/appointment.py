from sqlalchemy import Column, Integer, String
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    doctor_name = Column(String)
    time_slot = Column(String)
    status = Column(String)

