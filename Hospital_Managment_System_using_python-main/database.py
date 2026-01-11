import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("hospitalnew7.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                username TEXT UNIQUE,
                password TEXT,
                problem TEXT,
                assigned_doctor INTEGER
            )
        """)
      
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctors(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                specialty TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                doctor_id INTEGER,
                date TEXT,
                notes TEXT,
                payment_status TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Bills(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_id INTEGER,
                patient_id INTEGER,
                total_cost REAL,
                payment_status TEXT
            )
        """)
        


        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS Staff(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        role TEXT,
        access_level INTEGER,
        username TEXT,
        password TEXT
    )
""")
        
        self.cursor.execute("""
        INSERT INTO Staff  
        (name, age, gender, role, access_level, username, password) 
        VALUES ('Admin',30,'M','Admin',3,'admin','1234')
""")

        self.cursor.execute("""
    INSERT INTO Staff  
(name, age, gender, role, access_level, username, password) 
VALUES ('casher',30,'M','casher',1,'casher','1234')
""")
        self.conn.commit()
        

    # ===== Patients =====
    def add_patient(self, name, age, gender, username, password, problem=None, assigned_doctor=None):
        self.cursor.execute("SELECT * FROM Patients WHERE username=?", (username,))
        if self.cursor.fetchone():
            print(f"Username '{username}' already exists!")
            return None
        self.cursor.execute("""
            INSERT INTO Patients (name, age, gender, username, password, problem, assigned_doctor)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, age, gender, username, password, problem, assigned_doctor))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_patient_by_username(self, username):
        self.cursor.execute("SELECT * FROM Patients WHERE username=?", (username,))
        return self.cursor.fetchone()

    def get_patient_appointments(self, patient_id):
        self.cursor.execute("SELECT * FROM Appointments WHERE patient_id=?", (patient_id,))
        return self.cursor.fetchall()

    # ===== Doctors =====
    def add_doctor(self, name, specialty):
        self.cursor.execute("INSERT INTO Doctors (name, specialty) VALUES (?, ?)", (name, specialty))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_doctors(self, specialty=""):
        if specialty:
            self.cursor.execute("SELECT * FROM Doctors WHERE specialty LIKE ?", ('%'+specialty+'%',))
        else:
            self.cursor.execute("SELECT * FROM Doctors")
        return self.cursor.fetchall()

    # ===== Appointments =====
    def add_appointment(self, patient_id, doctor_id, date, notes):
        self.cursor.execute("""
            INSERT INTO Appointments(patient_id, doctor_id, date, notes, payment_status)
            VALUES (?, ?, ?, ?, 'pending')
        """, (patient_id, doctor_id, date, notes))
        self.conn.commit()
        return self.cursor.lastrowid

    def edit_appointment(self, appointment_id, new_date=None, new_notes=None):
        if new_date:
            self.cursor.execute("UPDATE Appointments SET date=? WHERE id=?", (new_date, appointment_id))
        if new_notes:
            self.cursor.execute("UPDATE Appointments SET notes=? WHERE id=?", (new_notes, appointment_id))
        self.conn.commit()

    

   
    
    def delete_appointment(self, appointment_id):
        appointment = self.execute(
        "SELECT id FROM Appointments WHERE id=?",
        (appointment_id,),
        fetchone=True ) 

        if not appointment:
          print("❌ Appointment not found")
          return
        else :
          self.execute("DELETE FROM Bills WHERE appointment_id=?", (appointment_id,))
          self.execute("DELETE FROM Appointments WHERE id=?", (appointment_id,))

          print("✔ Appointment deleted successfully")

    # ===== Bills =====
    def add_bill(self, appointment_id, patient_id, total_cost=100):
        self.cursor.execute("""
            INSERT INTO Bills(appointment_id, patient_id, total_cost, payment_status)
            VALUES (?, ?, ?, 'pending')
        """, (appointment_id, patient_id, total_cost))
        self.conn.commit()

    def update_bill_status(self, appointment_id, status):
        self.cursor.execute("UPDATE Bills SET payment_status=? WHERE appointment_id=?", (status, appointment_id))
        self.conn.commit()

    def get_bill(self, appointment_id):
        self.cursor.execute("SELECT * FROM Bills WHERE appointment_id=?", (appointment_id,))
        return self.cursor.fetchone()

    # ===== Staff / Doctor helper functions =====
    def get_doctor_patients(self, doctor_id):
        self.cursor.execute("""
            SELECT id, name, age, gender, problem 
            FROM Patients WHERE assigned_doctor=?
        """, (doctor_id,))
        return self.cursor.fetchall()

    def fetch(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

 

    def execute(self, query, params=(), fetchone=False, fetchall=False):
       self.cursor.execute(query, params)
       if fetchone:
        return self.cursor.fetchone()
       if fetchall:
        return self.cursor.fetchall()
       self.conn.commit()

    def delete_patient(self, patient_id):
        
        self.cursor.execute("DELETE FROM Bills WHERE patient_id=?", (patient_id,))
        self.cursor.execute("DELETE FROM Appointments WHERE patient_id=?", (patient_id,))
        self.cursor.execute("DELETE FROM Patients WHERE id=?", (patient_id,))
        self.conn.commit()

    