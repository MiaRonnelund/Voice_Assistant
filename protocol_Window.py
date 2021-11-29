import tkinter as tk
from tkinter import messagebox
from typing_extensions import IntVar

def pInput():
    window = tk.Tk()
    window.title("Welcome")

    lbl = tk.Label(window, text="Set your preferences", font=("Arial Bold", 24)).grid(column=0, row=0, padx=100)
    window.geometry('700x200')

    #adds - make check button
    a_state = tk.BooleanVar()
    a_state.set(True)
    a_check = tk.Checkbutton(window, text="Allow Adds", var=a_state).grid(column=0, row=1)

    #Location - make button
    l_state = tk.BooleanVar()
    l_state.set(True)
    location_check = tk.Checkbutton(window, text="Allow location based", var=l_state, anchor="e").grid(column=0, row=2)

    morning = tk.Label(window, text="Morning time").grid(column=0, row=3)
    night = tk.Label(window, text="Night time").grid(column=0, row=4)

    morningx = tk.IntVar()
    morning_input = tk.Entry(window, textvariable=morningx)

    nightx = tk.IntVar()
    night_input = tk.Entry(window, textvariable=nightx)

    morning_input.grid(column=1,row=3)
    night_input.grid(column=1,row=4)
    send_bnt = tk.Button(window, text="Registrer permissions", command=clicked).grid(column=0, row=5)

    window.mainloop()

    morning_time = morningx.get()
    get_night = nightx.get()
    aInput = a_state.get()
    lInput = l_state.get()

    return(morning_time, get_night, aInput, lInput)

def clicked():
    messagebox.showinfo("Thank you!", "Thank you for registering your preferences")
    
