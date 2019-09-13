from tkinter import *

window = Tk()

my_frame = Frame()
my_frame.grid()

label_top_left = Label(my_frame, text="I'm at (1,1)")
label_top_left.grid(row=1, column=1)

label_bottom_left = Label(my_frame, text="I'm at (2,1)")
label_bottom_left.grid(row=2, column=1)

button_bottom_right = Button(my_frame, text="I'm at (3,2)")
button_bottom_right.grid(row=3, column=2)

window.mainloop()
