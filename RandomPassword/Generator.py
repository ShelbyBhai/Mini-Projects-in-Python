import random
import string
from tkinter import *


def password():
    PassString = []
    for i in range(3):
        number = random.choice(string.digits)
        charup = random.choice(string.ascii_uppercase)
        chardown = random.choice(string.ascii_lowercase)
        symbols = random.choice(string.punctuation)
        PassString.append(number)
        PassString.append(charup)
        PassString.append(chardown)
        PassString.append(symbols)

    FinalPassword = "".join(str(j)for j in PassString)
    layer.config(text=FinalPassword)



base = Tk()

base.geometry("600x400")

button = Button(base, text="Give me the password", command=password)

button.grid(row=2, column=2)

layer = Label(base, font=("times", 18, "italic"))

layer.grid(row=4, column=2)

base.mainloop()


