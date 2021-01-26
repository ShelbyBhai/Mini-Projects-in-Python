from tkinter import *

import YotubeChannelAnalysis

_holder = Tk()

_holder.geometry("800x600")

_ch_name = StringVar()

_input = Entry(_holder, textvariable=_ch_name)

_input.grid(row=1, column=2)

_button = Button(_holder, text="Analyze", command=YotubeChannelAnalysis.Channel_date)

_button.grid(row=2, column=2)

l1 = Label(_holder, text="Subscriber : ", font="times 20 bold")

l1.grid(row=4, column=1)

l2 = Label(_holder, font="times 20 bold")

l2.grid(row=4, column=3)

l3 = Label(_holder, text="ViewCount : ", font="times 20 bold")

l3.grid(row=6, column=1)

l4 = Label(_holder, font="times 20 bold")

l4.grid(row=6, column=3)

l5 = Label(_holder, text="VideoCount : ", font="times 20 bold")

l5.grid(row=8, column=1)

l6 = Label(_holder, font="times 20 bold")

l6.grid(row=8, column=3)

_holder.mainloop()
