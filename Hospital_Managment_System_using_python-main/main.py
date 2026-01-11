from database import Database
from patient import Patient
from doctor import Doctor
from staff import Staff
from bill import Bill

db = Database()

def main():

    print("--- Welcome to Hospital System ---")
    user_type = ""
    while user_type not in ["1", "2", "3"]:
        print("\nWho are you?")
        print("1) Patient")
        print("2) Doctor")
        print("3) Staff")
        user_type = input("Enter choice: ")

    current_user = None

    # ================= Patient =================
    if user_type == "1":
        while not current_user:
            print("\n1) Login")
            print("2) Signup")
            choice = input("Enter choice: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                patient = Patient.login(username, password)
                if patient:
                    current_user = patient
                else:
                    print("❌ Invalid credentials, try again.")
            elif choice == "2":
                name = input("Name: ")
                age = (input("Age: "))
                Doctor.age(age)
                gender = input("Gender: ")
                username = input("Choose username: ")
                password = input("Choose password: ")
                patient = Patient.signup(name, age, gender, username, password)
                if patient:
                    current_user = patient
                else:
                    print("❌ Signup failed, try again.")
            else:
                print("Invalid choice!")
        patient_menu(current_user)

    # ================= Doctor =================
    elif user_type == "2":
        while not current_user:
            print("\n1) Login (by ID)")
            print("2) Signup")
            choice = input("Enter choice: ")
            if choice == "1":
                doctor_id = int(input("Enter your Doctor ID: "))
                for d in Doctor.get_all_doctors():
                    if d[0] == doctor_id:
                        current_user = Doctor(d[0], d[1], d[2], age=None)
                        break
                if not current_user:
                    print("Doctor ID not found.")
            elif choice == "2":
                name = input("Name: ")
                specialty = input("Specialty: ")
                age = (input("Age: "))
                Doctor.age(age)
                current_user = Doctor.sign_up(name, specialty, age)
            else:
                print("Invalid choice!")
        doctor_menu(current_user)

# ================= Staff =================
    elif user_type == "3":
     current_user = None
    while not current_user:
        print("\n--- Staff Login ---")
        username = input("Username: ")
        password = input("Password: ")
        staff = Staff.login(username, password)
        if staff:
            current_user = staff
        else:
            print("Try again!")

    staff_menu(current_user)

# ================= Patient Menu =================
def patient_menu(patient):
    while True:
        print("\n--- Patient Menu ---")
        print("1) Show Doctors")
        print("2) Book Appointment")
        print("3) View My Appointments")
        print("4) Edit Appointment")
        print("5) Delete Appointment")
        print("6) View Bills")
        print("7) Pay Bill")
        print("8) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            doctors = patient.view_doctors()
            print("\nDoctors:")
            for d in doctors:
                print(f"{d[0]}) {d[1]} - {d[2]}")

        elif choice == "2":
            doctors = patient.view_doctors()
            print("\nDoctors:")
            for d in doctors:
                print(f"{d[0]}) {d[1]} - {d[2]}")
            doc_id = int(input("Enter Doctor ID to book: "))
            day = input("Enter day (e.g., Monday): ")
            time = input("Enter time (e.g., 10:00): ")
            problem = input("Enter problem/notes: ")
            appointment_id = patient.book_appointment(doc_id, day, time, problem)
            print(f"✔ Appointment booked with ID: {appointment_id}")

        elif choice == "3":
            appointments = patient.view_appointments()
            print("\nMy Appointments:")
            for a in appointments:
                print(f"ID: {a[0]}, Doctor ID: {a[2]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")

        elif choice == "4":
            app_id = int(input("Enter Appointment ID to edit: "))
            new_date = input("Enter new date (leave empty to keep): ")
            new_notes = input("Enter new notes (leave empty to keep): ")
            patient.edit_appointment(app_id, new_date if new_date else None, new_notes if new_notes else None)
            print("✔ Appointment updated!")

        elif choice == "5":
            app_id = int(input("Enter Appointment ID to delete: "))
            patient.delete_appointment(app_id)
            print("✔ Appointment deleted!")

        elif choice == "6":
            appointments = patient.view_appointments()
            print("\nMy Bills:")
            for a in appointments:
                bill = patient.view_bill(a[0])
                if bill:
                    print(f"Appointment ID: {bill[1]}, Patient ID: {bill[2]}, Total: {bill[3]}, Status: {bill[4]}")

        elif choice == "7":
            app_id = int(input("Enter Appointment ID to pay: "))
            result = patient.pay_bill(app_id)
            print(result)

        elif choice == "8":
            break
        else:
            print("Invalid choice!")


# ================= Doctor Menu =================
def doctor_menu(doctor):
    while True:
        print("\n--- Doctor Menu ---")
        print("1) View Assigned Patients")
        print("2) View Appointments")
        print("3) View Profile")
        print("4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            patients = doctor.view_assigned_patients()
            print("\nAssigned Patients:")
            if not patients:
                print("No patients assigned.")
            for p in patients:
                print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}, Problem: {p[4]}")

        elif choice == "2":
            appointments = doctor.view_appointments()
            print("\nAppointments:")
            if not appointments:
                print("No appointments found.")
            for a in appointments:
                print(f"ID: {a[0]}, Patient ID: {a[1]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")

        elif choice == "3":
            profile = doctor.profile()
            print("\nProfile:")
            for key, value in profile.items():
                print(f"{key}: {value}")

        elif choice == "4":
            break
        else:
            print("Invalid choice!")




# ================= Staff Menu =================
def staff_menu(staff):
    while True:
        print("\n--- Staff Menu ---")
        print("1) Add Patient")
        print("2) Update Patient")
        print("3) Delete Patient")
        print("4) View Patients")
        print("5) View Doctors")
        print("6) View Appointments")
        print("7) View All Bills")
        print("8) View Paid Bills")
        print("9) View Total Paid Amount")
        print("10) Exit")
        print("11) Add Appointment")  # <-- الجديد
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Patient Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            problem = input("Problem: ")
            assigned_doctor = int(input("Assign Doctor ID: "))
            staff.add_patient(name, age, gender, problem, assigned_doctor)

        elif choice == "2":
            pid = int(input("Patient ID to update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            gender = input("New Gender: ")
            problem = input("New Problem: ")
            staff.update_patient(pid, name, age, gender, problem)

        elif choice == "3":
            pid = int(input("Patient ID to delete: "))
            staff.delete_patient(pid)

        elif choice == "4":
            patients = staff.view_patients()
            print("\nPatients:")
            for p in patients:
                print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}, Problem: {p[6]}")

        elif choice == "5":
            doctors = staff.view_doctors()
            print("\nDoctors:")
            for d in doctors:
                print(f"ID: {d[0]}, Name: {d[1]}, Specialty: {d[2]}")

        elif choice == "6":
            pid = int(input("Enter Patient ID to view appointments: "))
            appointments = staff.view_appointments(pid)
            print("\nAppointments:")
            for a in appointments:
                print(f"ID: {a[0]}, Doctor ID: {a[2]}, Date: {a[3]}, Notes: {a[4]}, Status: {a[5]}")

        elif choice == "7":
            bills = staff.view_all_bills()
            print("\nAll Bills:")
            for b in bills:
                print(f"Bill ID: {b['bill_id']}, Appointment ID: {b['appointment_id']}, "
                      f"Patient ID: {b['patient_id']}, Patient Name: {b['patient_name']}, "
                      f"Appointment Date: {b['appointment_date']}, Total: {b['total_cost']}, Status: {b['payment_status']}")

        elif choice == "8":
            bills = staff.view_paid_bills()
            print("\nPaid Bills:")
            for b in bills:
                print(f"Bill ID: {b['bill_id']}, Appointment ID: {b['appointment_id']}, "
                      f"Patient ID: {b['patient_id']}, Patient Name: {b['patient_name']}, "
                      f"Appointment Date: {b['appointment_date']}, Total: {b['total_cost']}, Status: {b['payment_status']}")

        elif choice == "9":
            total_paid = staff.total_paid_amount()
            print(f"\nTotal Paid Amount: {total_paid}")

        elif choice == "10":
            break

        elif choice == "11":  # إضافة مواعيد جديدة
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            date = input("Enter appointment date (e.g., 2025-12-30): ")
            notes = input("Enter notes (optional): ")
            staff.add_appointment(patient_id, doctor_id, date, notes)

        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
