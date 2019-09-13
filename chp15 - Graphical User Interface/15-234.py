from tkinter import *

window = Tk()

entry1 = Entry()
entry1.pack()
entry1.insert(0, "this is an entry")

entry2 = Entry()
entry2.pack()

my_text = entry1.get()
entry2.insert(0, my_text)
entry2.insert(8, "also ")

window.mainloop()
