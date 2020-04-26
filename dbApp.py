from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()
root.title("Database")
root.iconbitmap('C:/Users/compaq-pc/Desktop/Tkinter/icon.png')
root.geometry("400x400")

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#create a cursor c
c = conn.cursor()

#create table

# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
# )""")

#Create function to delete
def delete():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #create a cursor c
    c = conn.cursor() 

    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())


     #commit changes
    conn.commit()

    #close connection
    conn.close()  

#create submit function for database
def submit():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #create a cursor c
    c = conn.cursor() 

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        
        }
    
    
    
    
        )


    #commit changes
    conn.commit()

    #close connection
    conn.close()    


    #clear text box
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#Qyery function
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #create a cursor c
    c = conn.cursor()

    #query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() #fetchone(), fetchmany()
    print(records)

    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + " \t" + str(record[6])
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    #commit changes
    conn.commit()

    #close connection
    conn.close() 
#create text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box= Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#create textbox label

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Adddress")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete Id")
delete_box.grid(row=9, column=0, pady=5,)

submit_btn= Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10 ,padx=10, ipadx=100)

#Create a query button
query_btn = Button(root, text="SHow Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#Create a delete button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()