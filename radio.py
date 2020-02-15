from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("Radio Buttons")
root.iconbitmap('C:/Users/compaq-pc/Desktop')

r = IntVar()
r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Chicken","Chicken"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()



def clicked(value):
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable= r, value=1, command=lambda: clicked()).pack()
#Radiobutton(root, text="Option 2", variable= r, value=2, command=lambda: clicked()).pack()
#Radiobutton(root, text="Option 3", variable= r, value=3, command=lambda: clicked()).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()
myButton = Button(root, text="Click Me", command =lambda: clicked(pizza.get()))
myButton.pack()
mainloop()