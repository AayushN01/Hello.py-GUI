
from tkinter import *

root = Tk()
#Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Hello! I`m Aayush")
myLabel3 = Label(root, text="Hello")
#Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)
root.mainloop()
