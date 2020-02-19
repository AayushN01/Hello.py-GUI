from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Slider")
root.iconbitmap('C:/Users/compaq-pc/Desktop')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    my_label= Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn =  Button(root, text="Click ME!", command=slide).pack()
root.mainloop()