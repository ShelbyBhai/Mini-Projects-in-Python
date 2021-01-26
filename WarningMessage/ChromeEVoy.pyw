from tkinter import *

_signboard = Tk()

_signboard.geometry("1200x900")

warning = Label(_signboard, text="BlueScreen Error dite pare Bhai ektu por!!", font=("times", 50, "italic"))

warning.grid(row=2, column=0, padx=20, pady=20)

warning.config(background="blue")

_signboard.mainloop()