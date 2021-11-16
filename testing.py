import tkinter as tk
from tkinter import messagebox
from typing_extensions import IntVar

window = tk.Tk()
window.title("Welcome")

lbl = tk.Label(window, text="Set your preferences", font=("Arial Bold", 24)).grid(column=0, row=0, padx=100)
#lbl.grid(column=0, row=0)

window.geometry('700x200')

a_state = tk.BooleanVar()
a_state.set(True)
a_check = tk.Checkbutton(window, text="Allow Adds", var=a_state).grid(column=0, row=1)
#a_check.grid(column=0, row=1)

l_state = tk.BooleanVar()
l_state.set(True)
location_check = tk.Checkbutton(window, text="Allow location based", var=l_state, anchor="e").grid(column=0, row=2)
#location_check.grid(column=0, row=2)

morning = tk.Label(window, text="Morning time").grid(column=0, row=3)
night = tk.Label(window, text="Night time").grid(column=0, row=4)

morning_input = tk.Entry(window)
night_input = tk.Entry(window)
get_night = night_input.get()

morning_input.grid(column=1,row=3)
night_input.grid(column=1,row=4)

def clicked():
    messagebox.showinfo("Thank you!", "Thank you for registering your preferences")

send_bnt = tk.Button(window, text="Registrer permissions", command=clicked).grid(column=0, row=5)


# morning_time = morning_input.get
# night_time = night_input.get

# def get_values():
#     morning_time = int(morning_input.get())
#     night_time = int(night_input.get())
#     a = a_state.get()
#     l = l_state.get()

print(get_night)
window.mainloop()