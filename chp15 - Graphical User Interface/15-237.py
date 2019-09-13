from tkinter import *
from tkinter import filedialog

window = Tk()
frame = Frame()
frame.pack()

def open_file():
    type_list = [("Python scripts", "*.py"), ("Text files", "*.txt")]
    file_name = filedialog.askopenfilename(filetypes=type_list)
    label_file.config(text=file_name)

label_file = Label(frame)
label_file.pack()

button_open = Button(frame, text="Choose a file...", command=open_file)
button_open.pack()

window.mainloop()
