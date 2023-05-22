import tkinter as tk
from tkinter import messagebox

def display_message():
    name = entry.get()
    if name:
        message = f"Hello, {name}!"
        messagebox.showinfo("Message", message)
    else:
        messagebox.showerror("Error", "Please enter a name.")

# Creazione della finestra principale
window = tk.Tk()
window.title("Form")
window.geometry("300x150")

# Creazione del widget Entry
entry = tk.Entry(window, width=30)
entry.pack(pady=20)

# Creazione del pulsante
button = tk.Button(window, text="Submit", command=display_message)
button.pack()

# Avvio del ciclo principale della finestra
window.mainloop()