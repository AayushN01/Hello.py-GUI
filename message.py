from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root= Tk()
root.title("Message Box")
root.iconbitmap('C:/Users/compaq-pc/Desktop')
 #shhowinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    #messagebox.showinfo("This is my popUp", "Hello, World!!")
    #messagebox.showwarning("This is my popUp", "Hello, World!!")
    #messagebox.showerror("This is my popUp", "Hello, World!!")
    #messagebox.askquestion("This is my popUp", "Hello, World!!")
    #messagebox.askokcancel("This is my popUp", "Hello, World!!")
    response = messagebox.askyesno("This is my popUp", "Hello, World!!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!!").pack()
    else:
        Label(root, text="You clicked no!!").pack()


Button(root, text="Popup", command=popup).pack()



mainloop()