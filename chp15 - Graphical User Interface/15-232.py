from tkinter import *

window = Tk()

my_frame = Frame()
my_frame.grid()

label_top_left = Label(my_frame, text="I'm at (1,1)", bd="3", relief=SUNKEN)
label_top_left.grid(row=1, column=1, padx=100, pady=30)

label_bottom_left = Label(my_frame, text="I'm at (2,1)", bd="3", relief=SUNKEN)
label_bottom_left.grid(row=2, column=1, sticky=E)

button_right = Button(my_frame, text="I span 2 rows", height=5)
button_right.grid(row=1, column=2, rowspan=2)

window.mainloop()
