from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Using Icons, Images and Exit Buttons')
root.iconbitmap('C:/Users/compaq-pc/Desktop')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/icon.png"))
my_label = Label(image=my_img)
my_label.pack()






button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()
root.mainloop()