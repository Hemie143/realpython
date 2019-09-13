from tkinter import *
from tkinter import filedialog

window = Tk()
frame = Frame()
frame.pack()

def save_file():
    type_list = [("Python scripts", "*.py"), ("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(filetypes=type_list, defaultextension=".py")
    my_text = "I will save: " + file_name
    label_file.config(text=my_text)

label_file = Label(frame)
label_file.pack()

button_open = Button(frame, text="Choose a file...", command=save_file)
button_open.pack()

window.mainloop()
