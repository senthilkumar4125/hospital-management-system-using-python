from database import Database

db = Database()

class Bill:
    def __init__(self, patient_id=None, appointment_id=None, total_cost=100):
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.total_cost = total_cost
        self.payment_status = "pending"
        if patient_id and appointment_id:
            db.add_bill(appointment_id, patient_id, total_cost)

    # ===== VIEW ALL BILLS =====
    @staticmethod
    def view_all_bills(staff_access_level):
        if staff_access_level not in [2, 3]:
            print("Access denied")
            return []

        records = db.fetch("""
            SELECT Bills.id, Bills.appointment_id, Bills.patient_id, Patients.name, Appointments.date, Bills.total_cost, Bills.payment_status
            FROM Bills
            JOIN Patients ON Bills.patient_id = Patients.id
            JOIN Appointments ON Bills.appointment_id = Appointments.id
        """)
        bills = []
        for r in records:
            bills.append({
                "bill_id": r[0],
                "appointment_id": r[1],
                "patient_id": r[2],
                "patient_name": r[3],
                "appointment_date": r[4],
                "total_cost": r[5],
                "payment_status": r[6]
            })
        return bills

    # ===== VIEW PAID BILLS =====
    @staticmethod
    def view_paid_bills(staff_access_level):
        all_bills = Bill.view_all_bills(staff_access_level)
        return [b for b in all_bills if b["payment_status"] == "paid"]

    # ===== TOTAL PAID AMOUNT =====
    @staticmethod
    def total_paid_amount(staff_access_level):
        if staff_access_level not in [2, 3]:
            print("Access denied")
            return 0
        result = db.fetch("SELECT SUM(total_cost) FROM Bills WHERE payment_status='paid'")
        return result[0][0] if result[0][0] else 0

    # ===== MARK BILL AS PAID =====
    @staticmethod
    def mark_bill_as_paid(patient_id, staff_access_level):
        if staff_access_level not in [2, 3]:
            print("Access denied")
            return
        db.execute("UPDATE Bills SET payment_status='paid' WHERE patient_id=?", (patient_id,))
        print("✔ Bill(s) marked as paid")
