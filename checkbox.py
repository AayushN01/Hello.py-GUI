from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Slider")
root.iconbitmap('C:/Users/compaq-pc/Desktop')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

#var = IntVar()
var = StringVar()
c = Checkbutton(root, text="Check this box, I dare you!!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text= "Show Selection", command=show).pack()

root.mainloop()