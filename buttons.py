
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I Clicked a button!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=10, command=myClick, fg="blue", bg="brown")
myButton.pack()
root.mainloop()
