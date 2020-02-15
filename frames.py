from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Adding Frames to program')
root.iconbitmap('C:/Users/compaq-pc/Desktop')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b= Button(frame, text="Don`t click here!")
b.pack()

root.mainloop()