from database import Database

db = Database()

class Doctor:
    allDoctors = {}

    def __init__(self, doctor_id=None, name=None, specialty=None, age=None):
        self.id = doctor_id
        self.name = name
        self.specialty = specialty
        self.age = age
       
    @staticmethod
    def age(age):
        try:
            age = int(age)
        except ValueError:
            print("Invalid input for age. Please enter a number between 0 and 120.")
            age = int(input("Enter age: "))

        while not (0 < age <= 120):
            print("Invalid age. Please enter a number between 0 and 120.")
            age = int(input("Enter age: "))
        return age
    
    @staticmethod
    def sign_up(name, specialty, age):
        doctor_id = db.add_doctor(name, specialty)
        if doctor_id:
            doctor = Doctor(doctor_id, name, specialty, age)
            Doctor.allDoctors[doctor_id] = doctor
            print(f"✔ Dr.{name} added successfully with ID {doctor_id}")
            return doctor
        return None
    
    @staticmethod
    def login(doctor_id):
        for d in db.get_all_doctors():
            if d[0] == doctor_id:
                print("✔ Login successful!")
                return Doctor(d[0], d[1], d[2])
        print("Doctor ID not found.")
        return None
    
    @staticmethod
    def get_all_doctors():
        return db.get_all_doctors()

    # def add_time_slot(self, day, time_from, time_to):
    #     self.time_slots.append({"day": day, "from": time_from, "to": time_to})

    def view_assigned_patients(self):
        return db.get_doctor_patients(self.id)

    def view_appointments(self):
        query = "SELECT * FROM Appointments WHERE doctor_id=?"
        return db.fetch(query, (self.id,))

    def profile(self):
        return {
            "doctor_id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "age": self.age,
           
        }
