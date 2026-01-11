from database import Database

db = Database()

class Prescription:
    def __init__(self, patient_id, doctor_id, medications):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medications = medications
        self.prescription_id = None

    def add_prescription(self):
        self.prescription_id = len(db.cursor.execute("SELECT * FROM Appointments").fetchall()) + 1
        db.cursor.execute("""
            INSERT INTO Bills(appointment_id, patient_id, total_cost, payment_status)
            VALUES (?, ?, ?, 'pending')
        """, (self.prescription_id, self.patient_id, 100))
        db.conn.commit()

    @staticmethod
    def get_patient_prescriptions(patient_id):
        query = "SELECT * FROM Bills WHERE patient_id=?"
        db.cursor.execute(query, (patient_id,))
        return db.cursor.fetchall()