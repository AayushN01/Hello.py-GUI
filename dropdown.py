from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Drop down menu")
root.iconbitmap('C:/Users/compaq-pc/Desktop')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
            "Monday",
            "Tuesday",
            "wednesday",
            "Thursday",
            "Friday",
            "Saturday"
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options).pack() 

myButton = Button(root, text="Select", command=show).pack()

root.mainloop()