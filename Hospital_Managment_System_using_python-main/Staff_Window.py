from tkinter import *
from tkinter import ttk
from GUI_Tools import create_scrollable_tab
from tkinter import messagebox
from staff import Staff 

bg_color = "#D3D3D3"
fg_color = "#0026FF"

def signout():
    staff_window.destroy()
    from Login_Window import open_login
    open_login()

def update(current_staff,patient_id_entry, new_name_entry, new_age_entry,new_gender_entry,new_problem_entry):
    pid = int(patient_id_entry.get())
    name = new_name_entry.get()
    age = int(new_age_entry.get())
    gender = new_gender_entry.get()
    problem = new_problem_entry.get()
    current_staff.update_patient(pid, name, age, gender, problem)
    messagebox.showinfo(title="update_patient Apointment Success",
                        message=f"✔ Patient {pid} updated"
                        )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)

def delete(current_staff,patient_idd_entry):
    pid = int(patient_idd_entry.get())
    current_staff.delete_patient(pid)
    print("✔ Appointment Deleted!")
    messagebox.showinfo(title="Delete Patient Success",
                        message=f"✔ Patient {pid} and related appointments deleted"
                        )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)


def book(current_staff, patient_id_entry ,doc_id_entry, day_listbox , hour_entry, min_entry, note_entry):
    patient_id = patient_id_entry.get()
    doc_id = doc_id_entry.get()
    selected_day = day_listbox.curselection()
    day = day_listbox.get(selected_day[0])
    hour = hour_entry.get()
    min = min_entry.get()
    notes = note_entry.get() 
    appointment_id = current_staff.add_appointment(patient_id,doc_id, day, hour, min, notes)
    if appointment_id == None:
        messagebox.showerror(title="Book Apointment Failed",
                             message="❌ Invalid Data"
                             )
    else:
        print(f"✔ Appointment booked with ID: {appointment_id}")
        messagebox.showinfo(title="Book Apointment Success",
                            message=f"✔ Appointment booked with ID: {appointment_id}"
                            )
    patient_list_frame.destroy()
    bill_frame.destroy()
    paid_bill_frame.destroy()
    total_paid_frame.destroy()
    patient_list_f(current_staff)
    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)




def view(current_staff,patient_iddd_entry):
     appointment_list_frame.destroy()
     appointment_list_f(current_staff,int(patient_iddd_entry.get()))





def profile_f(current_staff):
    # Main container frame
    profile_frame = Frame(staff_window, bg=bg_color)
    profile_frame.pack(pady=25, padx=20, fill="x")

    val_color = "#0026FF" 
    label_color = "#000000"
    label_font = ("times new roman", 30, "bold")
    value_font = ("times new roman", 25)

    profile_frame.columnconfigure((0, 1, 2, 3), weight=1)

    # Staff Name
    Label(profile_frame, text="STAFF NAME:", bg=bg_color, fg=label_color, font=label_font).grid(row=0, column=0, sticky="e", padx=10, pady=15)
    Label(profile_frame, text=current_staff.name, bg=bg_color, fg=val_color, font=value_font).grid(row=0, column=1, sticky="w", padx=10, pady=15)

    # Staff ID
    Label(profile_frame, text="EMPLOYEE ID:", bg=bg_color, fg=label_color, font=label_font).grid(row=0, column=2, sticky="e", padx=10, pady=15)
    Label(profile_frame, text=f"#{current_staff.id}", bg=bg_color, fg=val_color, font=value_font).grid(row=0, column=3, sticky="w", padx=10, pady=15)

    # Role
    Label(profile_frame, text="ROLE:", bg=bg_color, fg=label_color, font=label_font).grid(row=1, column=0, sticky="e", padx=10, pady=15)
    Label(profile_frame, text=current_staff.role.upper(), bg=bg_color, fg=val_color, font=value_font).grid(row=1, column=1, sticky="w", padx=10, pady=15)

    # Gender
    Label(profile_frame, text="GENDER:", bg=bg_color, fg=label_color, font=label_font).grid(row=1, column=2, sticky="e", padx=10, pady=15)
    Label(profile_frame, text=current_staff.gender, bg=bg_color, fg=val_color, font=value_font).grid(row=1, column=3, sticky="w", padx=10, pady=15)


    Button(profile_frame, text="Sign OUT", bg="#555555", fg="white", width=10,
           font=("times new roman", 20, 'bold'), cursor="hand2", command=signout).grid(row=0, column=4, rowspan= 2, padx=5, pady=10)


def patient_list_f(current_staff):
    global patient_list_frame
    patient_tab.columnconfigure(0, weight=1)

    # Container Frame
    patient_list_frame = Frame(patient_tab, bg=bg_color)
    patient_list_frame.grid(row=0, column=0, pady=20)

    # Table Title
    Label(patient_list_frame, text="Patient List", bg=bg_color, fg='black', 
          font=("times new roman", 35, 'bold', 'underline')).grid(row=0, column=0, columnspan=5, pady=(0, 30))

    # Table Headers
    headers = ["ID", "Name", "Age", "Gender", "Problem"]
    for col, text in enumerate(headers):
        header_cell = Label(patient_list_frame, text=text, bg='#d3d3d3', font=("times new roman", 18, 'bold'),
                             relief="solid", borderwidth=1, width=15)
        header_cell.grid(row=1, column=col, sticky="nsew")

    # Fetch and Display Data
    patients = current_staff.view_patients()
    for i, p in enumerate(patients):

        data_to_display = [p[0], p[1], p[2], p[3], p[6]]
        
        for col, value in enumerate(data_to_display):
            Label(patient_list_frame, text=value, bg="white", fg='red', 
                  font=("times new roman", 16), relief="solid", borderwidth=1, 
                  padx=10, wraplength=200 if col == 4 else None).grid(row=i+2, column=col, sticky="nsew")


def update_patient_f(current_staff):
    # Section Title
    Label(patient_tab, text="Update Patient Information", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=1, column=0, pady=(40, 10))

    # Update LabelFrame
    update_patient_frame = LabelFrame(patient_tab, text=" Edit Patient Details ", 
                                      bg=bg_color, font=("times new roman", 15, 'italic'),
                                      relief="solid", borderwidth=1, padx=30, pady=20)
    update_patient_frame.grid(row=2, column=0, padx=20, pady=10)
    
    # Input Fields
    labels = ["Patient ID", "New Name", "New Age", "New Gender", "New Problem"]
    entries = []

    for i, label_text in enumerate(labels):
        Label(update_patient_frame, text=label_text, bg=bg_color, fg=fg_color, 
              font=("times new roman", 22, 'bold')).grid(row=i, column=0, sticky="w", pady=10)
        
        entry = Entry(update_patient_frame, font=("times new roman", 22), width=30)
        entry.grid(row=i, column=1, pady=10, padx=10)
        entries.append(entry)

    # Extracting entries for the command
    p_id, p_name, p_age, p_gender, p_prob = entries

    # Update Button
    update_button = Button(update_patient_frame, text="Update Patient", bg=fg_color, fg="#FFFFFF",
                           font=("times new roman", 22, 'bold'), cursor="hand2",
                           command=lambda: update(current_staff, p_id, p_name, p_age, p_gender, p_prob))
    update_button.grid(row=5, column=0, columnspan=2, pady=20)


def delete_f(current_staff):
    # Section Title
    Label(patient_tab, text="Delete Patient", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=3, column=0, pady=(40, 10))

    # Delete LabelFrame
    delete_frame = LabelFrame(patient_tab, text=" Danger Zone ", 
                              bg=bg_color, fg="red", font=("times new roman", 15, 'italic'),
                              relief="solid", borderwidth=1, padx=30, pady=20)
    delete_frame.grid(row=4, column=0, padx=20, pady=20)

    # Patient ID Input
    Label(delete_frame, text="Patient ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    
    patient_idd_entry = Entry(delete_frame, font=("times new roman", 22), width=30)
    patient_idd_entry.grid(row=0, column=1, pady=10, padx=10)

    # Delete Button
    delete_button = Button(delete_frame, text="Delete Patient Record", bg="#cc0000", fg="#FFFFFF",
                           font=("times new roman", 22, 'bold'), cursor="hand2",
                           command=lambda: delete(current_staff, patient_idd_entry))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)




def doctor_list_f(current_staff):
    # Main Container Frame
    doctor_list_frame = Frame(doctor_tab, bg=bg_color)
    doctor_list_frame.grid(row=0, column=0, pady=20)

    # Table Title
    Label(doctor_list_frame, 
          text="Doctor List", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 35, 'bold', 'underline')).grid(row=0, column=0, columnspan=3, pady=(0, 30))

    # Table Headers
    headers = ["Doctor ID", "Doctor Name", "Specialty"]
    for col_index, header_text in enumerate(headers):
        header_cell = Label(doctor_list_frame, 
                             text=header_text, 
                             bg='#d3d3d3', 
                             fg='black', 
                             font=("times new roman", 18, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=20)
        header_cell.grid(row=1, column=col_index, sticky="nsew")

    # Fetch and Display Doctors
    doctors = current_staff.view_doctors()
    
    for i, d in enumerate(doctors):
        
        # ID Cell
        Label(doctor_list_frame, text=d[0], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=0, sticky="nsew")
        
        # Name Cell
        Label(doctor_list_frame, text=d[1], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10).grid(row=i+2, column=1, sticky="nsew")
        
        # Specialty Cell
        Label(doctor_list_frame, text=d[2], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10).grid(row=i+2, column=2, sticky="nsew")



def book_f(current_staff):

    # Main Title
    title_label = Label(doctor_tab, 
                        text="Book An Appointment", 
                        bg=bg_color, fg='black', 
                        font=("times new roman", 35, 'bold', 'underline'))
    title_label.grid(row=1, column=0, pady=(40, 10))

    # LabelFrame
    book_frame = LabelFrame(doctor_tab,
                            text=" Appointment Details ", 
                            bg=bg_color,
                            font=("times new roman", 15, 'italic'),
                            padx=30, pady=30,
                            relief="solid", borderwidth=1)
    book_frame.grid(row=2, column=0, padx=20, pady=20)

    Label(book_frame, text="Patient ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    patient_id_entry = Entry(book_frame, font=("times new roman", 22), width=45)
    patient_id_entry.grid(row=0, column=1, columnspan=3, pady=10, padx=10)

    Label(book_frame, text="Doctor ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=1, column=0, sticky="w", pady=10)
    doc_id_entry = Entry(book_frame, font=("times new roman", 22), width=45)
    doc_id_entry.grid(row=1, column=1, columnspan=3, pady=10, padx=10)

    # Day Listbox
    Label(book_frame, text="Day", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=2, column=0, sticky="nw", pady=10)
    
    day_frame = Frame(book_frame, bg=bg_color)
    day_frame.grid(row=2, column=1, columnspan=3, pady=10, padx=10, sticky="w")
    
    day_scrollbar = Scrollbar(day_frame, orient=VERTICAL)
    # Changed height to 4 so it doesn't take over the whole screen
    day_listbox = Listbox(day_frame, font=("times new roman", 20), 
                          height=2, width=45, selectmode=SINGLE, 
                          yscrollcommand=day_scrollbar.set)
    day_scrollbar.config(command=day_listbox.yview)
    
    day_listbox.pack(side=LEFT)
    day_scrollbar.pack(side=RIGHT, fill=Y)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        day_listbox.insert(END, day)

    # Time (Hour : Min)
    Label(book_frame, text="Time", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=3, column=0, sticky="w", pady=10)
    
    # Using a sub-frame for time to keep ":" centered between entries
    time_container = Frame(book_frame, bg=bg_color)
    time_container.grid(row=3, column=1, columnspan=3, sticky="w")
    
    hour_entry = Entry(time_container, font=("times new roman", 22), width=15)
    hour_entry.pack(side=LEFT, padx=(10, 5))

    Label(time_container, text=":", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).pack(side=LEFT)

    min_entry = Entry(time_container, font=("times new roman", 22), width=15)
    min_entry.pack(side=LEFT, padx=5)
    
    Label(time_container, text="(HH:MM)",fg='red', bg=bg_color, font=("times new roman", 14, 'italic','bold')).pack(side=LEFT, padx=10)

    # Problem
    Label(book_frame, text="Problem", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=4, column=0, sticky="w", pady=10)
    note_entry = Entry(book_frame, font=("times new roman", 22), width=45)
    note_entry.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

    # BUTTON 
    book_button = Button(book_frame,
                         text="Book Appointment",
                         bg=fg_color, fg="#FFFFFF",
                         font=("times new roman", 22, 'bold'),
                         cursor="hand2",
                         command=lambda: book(current_staff, patient_id_entry ,doc_id_entry, day_listbox, hour_entry, min_entry, note_entry)
                         )
    book_button.grid(row=5, column=0, columnspan=4, pady=(30, 10))




def view_f(current_staff):

    # Main Title for the Section
    title_label = Label(appointment_tab, 
                        text="View Appointments", 
                        bg=bg_color, 
                        fg='black', 
                        font=("times new roman", 35, 'bold', 'underline'))
    title_label.grid(row=1, column=0, pady=(40, 10))

    # Create the Framed Container (LabelFrame)
    view_frame = LabelFrame(appointment_tab,
                            text=" Search Patient Records ",
                            bg=bg_color,
                            font=("times new roman", 15, 'italic'),
                            padx=30, pady=30,
                            relief="solid",
                            borderwidth=1)
    view_frame.grid(row=2, column=0, padx=20, pady=20)

    # Input Fields inside the frame
    patient_iddd_label = Label(view_frame,
                               text="Patient ID",
                               bg=bg_color,
                               fg=fg_color,
                               font=("times new roman", 25, 'bold'))
    patient_iddd_label.grid(row=0, column=0, sticky="w", pady=10)

    patient_iddd_entry = Entry(view_frame,
                               font=("times new roman", 25),
                               width=25)
    patient_iddd_entry.grid(row=0, column=1, pady=20, padx=10)

    # Search Button
    view_button = Button(view_frame,
                         text="Search Appointments",
                         bg=fg_color,
                         fg="#FFFFFF",
                         font=("times new roman", 25, 'bold'),
                         cursor="hand2",
                         command=lambda: view(current_staff, patient_iddd_entry))
    view_button.grid(row=1, column=0, columnspan=2, pady=30)


def appointment_list_f(current_staff, pid):
    global appointment_list_frame

    # 2. Main Container Frame
    appointment_list_frame = Frame(appointment_tab, bg=bg_color)
    appointment_list_frame.grid(row=0, column=0, pady=20)

    # 3. Dynamic Title using Patient ID
    Label(appointment_list_frame, 
          text=f"Patient {pid} Appointments", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 35, 'bold', 'underline')).grid(row=0, column=0, columnspan=5, pady=(0, 30))

    # 4. Table Headers
    headers = ["Appointment ID", "Doctor ID", "Date", "Notes", "Status"]
    for col_index, header_text in enumerate(headers):
        header_cell = Label(appointment_list_frame, 
                             text=header_text, 
                             bg='#d3d3d3', 
                             fg='black', 
                             font=("times new roman", 18, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=15)
        header_cell.grid(row=1, column=col_index, sticky="nsew")

    # Fetch and Display Data
    appointments = current_staff.view_appointments(pid)
    
    for i, a in enumerate(appointments):

        
        # Appointment ID
        Label(appointment_list_frame, text=a[0], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=0, sticky="nsew")
        
        # Doctor ID
        Label(appointment_list_frame, text=a[2], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=1, sticky="nsew")
        
        # Date
        Label(appointment_list_frame, text=a[3], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1).grid(row=i+2, column=2, sticky="nsew")
              
        # Notes
        Label(appointment_list_frame, text=a[4], bg="white", fg='red', 
              font=("times new roman", 16), relief="solid", borderwidth=1, padx=10, wraplength=200).grid(row=i+2, column=3, sticky="nsew")
              
        # Status
        Label(appointment_list_frame, text=a[5], bg="white", fg='red', 
              font=("times new roman", 16, 'bold'), relief="solid", borderwidth=1).grid(row=i+2, column=4, sticky="nsew")



def bill_f(current_staff):
    global bill_frame
    bill_tab.columnconfigure(0, weight=1)

    # Container Frame
    bill_frame = Frame(bill_tab, bg=bg_color)
    bill_frame.grid(row=0, column=0, pady=20)

    # Table Title
    Label(bill_frame, text="All Bills", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=0, column=0, columnspan=7, pady=(0, 20))

    # Table Headers
    headers = ["Bill ID", "Appointmentt ID", "Patient ID", "Name", "Date", "Total", "Status"]
    for col, text in enumerate(headers):
        Label(bill_frame, text=text, bg='#d3d3d3', font=("times new roman", 14, 'bold'),
              relief="solid", borderwidth=1, width=12).grid(row=1, column=col, sticky="nsew")

    # Data Rows
    bills = current_staff.view_all_bills()
    for i, b in enumerate(bills):
        row_data = [b['bill_id'], b['appointment_id'], b['patient_id'], b['patient_name'], 
                    b['appointment_date'], f"${b['total_cost']}", b['payment_status']]
        
        for col, value in enumerate(row_data):
            fg_color_data = 'green' if str(value).lower() == 'paid' else 'red'
            Label(bill_frame, text=value, bg="white", fg=fg_color_data if col == 6 else 'black',
                  font=("times new roman", 12), relief="solid", borderwidth=1, padx=5).grid(row=i+2, column=col, sticky="nsew")


def paid_bill_f(current_staff):
    global paid_bill_frame
    paid_bill_frame = Frame(bill_tab, bg=bg_color)
    paid_bill_frame.grid(row=1, column=0, pady=40)

    # Table Title
    Label(paid_bill_frame, text="Paid Bills History", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=0, column=0, columnspan=7, pady=(0, 20))

    # Table Headers
    headers = ["Paid ID", "Appointment ID", "Patient ID", "Name", "Date", "Total", "Status"]
    for col, text in enumerate(headers):
        Label(paid_bill_frame, text=text, bg='#d3d3d3', font=("times new roman", 14, 'bold'),
              relief="solid", borderwidth=1, width=12).grid(row=1, column=col, sticky="nsew")

    # Data Rows
    paid_bills = current_staff.view_paid_bills()
    for i, b in enumerate(paid_bills):
        # Note: mapping 'paid_bill_id' as per your original logic
        row_data = [b['bill_id'], b['appointment_id'], b['patient_id'], b['patient_name'], 
                    b['appointment_date'], f"${b['total_cost']}", b['payment_status']]
        
        for col, value in enumerate(row_data):
            Label(paid_bill_frame, text=value, bg="white", fg='green',
                  font=("times new roman", 12), relief="solid", borderwidth=1, padx=5).grid(row=i+2, column=col, sticky="nsew")




from tkinter import *

def total_paid_f(current_staff):
    global total_paid_frame

    # Create a LabelFrame to act as the "Total" box
    total_paid_frame = LabelFrame(bill_tab, 
                                  text=" Financial Summary ", 
                                  bg=bg_color, 
                                  font=("times new roman", 15, 'italic'),
                                  relief="solid", 
                                  borderwidth=2, 
                                  padx=50, 
                                  pady=20)
    # Placed at row 2, below the two tables
    total_paid_frame.grid(row=2, column=0, pady=40, padx=20)
    
    # Fetch the total amount
    total_paid = current_staff.total_paid_amount()

    # Label for description
    total_paid_label = Label(total_paid_frame,
                             text="Grand Total Paid Amount:",
                             bg=bg_color,
                             fg='Blue',
                             font=("times new roman", 22, 'bold')
                             )
    total_paid_label.grid(row=0, column=0, pady=10, padx=10)

    # Label for the actual numerical value
    # Added a currency symbol and formatting for a professional look
    amount_label = Label(total_paid_frame,
                         text=f"${total_paid:,.2f}",
                         bg=bg_color,
                         fg='black',
                         font=("times new roman", 22, 'bold')
                         )
    amount_label.grid(row=0, column=1, pady=10, padx=10)


def open_staff(username,password):
    global staff_window
    global patient_tab
    global doctor_tab
    global appointment_tab
    global bill_tab
    global appointment_list_frame
    current_staff = Staff.login(username,password)
    staff_window = Tk()
    staff_window.title("Staff Page")
    screen_width = staff_window.winfo_screenwidth()
    screen_height = staff_window.winfo_screenheight()
    staff_window.geometry(f"{screen_width}x{screen_height}+0+0")
    staff_window.state("zoomed")
    staff_window.configure(bg= bg_color)

    profile_f(current_staff)

    staff_tabs = ttk.Notebook(staff_window)
    staff_tabs.pack(expand=True,fill="both")  

    patient_tab = create_scrollable_tab(staff_tabs,"Patients")
    doctor_tab =  create_scrollable_tab(staff_tabs,"Doctors")
    appointment_tab =  create_scrollable_tab(staff_tabs,"Appointments")
    bill_tab =  create_scrollable_tab(staff_tabs,"Bills")

    patient_list_f(current_staff)
    update_patient_f(current_staff)
    delete_f(current_staff)
    doctor_list_f(current_staff)
    book_f(current_staff)
    view_f(current_staff)
    appointment_list_frame = Frame(appointment_tab,
                                   bg=bg_color
                                  )
    appointment_list_frame.grid(row=0,column=1,sticky='w',padx= 20)

    bill_f(current_staff)
    paid_bill_f(current_staff)
    total_paid_f(current_staff)


    staff_window.mainloop()


