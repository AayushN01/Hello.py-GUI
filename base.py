from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("First window")
root.iconbitmap('C:/Users/compaq-pc/Desktop')


def open():  
    global my_img
    top = Toplevel()
    lbl = Label(top, text="Hello, World!!").pack()
    top.title("Second window")
    top.iconbitmap('C:/Users/compaq-pc/Desktop')
    my_img = ImageTk.PhotoImage(Image.open("images/fb.png"))
    my_label = Label(top, image=my_img).pack()

btn = Button(root, text="Open second window", command = open).pack()

mainloop()