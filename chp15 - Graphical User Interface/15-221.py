from easygui import *

value = msgbox("MessageBox", "This is a message box")
print(value)

colors = ("Red", "Green", "Blue")
value = buttonbox("Choose a color", "Color", colors)
print(value)

value = fileopenbox("", "Select a file", "*.*")
print(value)

value = indexbox("Indexbox message", "Indexbox title", ["Yes", "No"])
print(value)

value = choicebox("Choicebox message", "Choicebox title", ["Item1", "Item2"])
print(value)

value = multchoicebox("Choicebox message", "Choicebox title", ["Item1", "Item2"])
print(value)

value = enterbox("Enterbox message", "Enterbox title", "String")
print(value)

value = passwordbox("Passwordbox message", "Passwordbox title", "")
print(value)

value = textbox("Textbox message", "Textbox title", "")
print(value)


'''
indexbox() , choicebox() , multchoicebox() , enterbox() , passwordbox()
and textbox() to see what GUI elements they produce; you can use the help()
function to read more about each
'''