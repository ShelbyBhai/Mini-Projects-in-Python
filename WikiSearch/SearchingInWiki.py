from tkinter.messagebox import showinfo

import wikipedia

from tkinter import *


def _ques_Ans():
    ques = q.get()
    ans = wikipedia.summary(ques)
    showinfo("Answer!!!!", ans)


start = Tk()

start.geometry("500x400+100+100")

start.title("StraightOuttaWiki")

query = StringVar()

q = Entry(start, textvariable=query)

q.grid(row=25, column=35,padx=30,pady=50)

b = Button(start, width=20, text="Go", command=_ques_Ans)

b.grid(row=25, column=70)

start.mainloop()
