
from tkinter import *

root = Tk()

def myClick():
    myLabel1 = Label(root, text="..")
    myLabel1.pack()

myButton = Button(root, text="Input Image", padx=50, pady=10, command=myClick)
myButton.pack()

def convert():
    myLabel2 = Label(root, text="..")
    myLabel2.pack()
myButton2 = Button(root, text="Grey Conversion", padx=50, pady=10, command=convert)
myButton2.pack()

def train():
    myLabel3 = Label(root, text="..")
    myLabel3.pack()
myButton3 = Button(root, text="Trainning Dataset", padx=50, pady=10, command=train)
myButton3.pack()

def detect():
    myLabel4 = Label(root, text="..")
    myLabel4.pack()
myButton4 = Button(root, text="Fake Currency Detection", padx=50, pady=10, command=detect)
myButton4.pack()

def myClick2():
    myLabel5 = Label(root, text="..")
    myLabel5.pack()
myButton5 = Button(root, text="Quit!!", padx=50, pady=10, command=myClick2)
myButton5.pack()

root.mainloop()