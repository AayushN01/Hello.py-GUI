from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Using Icons, Images and Exit Buttons')
root.iconbitmap('C:/Users/compaq-pc/Desktop')

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/Project/icon.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/Project/images/fb.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/Project/images/gmail.png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/Project/images/linkedin.png"))
my_img6 = ImageTk.PhotoImage(Image.open("C:/Users/compaq-pc/Desktop/Project/images/phone.png"))

image_list = [my_img1, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_fwd
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_fwd = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda:back(image_number-1))
    
    if image_number == 5:
        button_fwd = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_fwd.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_fwd
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_fwd = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda:back(image_number-1))
    
    if image_number == 1:
            button_back = Button(root, text="<<", state=DISABLED)

   
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_fwd.grid(row=1, column=2)
    

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_fwd.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit", command=root.quit)

button_fwd = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2)
root.mainloop()