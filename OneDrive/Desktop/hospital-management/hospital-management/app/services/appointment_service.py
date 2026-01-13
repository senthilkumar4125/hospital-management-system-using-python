from sqlalchemy.orm import Session
from app.models.appointment import Appointment

def book_appointment(data, db: Session):
    existing = db.query(Appointment).filter(
        Appointment.doctor_name == data.doctor_name,
        Appointment.time_slot == data.time_slot,
        Appointment.status == "BOOKED"
    ).first()

    status = "WAITING" if existing else "BOOKED"

    appointment = Appointment(
        patient_name=data.patient_name,
        doctor_name=data.doctor_name,
        time_slot=data.time_slot,
        status=status
    )

    db.add(appointment)
    db.commit()
    return status

