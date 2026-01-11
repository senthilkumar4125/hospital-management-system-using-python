from tkinter import *
from tkinter import ttk
from GUI_Tools import create_scrollable_tab
from doctor import Doctor 

bg_color = "#D3D3D3"
fg_color = "#0026FF"

def signout():
    doctor_window.destroy()
    from Login_Window import open_login
    open_login()

def profile_f(current_doctor):
    # Main container
    profile_frame = Frame(doctor_window, bg=bg_color)
    profile_frame.pack(pady=20, padx=20, fill="x")

    # Styling Configuration
    val_color = "#0026FF"
    label_color = "#000000"
    label_font = ("times new roman", 30, "bold")
    value_font = ("times new roman", 25)
    

    profile_frame.columnconfigure((0, 1, 2, 3), weight=1)

    # Name and ID
    Label(profile_frame, text="DOCTOR NAME:", bg=bg_color, fg=label_color, font=label_font).grid(row=0, column=0, sticky="e", padx=5, pady=10)
    Label(profile_frame, text=f"Dr. {current_doctor.name}", bg=bg_color, fg=val_color, font=value_font).grid(row=0, column=1, sticky="w",padx=5, pady=10)

    Label(profile_frame, text="ID:", bg=bg_color, fg=label_color, font=label_font).grid(row=0, column=2, sticky="e", padx=5, pady=10)
    Label(profile_frame, text=f"# {current_doctor.id}", bg=bg_color, fg=val_color, font=value_font).grid(row=0, column=3, sticky="w", padx=5, pady=10)

#     # Age and Specialty
#     Label(profile_frame, text="AGE:", bg=bg_color, fg=label_color, font=label_font).grid(row=1, column=0, sticky="e", padx=5, pady=10)
#     Label(profile_frame, text=f"{current_doctor.age} Years", bg=bg_color, fg=val_color, font=value_font).grid(row=1, column=1, sticky="w", padx=5, pady=10)

    Label(profile_frame, text="SPECIALTY:", bg=bg_color, fg=label_color, font=label_font).grid(row=1, column=0,columnspan=2, sticky="e", padx=5, pady=10)
    Label(profile_frame, text=current_doctor.specialty, bg=bg_color, fg=val_color, font=value_font).grid(row=1, column=2, columnspan=2, sticky="w", padx=5, pady=10)

    Button(profile_frame, text="Sign OUT", bg="#555555", fg="white", width=10,
           font=("times new roman", 20, 'bold'), cursor="hand2", command=signout).grid(row=0, column=4, rowspan= 2, padx=5, pady=10)


def patient_list_f(current_doctor):
    #  Container Frame
    table_container = Frame(patient_list_tab, bg=bg_color)
    table_container.grid(row=0, column=0, pady=20)

    # Table Title
    Label(table_container, 
          text="Assigned Patient List", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 35, 'bold', 'underline')).grid(row=0, column=0, columnspan=5, pady=(0, 30))

    # Table Headers
    headers = ["ID", "Patient Name", "Age", "Gender", "Problem"]
    for col_index, header_text in enumerate(headers):
        header_cell = Label(table_container, 
                             text=header_text, 
                             bg='#d3d3d3', 
                             fg='black', 
                             font=("times new roman", 18, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=15)
        header_cell.grid(row=1, column=col_index, sticky="nsew")

    # 5. Fetch and Display Patients
    patients = current_doctor.view_assigned_patients()
    
    for i, p in enumerate(patients):
        # We start at row i+2 to leave space for Title (0) and Headers (1)
        
        # ID Cell
        Label(table_container, text=p[0], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=0, sticky="nsew")
        
        # Name Cell
        Label(table_container, text=p[1], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10).grid(row=i+2, column=1, sticky="nsew")
        
        # Age Cell
        Label(table_container, text=p[2], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=2, sticky="nsew")
              
        # Gender Cell
        Label(table_container, text=p[3], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=3, sticky="nsew")
              
        # Problem Cell
        Label(table_container, text=p[4], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10, wraplength=250).grid(row=i+2, column=4, sticky="nsew")


def view_f(current_doctor):
    global view_appointment_frame
        
    # Main container frame
    view_appointment_frame = Frame(view_appointment_tab, bg=bg_color)
    view_appointment_frame.grid(row=0, column=0, pady=20)

    # Table Title
    Label(view_appointment_frame, 
          text="Appointment List", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 35, 'bold', 'underline')).grid(row=0, column=0, columnspan=5, pady=(0, 30))

    # Table Headers
    headers = ["Appt ID", "Patient ID", "Date", "Notes", "Status"]
    for col_index, header_text in enumerate(headers):
        header_cell = Label(view_appointment_frame, 
                             text=header_text, 
                             bg='#d3d3d3', 
                             fg='black', 
                             font=("times new roman", 18, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=15)
        header_cell.grid(row=1, column=col_index, sticky="nsew")

    # Fetch and Display Appointments
    appointments = current_doctor.view_appointments()
    
    for i, a in enumerate(appointments):
        
        # Appointment ID
        Label(view_appointment_frame, text=a[0], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=0, sticky="nsew")
        
        # Patient ID
        Label(view_appointment_frame, text=a[1], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=1, sticky="nsew")
        
        # Date
        Label(view_appointment_frame, text=a[3], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=2, sticky="nsew")
              
        # Notes (with padding and wrapping for longer text)
        Label(view_appointment_frame, text=a[4], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10, wraplength=200).grid(row=i+2, column=3, sticky="nsew")
              
        # Status
        Label(view_appointment_frame, text=a[5], bg="white", fg='red', 
              font=("times new roman", 16, 'bold'), relief="solid", borderwidth=1).grid(row=i+2, column=4, sticky="nsew")

def open_doctor(doctor_id):
    global doctor_window
    global patient_list_tab
    global view_appointment_tab
    current_doctor = Doctor.login(doctor_id)
    doctor_window = Tk()
    doctor_window.title("Doctor Page")
    screen_width = doctor_window.winfo_screenwidth()
    screen_height = doctor_window.winfo_screenheight()
    doctor_window.geometry(f"{screen_width}x{screen_height}+0+0")
    doctor_window.state("zoomed")
    doctor_window.configure(bg= bg_color)

    profile_f(current_doctor)

    doctor_tabs = ttk.Notebook(doctor_window) 
    doctor_tabs.pack(expand=True,fill="both")  

    patient_list_tab = create_scrollable_tab(doctor_tabs,"Assigned Patients List")
    view_appointment_tab = create_scrollable_tab(doctor_tabs,"Appointments")


    patient_list_f(current_doctor)
    view_f(current_doctor)

    doctor_window.mainloop()


