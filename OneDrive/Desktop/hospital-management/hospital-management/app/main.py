from fastapi import FastAPI
from fastapi import Request, Form
from app.database import SessionLocal
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates 
from app.database import engine
from app.models import user, doctor, patient, appointment, billing
from app.routers import auth, doctors, patients, appointments, billing as billing_router

user.Base.metadata.create_all(bind=engine)
doctor.Base.metadata.create_all(bind=engine)
patient.Base.metadata.create_all(bind=engine)
appointment.Base.metadata.create_all(bind=engine)
billing.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rajiv Gandhi Government Hospital Management System"
)
templates = Jinja2Templates(directory="app/templates")
app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(billing_router.router)

@app.get("/")
def home():
    return {"message": "Hospital Management System Running"}

@app.get("/admin", response_class=HTMLResponse)
def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.post("/add-doctor")
def add_doctor(
    name: str = Form(...),
    specialization: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...)
):
    from sqlalchemy.orm import Session
    from app.database import SessionLocal
    from app.models.doctor import Doctor

    db = SessionLocal()
    new_doctor = Doctor(name=name, specialization=specialization, phone=phone, email=email)
    db.add(new_doctor)
    db.commit()
    db.close()
    return RedirectResponse("/admin?success=1", status_code=303)

@app.post("/add-patient")
def add_patient(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    phone: str = Form(...),
    email: str = Form(None),
    address: str = Form(None)
):
    from sqlalchemy.orm import Session
    from app.database import SessionLocal
    from app.models.patient import Patient

    db = SessionLocal()
    new_patient = Patient(name=name, age=age, gender=gender, phone=phone, email=email, address=address)
    db.add(new_patient)
    db.commit()
    db.close()
    return RedirectResponse("/admin?success=1", status_code=303)

@app.post("/add-doctor")
def add_doctor(
    name: str = Form(...),
    specialization: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...)
):
    from sqlalchemy.orm import Session
    from app.database import engine
    from app.models.doctor import Doctor

    db = Session(engine)
    new_doctor = Doctor(name=name, specialization=specialization, phone=phone, email=email)
    db.add(new_doctor)
    db.commit()
    db.close()
    return RedirectResponse("/admin?success=1", status_code=303)

@app.post("/add-patient")
def add_patient(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    phone: str = Form(...),
    email: str = Form(None),
    address: str = Form(None)
):
    from sqlalchemy.orm import Session
    from app.database import engine
    from app.models.patient import Patient

    db = Session(engine)
    new_patient = Patient(name=name, age=age, gender=gender, phone=phone, email=email, address=address)
    db.add(new_patient)
    db.commit()
    db.close()
    return RedirectResponse("/admin?success=1", status_code=303)