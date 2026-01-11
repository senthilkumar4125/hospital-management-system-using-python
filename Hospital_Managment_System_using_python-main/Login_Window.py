from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from patient import Patient
from Patient_Window import open_patient

from doctor import Doctor
from Doctor_Window import open_doctor

from staff import Staff
from Staff_Window import open_staff



bg_color = "#D3D3D3"
fg_color = "#0026FF"

def signup():
    login_window.destroy()
    from Signup_Window import open_signup
    open_signup()

def staff_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    current_staff = Staff.login(username, password)
    if current_staff == None:
        messagebox.showerror(title="Login Failed",
                             message="❌ Invalid username or password"
                             )
    else:
        messagebox.showinfo(title="Login Success",
                            message="✔ Login successful!"
                            )
        login_window.destroy()
        open_staff(username,password)


def doctor_login(doc_id_entry):
    doctor_id = int(doc_id_entry.get())
    current_user = Doctor.login(doctor_id)
    if current_user == None:
        messagebox.showerror(title="Login Failed",
                             message="❌ Invalid Doctor ID"
                             )
    else:
        messagebox.showinfo(title="Login Success",
                            message="✔ Login successful!"
                            )
        login_window.destroy()
        open_doctor(doctor_id)

def patient_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    current_patient = Patient.login(username, password)
    if current_patient == None:
        messagebox.showerror(title="Login Failed",
                             message="❌ Invalid username or password"
                             )
    else:
        messagebox.showinfo(title="Login Success",
                            message="✔ Login successful!"
                            )
        login_window.destroy()
        open_patient(username,password)



def doctor_login_f():
    # 1. Clear any old widgets in the tab to prevent overlapping
    for widget in doctor_tab.winfo_children():
        widget.destroy()

    # 2. Main Container 
    login_frame = LabelFrame(doctor_tab, 
                             text=" Security Verification ", 
                             bg=bg_color,
                             font=("times new roman", 15, 'italic'),
                             relief="solid", 
                             borderwidth=1, 
                             padx=50, 
                             pady=40)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    # 3. Header Icon & Title
    Label(login_frame, text="⚕️", font=("serif", 60), bg=bg_color, fg=fg_color).grid(row=0, column=0, columnspan=2)
    
    login_label = Label(login_frame,
                        text="Doctor Login",
                        bg=bg_color,
                        fg=fg_color,
                        font=("times new roman", 40, 'bold')
                        )
    login_label.grid(row=1, column=0, columnspan=2, pady=(10, 40))

    # 4. Input Field
    Label(login_frame,
          text="Doctor ID",
          bg=bg_color,
          fg="#333333",
          font=("times new roman", 22, 'bold')
          ).grid(row=2, column=0, sticky="w", pady=10)

    doc_id_entry = Entry(login_frame,
                         font=("times new roman", 22),
                         width=25,
                         relief="groove",
                         borderwidth=2
                         )
    doc_id_entry.grid(row=2, column=1, pady=10, padx=(20, 0))

    # 5. Button Container
    btn_frame = Frame(login_frame, bg=bg_color)
    btn_frame.grid(row=3, column=0, columnspan=2, pady=(40, 0))

    # Login Button
    login_btn = Button(btn_frame,
                       text="Login",
                       bg=fg_color,
                       fg="#FFFFFF",
                       width=10,
                       font=("times new roman", 20, 'bold'),
                       cursor="hand2",
                       relief="raised",
                       command=lambda: doctor_login(doc_id_entry)
                       )
    login_btn.pack(side=LEFT, padx=10)

    # Sign Up Button 
    signup_btn = Button(btn_frame,
                        text="Register",
                        bg="#555555", 
                        fg="#FFFFFF",
                        width=10,
                        font=("times new roman", 20, 'bold'),
                        cursor="hand2",
                        relief="raised",
                        command=signup
                        )
    signup_btn.pack(side=LEFT, padx=10)

    return doc_id_entry


def page(tab, fun, type):
    # 1. Clear any existing widgets in the tab
    for widget in tab.winfo_children():
        widget.destroy()

    # 2. Card-style Container
    login_frame = LabelFrame(tab, 
                             text=f" {type} Portal Access ", 
                             bg=bg_color,
                             font=("times new roman", 15, 'italic'),
                             relief="solid", 
                             borderwidth=1, 
                             padx=50, 
                             pady=40)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    # 3. Header Title
    Label(login_frame,
          text=f"{type} Login",
          bg=bg_color,
          fg=fg_color,
          font=("times new roman", 40, 'bold')
          ).grid(row=0, column=0, columnspan=2, pady=(0, 40))

    # 4. Input Fields
    # Username Field
    Label(login_frame,
          text="Username",
          bg=bg_color,
          fg="#333333", # Dark grey for readability
          font=("times new roman", 22, 'bold')
          ).grid(row=1, column=0, sticky="w", pady=10)

    username_entry = Entry(login_frame,
                           font=("times new roman", 22),
                           width=25,
                           relief="groove",
                           borderwidth=2)
    username_entry.grid(row=1, column=1, pady=10, padx=(20, 0))

    # Password Field
    Label(login_frame,
          text="Password",
          bg=bg_color,
          fg="#333333",
          font=("times new roman", 22, 'bold')
          ).grid(row=2, column=0, sticky="w", pady=10)

    password_entry = Entry(login_frame,
                           show="*",
                           font=("times new roman", 22),
                           width=25,
                           relief="groove",
                           borderwidth=2)
    password_entry.grid(row=2, column=1, pady=10, padx=(20, 0))

    # 5. Button Sub-frame
    btn_frame = Frame(login_frame, bg=bg_color)
    btn_frame.grid(row=3, column=0, columnspan=2, pady=(40, 0))

    # Login Button
    login_button = Button(btn_frame,
                          text="Login",
                          bg=fg_color,
                          fg="#FFFFFF",
                          width=10,
                          font=("times new roman", 20, 'bold'),
                          cursor="hand2",
                          relief="raised",
                          command=lambda: fun(username_entry, password_entry))
    login_button.pack(side=LEFT, padx=10)

    # Sign Up Button
    signup_button = Button(btn_frame,
                           text="Sign Up",
                           bg="#555555", # Professional secondary color
                           fg="#FFFFFF",
                           width=10,
                           font=("times new roman", 20, 'bold'),
                           cursor="hand2",
                           relief="raised",
                           command=signup)
    signup_button.pack(side=LEFT, padx=10)

    return username_entry, password_entry


def open_login():
    global login_window
    global doctor_tab
    login_window = Tk()
    login_window.title("Log-In Page")
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    login_window.geometry(f"{screen_width}x{screen_height}+0+0")
    login_window.state("zoomed")
    login_window.configure(bg= bg_color)


    login_tabs = ttk.Notebook(login_window) 

    staff_tab = Frame(login_tabs,
                    bg= bg_color,
                    )
    doctor_tab = Frame(login_tabs,
                    bg= bg_color
                    )
    patient_tab = Frame(login_tabs,
                    bg= bg_color
                    )

    login_tabs.add(staff_tab,
                text="Staff",
                )
    login_tabs.add(doctor_tab,
                text="Doctor",
                )
    login_tabs.add(patient_tab,
                text="Patient",
                )

    login_tabs.pack(expand=True,
                    fill="both"
                )
    
    page(staff_tab,staff_login, 'Staff')
    doctor_login_f()
    page(patient_tab,patient_login, 'Patient')

    login_window.mainloop()