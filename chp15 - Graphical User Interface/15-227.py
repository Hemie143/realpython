from tkinter import *

window = Tk()

my_frame = Frame()
my_frame.pack()

label_text1 = Label(my_frame, text="top bar", bg="red")
label_text1.pack(fill=X)

label_left = Label(my_frame, text="left", bg="yellow")
label_left.pack(side=LEFT)

label_mid = Label(my_frame, text="middle", bg="green")
label_mid.pack(side=LEFT)

label_right = Label(my_frame, text="right", bg="blue")
label_right.pack()

window.mainloop()
