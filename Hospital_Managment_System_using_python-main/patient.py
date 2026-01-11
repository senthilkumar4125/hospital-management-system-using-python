import time
from Staff_Window import patient_list_f
from database import Database
from bill import Bill

db = Database()

class Patient:
    def __init__(self, id, name, age, gender, username, password, problem=None, assigned_doctor=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.username = username
        self.password = password
        self.problem = problem
        self.assigned_doctor = assigned_doctor

    @staticmethod
    def signup(name, age, gender, username, password):
        patient_id = db.add_patient(name, age, gender, username, password)
        if patient_id:
            print(f"✔ Signup successful! Your Patient ID: {patient_id}")
            return Patient(patient_id, name, age, gender, username, password)
        return None

    @staticmethod
    def login(username, password):
        record = db.get_patient_by_username(username)
        if record and record[5] == password:
            print("✔ Login successful!")
            return Patient(*record)
        print("❌ Invalid username or password")
        return None

    def view_doctors(self):
        return db.get_all_doctors()

    @staticmethod
    def date():
        print("1.Sunday \n2.Monday \n3.Tuesday \n4.Wednesday \n5.Thursday \n6.Friday \n7.Saturday")
        day = input("Enter day: ")
        if day not in ['1','2','3','4','5','6','7']:
            print("Invalid day. Please enter a number between 1 and 7.")
            return Patient.date()
        else:
            day_dict = {
                '1': 'Sunday',
                '2': 'Monday',
                '3': 'Tuesday',
                '4': 'Wednesday',
                '5': 'Thursday',
                '6': 'Friday',
                '7': 'Saturday'
            }
            day = day_dict[day]
            return day
        

    def book_appointment(self, doctor_id, day, hour, minuts, problem):
        self.problem = problem
        self.assigned_doctor = doctor_id
        try:
            hour = int(hour)
            minuts = int(minuts)
            doctor_id = int(doctor_id)
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

        db.execute(
            "UPDATE Patients SET problem=?, assigned_doctor=? WHERE id=?",
            (problem, doctor_id, self.id)
        )
        full_date = f"{day} - {time}"
        appointment_id = db.add_appointment(self.id, doctor_id, full_date, problem)
        Bill(self.id, appointment_id)
        return appointment_id

    def view_appointments(self):
        return db.get_patient_appointments(self.id)

    def edit_appointment(self,appointment_id, day, hour, minuts, new_notes):
        try:
            hour = int(hour)
            minuts = int(minuts)
            appointment_id = int(appointment_id)
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
        new_date = f"{day} - {time}"
        db.edit_appointment(appointment_id, new_date, new_notes)
        return 1

    def delete_appointment(self, appointment_id):
        db.delete_appointment(appointment_id)

    def view_bill(self, appointment_id):
        return db.get_bill(appointment_id)

    def pay_bill(self, appointment_id):
        bill = db.get_bill(appointment_id)
        if bill:
            db.update_bill_status(appointment_id, "paid")
            return "✔ Payment successful!"
        return "❌ Bill not found"
