import tkinter as tk
from tkinter import *
import psutil
import sys
import os

is_on = False

def interface(queue):

    def on_closing():
        print("Quitting")
        p = psutil.Process(os.getppid())
        p.terminate()
        sys.exit()

    def sendStatus(boolean):
        queue.put(boolean)

    def sendRessourceTime():
        try:
            health = f"H{healthTime.get()}"
            mana = f"M{manaTime.get()}"
        except ValueError:
            print("Just put numbers in the fields")
            return

        queue.put(health)
        queue.put(mana)



    print("interface started")

    #Main window
    root = tk.Tk()
    root.geometry("600x500")
    root.configure(bg="#303030")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure([0,1,2,3,4], weight=1)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.title("Auto PoE Ressource")

    #Active label
    border_color = Frame(root, background="#D41920")
    border_color.grid_columnconfigure(0, weight=1)
    border_color.grid_rowconfigure(0, weight=1)
    border_color.grid(row=0, column=0,pady=20)

    stateLabel = tk.Label(border_color, text="Auto PoE Ressource is inactive", font=("Fontin", 20), fg="#D41920",
                          bg="#303030")
    stateLabel.grid(row=0,column=0,pady=2, padx=2)


    def switch():
        global is_on

        # Determine is on or off
        if is_on:
            on_button.config(image=off)
            stateLabel.config(text="Auto PoE Ressource is inactive", font=("Fontin", 20), fg="#D41920", bg="#303030")
            border_color.config(background="#D41920")
            is_on = False
            sendStatus(is_on)
        else:

            on_button.config(image=on)
            stateLabel.config(text="Auto PoE Ressource is active", font=("Fontin", 20), fg="#1D9641", bg="#303030")
            border_color.config(background="#1D9641")
            is_on = True
            sendStatus(is_on)

    # Image
    on = PhotoImage(file="img/on.png")
    off = PhotoImage(file="img/off.png")

    # Health Potion Time
    healthTimeFrame = Frame(root, bg="#303030")
    healthTimeFrame.columnconfigure([0,1], weight=1)
    healthTimeFrame.rowconfigure(0, weight=1)
    healthTimeFrame.grid(row=1,column=0,pady=10)

    healthLabel = Label(healthTimeFrame, text="Health Potion Active Time", font=("Fontin", 12), fg="white", bg="#303030")
    healthLabel.grid(row=0, column=0, padx=5, pady=10)

    healthTime = Entry(healthTimeFrame, width=10, borderwidth=2, bg="#303030", fg="white", font=("Fontin", 10))
    healthTime.grid(row=0, column=1, padx=10, pady=10)

    # Mana Potion Time
    manaTimeFrame = Frame(root, bg="#303030")
    manaTimeFrame.columnconfigure([0, 1], weight=1)
    manaTimeFrame.rowconfigure(0, weight=1)
    manaTimeFrame.grid(row=2, column=0, pady=10)

    manaLabel = Label(manaTimeFrame, text="Mana Potion Active Time", font=("Fontin", 12), fg="white", bg="#303030")
    manaLabel.grid(row=1, column=0, padx=5, pady=10)

    manaTime = Entry(manaTimeFrame, width=10, borderwidth=2, bg="#303030", fg="white", font=("Fontin", 10))
    manaTime.grid(row=1, column=1, padx=10, pady=10)

    #Apply Button
    applyButton = Button(root, text="Apply", font=("Fontin", 15), fg="white", bg="#D41920", bd=0,
                         activebackground="#F5C10D", activeforeground="#303030", width=7, height=1,
                         command=sendRessourceTime)
    applyButton.grid(row=3,column=0,pady=5)



    # On/Off Button
    on_button = Button(root, image=off, command=switch, bg="#303030", bd=0, activebackground="#303030")
    on_button.grid(row=4,column=0,pady=50)


    root.mainloop()
