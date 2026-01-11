from tkinter import *
from tkinter import ttk


# def create_scrollable_tab(notebook,title):
#     tab = ttk.Frame(notebook)
#     notebook.add(tab, text=title)

#     canvas = Canvas(tab)
#     scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)

#     scrollable_frame = Frame(canvas,bg= "#D3D3D3")

#     scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#     canvas.configure(yscrollcommand=scrollbar.set,bg="#D3D3D3")
#     canvas.bind_all("<MouseWheel>",lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))
    
#     canvas.pack(side="left", fill="both", expand=True)

#     scrollbar.pack(side="right", fill="y")

#     return scrollable_frame



def create_scrollable_tab(notebook, title):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=title)

    canvas = Canvas(tab, bg="#D3D3D3", highlightthickness=0)
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#D3D3D3")

    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

    # --- Improved Scrolling Logic ---
    
    def _on_mousewheel(event):
        # Standard scroll calculation
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(event):
        # Bind specifically to this canvas when mouse enters
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _unbind_from_mousewheel(event):
        # Unbind when mouse leaves so other widgets can use the wheel
        canvas.unbind_all("<MouseWheel>")

    # Bind the enter/leave events to the canvas AND the inner frame
    # This ensures scrolling works even if the mouse is over a button inside the frame
    canvas.bind("<Enter>", _bind_to_mousewheel)
    canvas.bind("<Leave>", _unbind_from_mousewheel)
    
    # --- Existing Configuration ---

    def configure_scroll_region(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
        if scrollable_frame.winfo_reqwidth() < canvas.winfo_width():
            canvas.itemconfigure(canvas_window, width=canvas.winfo_width())

    scrollable_frame.bind("<Configure>", configure_scroll_region)
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(canvas_window, width=e.width))

    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)

    scrollable_frame.columnconfigure(0, weight=1)
    scrollable_frame.rowconfigure(0, weight=1)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame



def create_styled_notebook(parent):
    style = ttk.Style()
    style.theme_use('clam')
    
    # Modern Flat Design
    style.configure("TNotebook", background="#E0E0E0", borderwidth=0)
    style.configure("TNotebook.Tab", 
                    background="#C0C0C0", 
                    padding=[20, 8], 
                    font=('Helvetica', 10, 'bold'))
    style.map("TNotebook.Tab", background=[("selected", "#D3D3D3")])

    notebook = ttk.Notebook(parent)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    return notebook
