from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from patient import Patient
from doctor import Doctor
from Login_Window import open_login


bg_color = "#D3D3D3"
fg_color = "#0026FF"

def login():
    signup_window.destroy()
    from Login_Window import open_login
    open_login()

def doctor_signup(name_entry, specialty_entry, age_entry):
    name = name_entry.get()
    specialty = specialty_entry.get()
    age = age_entry.get()
    current_user = Doctor.sign_up(name, specialty, age)
    if name == "" or specialty == "" or age == "":
        messagebox.showerror(title="Sign_UP Failed",
                             message="❌ Invalid Data"
                             )
    else:
        messagebox.showinfo(title="Sign_UP Success",
                            message=f"✔ signup successful! \n Dr.{current_user.name} added successfully with ID: {current_user.id}"
                            )
        signup_window.destroy()
        open_login()

        

def patient_signup(name_entry, age_entry, gender_entry, username_entry, password_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    current_patient = Patient.signup(name, age, gender, username, password)
    current_patient = Patient.login(username,password) 
    if name == ""  or age == "" or gender == "" or username == "" or password == "":
        messagebox.showerror(title="Sign_UP Failed",
                             message="❌ Invalid  Data"
                             )
    else:
        messagebox.showinfo(title="Sign_UP Success",
                            message=f"✔ Sign_UP successful! \n Dr.{current_patient.name} added successfully with Username: {current_patient.username} "
                            )
        signup_window.destroy()
        open_login()



def doctor_signup_f():
    # Clear the tab for a fresh view
    for widget in doctor_tab.winfo_children():
        widget.destroy()

    # Main Container
    signup_frame = LabelFrame(doctor_tab, 
                              text=" Registration Portal ", 
                              bg=bg_color,
                              font=("times new roman", 15, 'italic'),
                              relief="solid", borderwidth=1, 
                              padx=40, pady=20)
    signup_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header Title
    Label(signup_frame, text="Doctor Sign Up", bg=bg_color, fg=fg_color,
          font=("times new roman", 40, 'bold', 'underline')).grid(row=0, column=0, columnspan=2, pady=(10, 40))

    fields = [("Full Name", "name"), ("Specialty", "spec"), ("Age", "age")]
    entries = {}

    for i, (label_text, key) in enumerate(fields):
        Label(signup_frame, text=label_text, bg=bg_color, fg="#333333",
              font=("times new roman", 22, 'bold')).grid(row=i+1, column=0, sticky="w", pady=15)
        
        entry = Entry(signup_frame, font=("times new roman", 22), width=25, relief="groove", borderwidth=2)
        entry.grid(row=i+1, column=1, pady=15, padx=(20, 0))
        entries[key] = entry

    # Button Sub-frame
    btn_frame = Frame(signup_frame, bg=bg_color)
    btn_frame.grid(row=4, column=0, columnspan=2, pady=(40, 10))

    Button(btn_frame, text="Login", bg="#555555", fg="white", width=10,
           font=("times new roman", 20, 'bold'), cursor="hand2", command=login).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Sign Up", bg=fg_color, fg="white", width=10,
           font=("times new roman", 20, 'bold'), cursor="hand2",
           command=lambda: doctor_signup(entries["name"], entries["spec"], entries["age"])).pack(side=LEFT, padx=10)
    
    return entries["name"], entries["spec"], entries["age"]


def patient_signup_f():
    # Clear the tab
    for widget in patient_tab.winfo_children():
        widget.destroy()

    # Main Container
    signup_frame = LabelFrame(patient_tab, 
                              text=" Create New Account ", 
                              bg=bg_color,
                              font=("times new roman", 15, 'italic'),
                              relief="solid", borderwidth=1, 
                              padx=40, pady=20)
    signup_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Header Title
    Label(signup_frame, text="Patient Sign Up", bg=bg_color, fg=fg_color,
          font=("times new roman", 40, 'bold', 'underline')).grid(row=0, column=0, columnspan=2, pady=(10, 40))

    # Input mapping
    fields = [("Full Name", "name"), ("Age", "age"), ("Gender", "gen"), 
              ("Username", "user"), ("Password", "pass")]
    entries = {}

    for i, (label_text, key) in enumerate(fields):
        Label(signup_frame, text=label_text, bg=bg_color, fg="#333333",
              font=("times new roman", 20, 'bold')).grid(row=i+1, column=0, sticky="w", pady=10)
        
        # Use show="*" for password field
        is_pass = "*" if key == "pass" else ""
        entry = Entry(signup_frame, font=("times new roman", 20), width=30, 
                      show=is_pass, relief="groove", borderwidth=2)
        entry.grid(row=i+1, column=1, pady=10, padx=(20, 0))
        entries[key] = entry

    # Button sub-frame
    btn_frame = Frame(signup_frame, bg=bg_color)
    btn_frame.grid(row=6, column=0, columnspan=2, pady=(30, 10))

    Button(btn_frame, text="Login", bg="#555555", fg="white", width=12,
           font=("times new roman", 18, 'bold'), cursor="hand2", command=login).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Sign Up", bg=fg_color, fg="white", width=12,
           font=("times new roman", 18, 'bold'), cursor="hand2",
           command=lambda: patient_signup(entries["name"], entries["age"], entries["gen"], 
                                         entries["user"], entries["pass"])).pack(side=LEFT, padx=10)
    
    return entries["name"], entries["age"], entries["gen"], entries["user"], entries["pass"]

def open_signup():
    global signup_window
    global doctor_tab
    global patient_tab
    signup_window = Tk()
    signup_window.title("Sign Up Page")
    screen_width = signup_window.winfo_screenwidth()
    screen_height = signup_window.winfo_screenheight()
    signup_window.geometry(f"{screen_width}x{screen_height}+0+0")
    signup_window.state("zoomed")
    signup_window.configure(bg= bg_color)


    signup_tabs = ttk.Notebook(signup_window) 


    doctor_tab = Frame(signup_tabs,bg= bg_color)
    patient_tab = Frame(signup_tabs,bg= bg_color)


    signup_tabs.add(doctor_tab,text="Doctor",)
    signup_tabs.add(patient_tab,text="Patient",)

    signup_tabs.pack(expand=True,fill="both")

    doctor_signup_f()
    patient_signup_f()

    signup_window.mainloop()