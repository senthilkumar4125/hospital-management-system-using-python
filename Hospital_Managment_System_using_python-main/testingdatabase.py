import unittest
from database import Database
import os

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
      
        if os.path.exists("hospital.db"):
            os.remove("hospital.db")
        cls.db = Database()

    # ==================== Patients ====================
    def test_add_and_get_patient(self):
        self.db.add_patient(1, "Maya", 25, "Female", "Headache")
        patient = self.db.get_patient(1)
        self.assertEqual(patient, (1, "Maya", 25, "Female", "Headache"))

    # ==================== Doctors =====================
    def test_add_and_get_doctor(self):
        self.db.add_doctor(1, "Dr. Ahmed", "Orthopedic")
        self.db.add_doctor(2, "Dr. Sara", "Neurology")
        doctors = self.db.get_doctors_by_specialty("Neurology")
        self.assertEqual(doctors, [(2, "Dr. Sara", "Neurology")])

    # ==================== Appointments =================
    def test_add_and_get_appointment(self):
        appointment_id = self.db.add_appointment(1, 2, "2025-12-28", "First visit")
        appointments = self.db.get_patient_appointments(1)
        self.assertTrue(any(a[0] == appointment_id for a in appointments))

    # ==================== Prescriptions =================
    def test_add_prescription(self):
        self.db.add_prescription(1, 2, "Paracetamol", "500mg", 10.5)
       
        self.db.cursor.execute("SELECT * FROM Prescriptions WHERE patient_id=1 AND doctor_id=2")
        prescription = self.db.cursor.fetchone()
        self.assertIsNotNone(prescription)

    # ==================== Bills ========================
    def test_add_and_update_bill(self):
        appointment_id = self.db.add_appointment(1, 2, "2025-12-30", "Follow-up")
        self.db.add_bill(appointment_id, 1, 50)
        bill = self.db.get_bill(appointment_id)
        self.assertEqual(bill[3], 50)
        self.assertEqual(bill[4], "pending")
       
        self.db.update_bill_status(appointment_id, "paid")
        updated_bill = self.db.get_bill(appointment_id)
        self.assertEqual(updated_bill[4], "paid")


if __name__ == "__main__":
    unittest.main()
