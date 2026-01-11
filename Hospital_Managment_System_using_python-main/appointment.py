from database import Database

db = Database()

class Appointment:
    def __init__(self, patient_id, doctor_id, date, notes=""):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.notes = notes
        self.payment_status = "pending"
        self.id = db.add_appointment(patient_id, doctor_id, date, notes)

    # ===== ADD APPOINTMENT =====
    @staticmethod
    def add(patient_id, doctor_id, date, notes=""):
        return Appointment(patient_id, doctor_id, date, notes)

    # ===== UPDATE APPOINTMENT =====
    def update(self, day, hour, minuts, new_notes=None):
        try:
            hour = int(hour)
            minuts = int(minuts)
        except ValueError:
            print("Invalid input for hour or Invalid input for minuts.\n Please enter a number between 0 and 23.\nPlease enter a number between 0 and 59.")  
            return None
        if not (0 <= int(hour) <= 23):
            print("Invalid time entered. Please enter a valid hour (0-23).")
            return None
        if not (0 <= int(minuts) <= 59):
            print("Invalid time entered. Please enter a valid minuts (0-59).")
            return None

        time = f"{hour}:{minuts}"

        if time:
            self.time = time
        else:
            return None

        if new_notes:
            self.notes = new_notes
        else:
            return None
        
        new_date = f"{day} - {time}"
        db.edit_appointment(self.id, new_date, new_notes)
        print(f"✔ Appointment ID {self.id} updated successfully at {new_date}!")
        return 1

    # ===== DELETE APPOINTMENT =====
    def delete(self):
        db.delete_appointment(self.id)
        print(f"✔ Appointment ID {self.id} deleted successfully!")

    # ===== VIEW PATIENT APPOINTMENTS =====
    @staticmethod
    def get_patient_appointments(patient_id):
        records = db.get_patient_appointments(patient_id)
        appointments = []
        for r in records:
            appt = Appointment(r[1], r[2], r[3], r[4])
            appt.id = r[0]
            appt.payment_status = r[5]
            appointments.append(appt)
        return appointments

    # ===== VIEW APPOINTMENT DETAILS =====
    def details(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date": self.date,
            "notes": self.notes,
            "status": self.payment_status
        }

e = Appointment.update_appointments(1)
print(e)