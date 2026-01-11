# Hospital Management System

## Project Overview
The **Hospital Management System** is a Python-based application designed to manage basic hospital operations using **Object-Oriented Programming (OOP)**, a **SQLite database**, and a **Graphical User Interface (GUI)** built with **Tkinter**.

The system supports multiple user roles (**Patient**, **Doctor**, and **Staff**) and allows appointment booking, billing management, and patient records handling in an organized and interactive way.

---

## Group Members
- Maya Maged — 120230241  
- Karen Labib — 120230259  
- Mairoun Michel — 120230136  
- Kirolos Khairy — 120230237  

---

## Technologies Used
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Database:** SQLite3  
- **Paradigm:** Object-Oriented Programming (OOP)  

---

##  Project Structure
Doctor.py
patient.py
staff.py
appointment.py
bill.py
database.py
main.py
GUI_main.py
GUI_tools.py
Signup_window.py
Login_window.py
Doctor_window.py
Patient_window.py
Staff_window.py

---

## Object-Oriented Design

### Main Classes
- Patient  
- Doctor  
- Staff  
- Appointment  
- Bill  

### Patient Attributes
- ID  
- Name  
- Age  
- Gender  
- Username  
- Password  
- Problem  
- Assigned Doctor  

### Doctor Attributes
- ID  
- Name  
- Age  
- Specialty  

### Staff Attributes
- ID  
- Name  
- Age  
- Gender  

### Appointment Attributes
- Patient ID  
- Doctor ID  
- Date  
- Notes  
- Payment Status  

### Bill Attributes
- Patient ID  
- Appointment ID  
- Total Cost  
- Payment Status  

---

## System Methods

### Patient Functions
- `signup()`  
- `login()`  
- `view_doctors()`  
- `book_appointment()`  
- `view_appointments()`  
- `pay_bill()`  

### Doctor Functions
- `view_assigned_patients()`  
- `view_appointments()`  
- `profile()`  

### Staff Functions
- `add_patient()`  
- `update_patient()`  
- `delete_patient()`  
- `register_patient_offline()`  
- `view_all_bills()`  

### Appointment Functions
- `add_patient_appointment()`  
- `get_patient_appointments()`  

### Bill Functions
- `view_all_bills()`  
- `view_paid_bills()`  
- `total_paid_amount()`  
- `mark_bill_as_paid()`  

---

## OOP Concepts Applied
- **Encapsulation:** Each class manages its own data and behavior  
- **Abstraction:** Only essential methods are exposed  
- **Inheritance:** Designed for future extension (User → Patient/Doctor/Staff)  
- **Polymorphism:** Similar methods behave differently across classes  

---

## Application Features

### Patient Features
- Sign up & login  
- View doctors  
- Book appointments  
- View, edit, and delete appointments  
- View and pay bills  

### Doctor Features
- View assigned patients  
- View appointments  
- View profile  

### Staff Features
- Add, update, and delete patients  
- View patients and doctors  
- Add appointments (offline registration)  
- View all bills  
- View paid bills  
- View total paid amount  

---

##  Database Structure

### Patients Table
(id, name, age, gender, problem, assigned_doctor)

### Doctors Table
(id, name, specialty)

### Appointments Table
(id, patient_id, doctor_id, date, notes, payment_status)

### Bills Table
(patient_id, appointment_id, total_cost, payment_status)

## implementation 
### how to run 
1. Install **Python 3**.
2. Open the project folder.
3. Run the following command:
```bash
python GUI_main.py
```
### screenshot
1)Program Execution and User Interaction

## implementation 
### how to run 
1. Install **Python 3**.
2. Open the project folder.
3. Run the following command:
```bash
python GUI_main.py
```
### screenshot
1. [Program Execution and User Interaction](https://github.com/user-attachments/assets/9f056f99-6165-4e09-806e-41569d81b570)
2. [Patient Menu – Viewing Doctors and Booking an Appointment ](https://github.com/user-attachments/assets/dba2c685-162f-48f9-993c-1120f7256492)
3. [Patient Appointment and Billing Execution](https://github.com/user-attachments/assets/218213dc-69f5-47b7-87fe-7e13514c6ddc)
4. [Doctor Login and Patient Management Execution](https://github.com/user-attachments/assets/92416a7a-705c-4865-9425-55a37ff20bcb)
5. [Staff login()and view_appointments()](https://github.com/user-attachments/assets/66052bd7-d485-40af-8abd-1ae72548ebf6)
6. [view_all_bills() and view_patients()](https://github.com/user-attachments/assets/1bf1d5c8-d9ca-4fb0-b9cc-036af495cc9f)

## Runtime Flow

1. When the program starts, the main execution window is created using Tkinter.

2. A full-screen main window titled **"Hospital System"** appears.
   This window acts as the entry point of the application.

3. The main window displays two buttons:
   - **LOG IN Page**
   - **SIGN UP Page**

4. If the user clicks **LOG IN Page**:
   - The main window is closed.
   - The system redirects the user to the login interface by calling the `open_login()` function.

5. If the user clicks **SIGN UP Page**:
   - The main window is closed.
   - The system redirects the user to the signup interface by calling the `open_signup()` function.

6. Each button triggers a specific function (`login()` or `signup()`),
   ensuring clear navigation between system pages.

7. This design allows the application to follow a structured and user-friendly flow,
   where the user selects an action before accessing system functionalities.

8. After selecting **Log In** or **Sign Up**, the system redirects the user to the authentication interface.
Once authentication is completed successfully, the user is redirected based on their role.

---

### Patient Runtime Flow

1. After logging in or signing up as a **Patient**, the patient main menu window is displayed.

2. The patient menu provides the following options:
   - View available doctors
   - Book an appointment
   - View my appointments
   - Edit or delete appointments
   - View bills
   - Pay bills
   - Log out

3. When the patient selects an option:
   - Viewing doctors retrieves doctor data from the database.
   - Booking an appointment allows the patient to select a doctor and date.
   - Viewing appointments displays all appointments related to the patient.
   - Viewing bills shows all unpaid and paid bills.
   - Paying a bill updates the payment status in the database.

4. Each action is handled by the corresponding patient-related function
   (such as `view_doctors()`, `book_appointment()`, and `pay_bill()`).
   <img width="1024" height="1536" alt="patient flow" src="https://github.com/user-attachments/assets/2b45e0b7-83a9-42ff-9886-aea92677f82e" />
   


---

###  Doctor Runtime Flow

5. After logging in as a **Doctor**, the doctor dashboard window appears.

6. The doctor menu includes the following options:
   - View assigned patients
   - View appointments
   - View personal profile
   - Log out

7. When a doctor selects an option:
   - Viewing assigned patients displays patients linked to the doctor.
   - Viewing appointments shows the doctor’s scheduled appointments.
   - Viewing the profile displays doctor information stored in the system.

8. These actions are managed through doctor-specific functions
   (such as `view_assigned_patients()` and `view_appointments()`).
<img width="1024" height="1536" alt="Doctor flow" src="https://github.com/user-attachments/assets/a25f3c32-0fa0-4751-8918-1ef581c6dada" />

---

###  Staff Runtime Flow

9. After logging in as **Staff**, the administrative control panel is displayed.

10. The staff menu provides administrative options including:
    - Add a new patient
    - Update patient information
    - Delete a patient
    - Register appointments offline
    - View all bills
    - View paid bills
    - View total paid amount
    - Log out

11. Each selected option performs a database operation such as inserting,
    updating, or deleting records.

12. Staff actions are handled using staff-related functions
    (such as `add_patient()`, `update_patient()`, and `view_all_bills()`).
<img width="1024" height="1536" alt="staff flow" src="https://github.com/user-attachments/assets/07912e23-91e6-4459-9130-a26a1d9dcc78" />

---

### Database Interaction:

13. All user actions across Patient, Doctor, and Staff roles are connected to
    the database layer (`Database.py`).

14. The database ensures data persistence and consistency using SQLite,
    allowing the system to store and retrieve information efficiently.
 ### screenshots GUI
 ![GUI 1](https://github.com/user-attachments/assets/14e6208e-372c-477b-9663-6215084e0d36)
![GUI2](https://github.com/user-attachments/assets/73866364-5d65-4a17-a88b-32b7f985df84)
![GUI3](https://github.com/user-attachments/assets/887938e3-00f1-4d14-9b89-d15d2ee9beca)


### documentationdile 
[hospital system docuemntation.pdf](https://github.com/user-attachments/files/24394381/hospital.system.docuemntation.pdf)





















