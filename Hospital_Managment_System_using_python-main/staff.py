from database import Database
from bill import Bill

db = Database()

class Staff:
    def __init__(self, id, name, age, gender, role, access_level):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
        self.access_level = access_level
        self.db = Database()  
    @staticmethod
    def login(username, password):
        data = db.fetch("SELECT * FROM Staff WHERE username=? AND password=?", (username, password))
        if data:
            s = data[0]
            print(f"✔ Welcome {s[1]}")
            return Staff(s[0], s[1], s[2], s[3], s[4], s[5])
        else:
            print("❌ Invalid username or password")
            return None
        
    # ===== ADD APPOINTMENT =====
    def add_appointment(self, patient_id, doctor_id, day, hour, minute, notes=""):
        patient = db.fetch("SELECT id FROM Patients WHERE id=?",(patient_id)) 

        if not patient:
            print("❌ patient not found")
            return None

        doctor = db.fetch("SELECT id FROM Doctors WHERE id=?",(doctor_id)) 

        if not doctor:
            print("❌ Doctor not found")
            return None

        if self.access_level not in [2, 3]:
            print("Access denied")
            return None 
        try:
            hour = int(hour)
            minute = int(minute)
            doctor_id = int(doctor_id)
        except ValueError:
            print("Invalid input for hour or Invalid input for minutes.\n Please enter a number between 0 and 23.\nPlease enter a number between 0 and 59.")  
            return None
        if not (0 <= int(hour) <= 23):
            print("Invalid time entered. Please enter a valid hour (0-23).")
            return None
        if not (0 <= int(minute) <= 59):
            print("Invalid time entered. Please enter a valid minutes (0-59).")
            return None
        formatted_date = f"{day} - {hour}:{minute}"
        db.execute(
            "UPDATE Patients SET problem=?, assigned_doctor=? WHERE id=?",
            (notes, doctor_id, patient_id)
        )
        appointment_id = self.db.add_appointment(patient_id, doctor_id, formatted_date, notes)
        Bill(patient_id, appointment_id)
        print(f"✔ Appointment added with ID: {appointment_id}")
        return appointment_id

    # ===== ADD PATIENT =====
    def add_patient(self, name, age, gender, problem, assigned_doctor):
        if self.access_level in [1,3]:
            username = f"{name.lower()}{age}"
            password = "defaultpass"
            self.db.add_patient(name, age, gender, username, password, problem, assigned_doctor)
            print(f"✔ Patient {name} added successfully")
        else:
            print("Access denied")

    # ===== UPDATE PATIENT =====
    def update_patient(self, patient_id, name, age, gender, problem):
        if self.access_level == 3:
            self.db.execute("UPDATE Patients SET name=?, age=?, gender=?, problem=? WHERE id=?",
                            (name, age, gender, problem, patient_id))
            print(f"✔ Patient {patient_id} updated")
        else:
            print("Access denied")

    # ===== DELETE PATIENT =====
    def delete_patient(self, patient_id):
        if self.access_level != 3:
            print("Access denied")
            return
        patient = self.db.execute("SELECT id FROM Patients WHERE id=?", (patient_id,), fetchone=True)
        if not patient:
                print("❌ Patient not found, nothing to delete")
                return
        # delete patient's appointments and bills
        appointments = self.db.get_patient_appointments(patient_id)
        for app in appointments:
            self.db.delete_appointment(app[0])
        # delete patient
        self.db.execute("DELETE FROM Patients WHERE id=?", (patient_id,))
        print(f"✔ Patient {patient_id} and related appointments deleted")
        
    # ===== VIEW PATIENTS =====
    def view_patients(self):
        return self.db.fetch("SELECT * FROM Patients")

    # ===== VIEW DOCTORS =====
    def view_doctors(self):
        return self.db.get_all_doctors()

    # ===== VIEW APPOINTMENTS =====
    def view_appointments(self, patient_id=None):
        if patient_id:
            return self.db.get_patient_appointments(patient_id)
        else:
            return self.db.fetch("SELECT * FROM Appointments")
    

    # ===== BILLS =====
    def view_all_bills(self):
        bill = Bill()
        return bill.view_all_bills(self.access_level)

    def view_paid_bills(self):
        bill = Bill()
        return bill.view_paid_bills(self.access_level)

    def total_paid_amount(self):
        bill = Bill()
        return bill.total_paid_amount(self.access_level)

