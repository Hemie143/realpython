from tkinter import *

def recalc():
    cel_temp = entry_cel.get()
    try:
        far_temp = float(cel_temp) * 9/5 + 32
        far_temp = round(far_temp, 3)
        result_far.config(text=far_temp)
    except:
        result_far.config(text="invalid")

window = Tk()
window.title("Temperature converter")

frame = Frame()
frame.grid(padx=5, pady=5)

label_cel = Label(frame, text="Celsius temperature:")
label_cel.grid(row=1, column=1, sticky=S+E)

label_far = Label(frame, text="Fahrenheit temperature")
label_far.grid(row=2, column=1, sticky=S+E)

entry_cel = Entry(frame, width=7)
entry_cel.grid(row=1, column=2)

result_far = Label(frame)
result_far.grid(row=2, column=2)

btn_recalc = Button(frame, text="Recalculate", command=recalc)
btn_recalc.grid(row=1, column=3, rowspan=2)

recalc()

window.mainloop()
