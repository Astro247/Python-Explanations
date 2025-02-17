#I frame sono dei riquadri interni alla finestra che contengono dei widgets.

from tkinter import *

window_with_frames = Tk()

buttons_area = Frame(window_with_frames)
buttons_area.grid(row=1,column=1)

w_key = Button(buttons_area, text="W", font=("Arial", 25, "bold"), width=3, activebackground="black", activeforeground="white")
w_key.grid(row=1,column=2)

a_key = Button(buttons_area, text="A", font=("Arial", 25, "bold"), width=3, activebackground="black", activeforeground="white")
a_key.grid(row=2,column=1)

s_key = Button(buttons_area, text="S", font=("Arial", 25, "bold"), width=3, activebackground="black", activeforeground="white")
s_key.grid(row=2,column=2)

d_key = Button(buttons_area, text="D", font=("Arial", 25, "bold"), width=3, activebackground="black", activeforeground="white")
d_key.grid(row=2,column=3)

window_with_frames.mainloop()