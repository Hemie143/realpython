from tkinter import *

window = Tk()

def increment_button():
    new_number = 1 + my_button.cget("text")
    my_button.config(text=new_number)

my_button = Button(text=1, command=increment_button)
my_button.pack()

window.mainloop()
