from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from GUI_Tools import create_scrollable_tab
from patient import Patient 

bg_color = "#D3D3D3"
fg_color = "#0026FF"

def signout():
    patient_window.destroy()
    from Login_Window import open_login
    open_login()

def book(current_patient, doc_id_entry, day_listbox , hour_entry, min_entry, problem_entry):
    doc_id = doc_id_entry.get()
    selected_day = day_listbox.curselection()
    day = day_listbox.get(selected_day[0])
    hour = hour_entry.get()
    min = min_entry.get()
    problem = problem_entry.get() 
    appointment_id = current_patient.book_appointment(doc_id, day, hour, min, problem)
    if appointment_id == None:
        messagebox.showerror(title="Book Apointment Failed",
                             message="❌ Invalid Data"
                             )
    else:
        print(f"✔ Appointment booked with ID: {appointment_id}")
        messagebox.showinfo(title="Book Apointment Success",
                            message=f"✔ Appointment booked with ID: {appointment_id}"
                            )
        view_appointment_frame.destroy()
        bill_frame.destroy()
        view_f(current_patient)
        bill_f(current_patient)


def edit(current_patient, app_id_entry, day_listbox, hour_entry,min_entry, new_notes_entry):
    app_id = app_id_entry.get()
    selected_day = day_listbox.curselection()
    day = day_listbox.get(selected_day[0])
    hour = hour_entry.get()
    min = min_entry.get()
    new_notes = new_notes_entry.get()
    x = current_patient.edit_appointment(app_id, day, hour,min, new_notes)
    if x == None:
        messagebox.showerror(title="Update Apointment Failed",
                             message="❌ Invalid Data"
                             )
    else:
        print("✔ Appointment updated!")
        messagebox.showinfo(title="Edit Apointment Success",
                            message="✔ Appointment updated!"
                            )
        view_appointment_frame.destroy()
        bill_frame.destroy()
        view_f(current_patient)
        bill_f(current_patient)
    


def delete(current_patient,app_idd_entry):
    app_idd = int(app_idd_entry.get())
    current_patient.delete_appointment(app_idd)
    print("✔ Appointment Deleted!")
    messagebox.showinfo(title="Delete Apointment Success",
                        message="✔ Appointment Deleted!"
                        )
    view_appointment_frame.destroy()
    bill_frame.destroy()
    view_f(current_patient)
    bill_f(current_patient)
    
def pay(current_patient,app_iddd_entry):
    app_iddd = int(app_iddd_entry.get())
    result = current_patient.pay_bill(app_iddd)
    print(result)
    messagebox.showinfo(title="Pay A Bill Success",
                        message=result
                        )
    bill_frame.destroy()
    bill_f(current_patient)


def profile_f(current_patient):
    # Main container 
    profile_frame = Frame(patient_window, bg=bg_color)
    profile_frame.pack(pady=20, padx=20, fill="x")


    data_color = "#0026FF" 
    label_color = "#000000"
    label_font = ("times new roman", 30, "bold")
    value_font = ("times new roman", 25)
    
    # Configure columns to distribute space evenly
    profile_frame.columnconfigure((0, 1, 2, 3), weight=1)

    # Name Label + Value
    name_label = Label(profile_frame, text="NAME:", bg=bg_color, fg=label_color, font=label_font)
    name_label.grid(row=0, column=0, sticky="e", padx=5, pady=10)
    
    name_val = Label(profile_frame, text=current_patient.name.upper(), bg=bg_color, fg=data_color, font=value_font)
    name_val.grid(row=0, column=1, sticky="w", padx=5, pady=10)

    # ID Label + Value
    id_label = Label(profile_frame, text="ID:", bg=bg_color, fg=label_color, font=label_font)
    id_label.grid(row=0, column=2, sticky="e", padx=5, pady=10)
    
    id_val = Label(profile_frame, text=f"#{current_patient.id}", bg=bg_color, fg=data_color, font=value_font)
    id_val.grid(row=0, column=3, sticky="w", padx=5, pady=10)

    # Age Label + Value
    age_label = Label(profile_frame, text="AGE:", bg=bg_color, fg=label_color, font=label_font)
    age_label.grid(row=1, column=0, sticky="e", padx=5, pady=10)
    
    age_val = Label(profile_frame, text=f"{current_patient.age} Years", bg=bg_color, fg=data_color, font=value_font)
    age_val.grid(row=1, column=1, sticky="w", padx=5, pady=10)

    # Gender Label + Value
    gender_label = Label(profile_frame, text="GENDER:", bg=bg_color, fg=label_color, font=label_font)
    gender_label.grid(row=1, column=2, sticky="e", padx=5, pady=10)
    
    gender_val = Label(profile_frame, text=current_patient.gender, bg=bg_color, fg=data_color, font=value_font)
    gender_val.grid(row=1, column=3, sticky="w", padx=5, pady=10)

    Button(profile_frame, text="Sign OUT", bg="#555555", fg="white", width=10,
           font=("times new roman", 20, 'bold'), cursor="hand2", command=signout).grid(row=0, column=4, rowspan= 2, padx=5, pady=10)

def doctor_list_f(current_patient):

    doctor_list_frame = Frame(doctor_list_tab, bg=bg_color)
    doctor_list_frame.grid(row=0, column=0)

    # ADD THE TITLE 
    title_label = Label(doctor_list_frame, 
                        text="Doctor List", 
                        bg=bg_color, 
                        fg='black', 
                        font=("times new roman", 35, 'bold', 'underline'))

    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))

    # TABLE HEADERS
    headers = ["ID", "Doctor Name", "Specialty"]
    for col_index, header_text in enumerate(headers):
        header_cell = Label(doctor_list_frame, 
                             text=header_text, 
                             bg='#d3d3d3', 
                             fg='black', 
                             font=("times new roman", 20, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=15)
        header_cell.grid(row=1, column=col_index, sticky="nsew")

    # TABLE DATA
    doctors = current_patient.view_doctors()
    
    for i, d in enumerate(doctors):
        Label(doctor_list_frame, text=d[0], bg="white", fg='red', 
              font=("times new roman", 18), relief="solid", borderwidth=1, width=10).grid(row=i+2, column=0, sticky="nsew")
        
        Label(doctor_list_frame, text=d[1], bg="white", fg='red', 
              font=("times new roman", 18), relief="solid", borderwidth=1, width=20).grid(row=i+2, column=1, sticky="nsew")
        
        Label(doctor_list_frame, text=d[2], bg="white", fg='red', 
              font=("times new roman", 18), relief="solid", borderwidth=1, width=20).grid(row=i+2, column=2, sticky="nsew")


def book_f(current_patient):

    # Main Title
    title_label = Label(doctor_list_tab, 
                        text="Book An Appointment", 
                        bg=bg_color, fg='black', 
                        font=("times new roman", 35, 'bold', 'underline'))
    title_label.grid(row=1, column=0, pady=(40, 10))

    # LabelFrame
    book_frame = LabelFrame(doctor_list_tab,
                            text=" Appointment Details ", 
                            bg=bg_color,
                            font=("times new roman", 15, 'italic'),
                            padx=30, pady=30,
                            relief="solid", borderwidth=1)
    book_frame.grid(row=2, column=0, padx=20, pady=20)

    # INPUT FIELDS 
    
    # Doctor ID
    Label(book_frame, text="Doctor ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    doc_id_entry = Entry(book_frame, font=("times new roman", 22), width=45)
    doc_id_entry.grid(row=0, column=1, columnspan=3, pady=10, padx=10)

    # Day Listbox
    Label(book_frame, text="Day", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=1, column=0, sticky="nw", pady=10)
    
    day_frame = Frame(book_frame, bg=bg_color)
    day_frame.grid(row=1, column=1, columnspan=3, pady=10, padx=10, sticky="w")
    
    day_scrollbar = Scrollbar(day_frame, orient=VERTICAL)
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
          font=("times new roman", 22, 'bold')).grid(row=2, column=0, sticky="w", pady=10)
    
 
    time_container = Frame(book_frame, bg=bg_color)
    time_container.grid(row=2, column=1, columnspan=3, sticky="w")
    
    hour_entry = Entry(time_container, font=("times new roman", 22), width=15)
    hour_entry.pack(side=LEFT, padx=(10, 5))

    Label(time_container, text=":", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).pack(side=LEFT)

    min_entry = Entry(time_container, font=("times new roman", 22), width=15)
    min_entry.pack(side=LEFT, padx=5)
    
    Label(time_container, text="(HH:MM)",fg='red', bg=bg_color, font=("times new roman", 14, 'italic','bold')).pack(side=LEFT, padx=10)

    # Problem
    Label(book_frame, text="Problem", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=3, column=0, sticky="w", pady=10)
    problem_entry = Entry(book_frame, font=("times new roman", 22), width=45)
    problem_entry.grid(row=3, column=1, columnspan=3, pady=10, padx=10)

    # BUTTON 
    book_button = Button(book_frame,
                         text="Book Appointment",
                         bg=fg_color, fg="#FFFFFF",
                         font=("times new roman", 22, 'bold'),
                         cursor="hand2",
                         command=lambda: book(current_patient, doc_id_entry, day_listbox, hour_entry, min_entry, problem_entry)
                         )
    book_button.grid(row=4, column=0, columnspan=4, pady=(30, 10))



def view_f(current_patient):
    global view_appointment_frame
    # Container Frame
    view_appointment_frame = Frame(view_appointment_tab, bg=bg_color)
    view_appointment_frame.grid(row=0, column=0, pady=20)

    # Table Title
    Label(view_appointment_frame, 
          text="Your Appointments", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=0, column=0, columnspan=5, pady=(0, 20))

    # Table Headers
    headers = ["Appointment ID", "Doctor ID", "Date", "Notes", "Status"]
    for col, text in enumerate(headers):
        header_label = Label(view_appointment_frame, 
                             text=text, 
                             bg='#E0E0E0', 
                             font=("times new roman", 16, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=15)
        header_label.grid(row=1, column=col, sticky="nsew")

    # Table Data Rows
    appointments = current_patient.view_appointments()
    
    for row_idx, a in enumerate(appointments):
        status_color = "green" if str(a[5]).lower() == "scheduled" else "red"
        
        # ID: a[0]
        Label(view_appointment_frame, text=a[0], bg="white", font=("times new roman", 14),
              relief="solid", borderwidth=1).grid(row=row_idx+2, column=0, sticky="nsew")
        
        # Doctor ID: a[2]
        Label(view_appointment_frame, text=a[2], bg="white", font=("times new roman", 14),
              relief="solid", borderwidth=1).grid(row=row_idx+2, column=1, sticky="nsew")
        
        # Date: a[3]
        Label(view_appointment_frame, text=a[3], bg="white", font=("times new roman", 14),
              relief="solid", borderwidth=1).grid(row=row_idx+2, column=2, sticky="nsew")
        
        # Notes/Problem: a[4]
        Label(view_appointment_frame, text=a[4], bg="white", font=("times new roman", 14),
              relief="solid", borderwidth=1, padx=5).grid(row=row_idx+2, column=3, sticky="nsew")
        
        # Status: a[5]
        Label(view_appointment_frame, text=a[5], bg="white", fg=status_color, font=("times new roman", 14, 'bold'),
              relief="solid", borderwidth=1).grid(row=row_idx+2, column=4, sticky="nsew")



def edit_f(current_patient):

    # Title for Edit Section
    Label(view_appointment_tab, text="Edit An Appointment", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=1, column=0, pady=(40, 10))

    # Edit LabelFrame (The Bordered Box)
    edit_frame = LabelFrame(view_appointment_tab, text=" Update Details ", 
                            bg=bg_color, relief="solid", borderwidth=1, padx=20, pady=20)
    edit_frame.grid(row=2, column=0, padx=20, pady=10)

    # Appointment ID Input
    Label(edit_frame, text="Appointment ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 20, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    app_id_entry = Entry(edit_frame, font=("times new roman", 20), width=45)
    app_id_entry.grid(row=0, column=1,columnspan=3, pady=10, padx=10)

    # Day Listbox
    Label(edit_frame, text="Day", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=1, column=0, sticky="nw", pady=10)
    
    day_frame = Frame(edit_frame, bg=bg_color)
    day_frame.grid(row=1, column=1, columnspan=3, pady=10, padx=10, sticky="w")
    
    day_scrollbar = Scrollbar(day_frame, orient=VERTICAL)
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
    Label(edit_frame, text="Time", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=2, column=0, sticky="w", pady=10)
    
    time_container = Frame(edit_frame, bg=bg_color)
    time_container.grid(row=2, column=1, columnspan=3, sticky="w")
    
    hour_entry = Entry(time_container, font=("times new roman", 22), width=15)
    hour_entry.pack(side=LEFT, padx=(10, 5))

    Label(time_container, text=":", bg=bg_color, fg=fg_color, 
          font=("times new roman", 22, 'bold')).pack(side=LEFT)

    min_entry = Entry(time_container, font=("times new roman", 22), width=15)
    min_entry.pack(side=LEFT, padx=5)
    
    Label(time_container, text="(HH:MM)",fg='red', bg=bg_color, font=("times new roman", 14, 'italic','bold')).pack(side=LEFT, padx=10)



    # New Notes Input
    Label(edit_frame, text="New Notes", bg=bg_color, fg=fg_color, 
          font=("times new roman", 20, 'bold')).grid(row=3, column=0, sticky="w", pady=10)
    new_notes_entry = Entry(edit_frame, font=("times new roman", 20), width=45)
    new_notes_entry.grid(row=3, column=1, columnspan=3 ,pady=10, padx=10)

    # Edit Button
    edit_button = Button(edit_frame, text="Update Appointment", bg=fg_color, fg="#FFFFFF",
                         font=("times new roman", 20, 'bold'),
                         command=lambda: edit(current_patient, app_id_entry, day_listbox,hour_entry,min_entry, new_notes_entry))
    edit_button.grid(row=4, column=0, columnspan=4, pady=20)


def delete_f(current_patient):
    # Title for Delete Section
    Label(view_appointment_tab, text="Delete An Appointment", bg=bg_color, fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=3, column=0, pady=(40, 10))

    # Delete LabelFrame (The Bordered Box)
    delete_frame = LabelFrame(view_appointment_tab, text=" Danger Zone ", 
                              bg=bg_color, fg="red", relief="solid", borderwidth=1, padx=20, pady=20)
    delete_frame.grid(row=4, column=0, padx=20, pady=10)

    # Appointment ID Input
    Label(delete_frame, text="Appointment ID", bg=bg_color, fg=fg_color, 
          font=("times new roman", 20, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    app_idd_entry = Entry(delete_frame, font=("times new roman", 20), width=20)
    app_idd_entry.grid(row=0, column=1, pady=10, padx=10)

    # Delete Button
    delete_button = Button(delete_frame, text="Confirm Delete", bg="#cc0000", fg="#FFFFFF",
                           font=("times new roman", 20, 'bold'),
                           command=lambda: delete(current_patient, app_idd_entry))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)



def bill_f(current_patient):
    global bill_frame
    
    # Center the table in the tab
    bill_tab.columnconfigure(0, weight=1)
    
    # Container Frame
    bill_frame = Frame(bill_tab, bg=bg_color)
    bill_frame.grid(row=0, column=0, pady=20)

    # Section Title
    Label(bill_frame, 
          text="Billing & Invoices", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=0, column=0, columnspan=4, pady=(0, 20))

    # Table Headers
    headers = ["Appointment ID", "Patient ID", "Total Amount", "Payment Status"]
    for col, text in enumerate(headers):
        header_label = Label(bill_frame, 
                             text=text, 
                             bg='#E0E0E0', 
                             font=("times new roman", 16, 'bold'),
                             relief="solid", 
                             borderwidth=1, 
                             width=18)
        header_label.grid(row=1, column=col, sticky="nsew")

    # Fetch Data and Fill Table
    iii = 0
    appointments = current_patient.view_appointments()
    
    for a in appointments:
        bill = current_patient.view_bill(a[0])
        if bill:
            status_text = str(bill[4]).strip().lower()
            status_fg = "green" if status_text == "paid" else "orange"
            
            current_row = iii + 2
            
            # Appt ID
            Label(bill_frame, text=bill[1], bg="white", font=("times new roman", 14),
                  relief="solid", borderwidth=1).grid(row=current_row, column=0, sticky="nsew")
            
            # Patient ID
            Label(bill_frame, text=bill[2], bg="white", font=("times new roman", 14),
                  relief="solid", borderwidth=1).grid(row=current_row, column=1, sticky="nsew")
            
            # Total Amount 
            Label(bill_frame, text=f"${bill[3]}", bg="white", font=("times new roman", 14),
                  relief="solid", borderwidth=1).grid(row=current_row, column=2, sticky="nsew")
            
            # Payment Status
            Label(bill_frame, text=bill[4], bg="white", fg=status_fg, font=("times new roman", 14, 'bold'),
                  relief="solid", borderwidth=1).grid(row=current_row, column=3, sticky="nsew")
            
            iii += 1


def pay_f(current_patient):
    bill_tab.columnconfigure(0, weight=1)

    # Section Title
    Label(bill_tab, 
          text="Pay An Appointment", 
          bg=bg_color, 
          fg='black', 
          font=("times new roman", 30, 'bold', 'underline')).grid(row=1, column=0, pady=(40, 10))

    # Payment LabelFrame (The Boxed Container)
    pay_frame = LabelFrame(bill_tab, 
                           text=" Payment Details ", 
                           bg=bg_color, 
                           font=("times new roman", 15, 'italic'),
                           relief="solid", 
                           borderwidth=1, 
                           padx=30, 
                           pady=20)
    pay_frame.grid(row=2, column=0, padx=20, pady=10)

    # Appointment ID Input
    Label(pay_frame, 
          text="Appointment ID", 
          bg=bg_color, 
          fg=fg_color, 
          font=("times new roman", 22, 'bold')).grid(row=0, column=0, sticky="w", pady=10)
    
    app_iddd_entry = Entry(pay_frame, 
                           font=("times new roman", 22), 
                           width=20)
    app_iddd_entry.grid(row=0, column=1, pady=10, padx=10)

    # Pay Button
    pay_button = Button(pay_frame,
                        text="Complete Payment",
                        bg=fg_color,
                        fg="#FFFFFF",
                        font=("times new roman", 22, 'bold'),
                        cursor="hand2",
                        command=lambda: pay(current_patient, app_iddd_entry)
                        )
    pay_button.grid(row=1, column=0, columnspan=2, pady=(20, 10))


def open_patient(username,password):
    global patient_window
    global doctor_list_tab
    global view_appointment_tab
    global bill_tab
    current_patient = Patient.login(username,password)
    patient_window = Tk()
    patient_window.title("Patient Page")
    screen_width = patient_window.winfo_screenwidth()
    screen_height = patient_window.winfo_screenheight()
    patient_window.geometry(f"{screen_width}x{screen_height}+0+0")
    patient_window.state("zoomed")
    patient_window.configure(bg= bg_color)

    profile_f(current_patient)

    patient_tabs = ttk.Notebook(patient_window) 
    patient_tabs.pack(expand=True,fill="both")  

    doctor_list_tab = create_scrollable_tab(patient_tabs,"Doctors List")
    view_appointment_tab = create_scrollable_tab(patient_tabs,"My Appointment")
    bill_tab = create_scrollable_tab(patient_tabs,"Bills")

    doctor_list_f(current_patient)
    book_f(current_patient)
    view_f(current_patient)
    edit_f(current_patient)
    delete_f(current_patient)
    bill_f(current_patient)
    pay_f(current_patient)


    patient_window.mainloop()


