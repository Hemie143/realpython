from tkinter import *

window = Tk()
window.geometry("200x50")

frame_left = Frame(bd=3, relief=SUNKEN)
frame_left.place(relx=0, relwidth=0.5, relheight=1)

frame_right = Frame(bd=3, relief=SUNKEN)
frame_right.place(relx=0.7, relwidth=0.3)

left_label = Label(frame_left, text="I've been framed!")
left_label.pack()

right_label = Label(frame_right, text="So have I!")
right_label.pack()

window.mainloop()
