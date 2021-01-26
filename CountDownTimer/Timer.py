from tkinter import *

time = 0


def _set_Time():
    global time
    time = time + int(_getting_time.get())
    return time


def _Counter():
    global time
    if time > 0:
        l.config(text=time)
        time = time - 1
        l.after(1000, _Counter)
    elif time == 0:
        l.config(text="Done!!")


builder = Tk()

builder.geometry("200x130")

builder.title("StopWatch")

l = Label(builder, font="times 25")

l.grid(row=1, column=2)

_getting_time = StringVar()

_input = Entry(builder, textvariable=_getting_time)

_input.grid(row=3, column=2)

b1 = Button(builder, width=20, text="SetTime", command=_set_Time)

b1.grid(row=4, column=2, padx=25)

b2 = Button(builder, width=20, text="StartTime", command=_Counter)

b2.grid(row=6, column=2, padx=25)

builder.mainloop()
