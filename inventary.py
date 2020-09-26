from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# when i finish the program, add that is posiible to change the database,edit and exit.(this code not found,at the end finish it)
"""def add_database():
    # database option, put in connet option,that need to put host,user,name of same and password and return thist information 
    # to database for stablish connection. when connecion failed put pop up window, in the moment to add new database, if exists put pop up window(in the same put: host,root,name and password)
    window_add_database = Toplevel(window)
    width = 350
    height = 300
    window_add_database.geometry(f"{width}x{height}")
    window_add_database.resizable(False,False)

    # Title Labels
    host_Label = Label(window_add_database,text = "HOST:")
    host_Label.place(x=10,y=20)
    user_Label = Label(window_add_database,text = "USER:")
    user_Label.place(x=10,y=80)
    pass_Label = Label(window_add_database,text = "PASSWORD:")
    pass_Label.place(x=10,y=140)
    database_Label = Label(window_add_database,text = "DATABASE:")
    database_Label.place(x=10,y=200)

    #STRINGVAR
    host_Label = StringVar()
    user_Label = StringVar()
    pass_Label = StringVar()
    database_Label = StringVar()

    #ENTRY
    host_Entry = Entry(window_add_database,textvariable = host_Label,width = 30)
    host_Entry.place(x=10,y=40)
    user_Entry = Entry(window_add_database,textvariable = user_Label,width = 30)
    user_Entry.place(x=10,y=100)
    pass_Entry = Entry(window_add_database,textvariable = pass_Label,width = 30)
    pass_Entry.place(x=10,y=160)
    database_Entry = Entry(window_add_database,textvariable = database_Label,width = 30)
    database_Entry.place(x=10,y=220)

    #CONFIRM BUTTON
    confirm_button = Button(window_add_database,text="Confirm",bg= "green",command = lambda: stablish_connection(host_Entry,user_Entry,pass_Entry,database_Entry))
    confirm_button.place(x=270,y=250) """

# DB CONNECT
dbConnect = {
    "host": "localhost",
    "user": "root",
    "password": "12345678",
    "database": "inventary"
}

connection = mysql.connector.connect(**dbConnect)
cursor = connection.cursor()


def add_products(product,provider,kind,description,price,quantity):
    # get values for window_to_add
    get_product = product.get()
    get_provider = provider.get()
    get_kind = kind.get()
    get_description = str(description.get())
    get_price = str(price.get())
    get_quantity =str(quantity.get())

    data_obtained = [None,get_product,get_provider,get_kind,get_description,get_price,get_quantity]

    #avoid errors of programs
    if (len(get_product) or len(get_provider) or len(get_kind) or len(get_description) or len(get_price) or len(get_quantity)) == 0:
        messagebox.showerror("ERROR","Complete empty spaces",icon="error")

    elif (len(get_product) and len(get_provider) and len(get_kind) and len(get_description) and len(get_price) and len(get_quantity)) == 0:
        messagebox.showerror("ERROR","You cangt leave empty spaces",icon="error")

    else:
        #upload data to database
        connection = mysql.connector.connect(**dbConnect)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO inventary VALUES(%s,%s,%s,%s,%s,%s,%s)",data_obtained)
        connection.commit()
        connection.close()
        #ADD MESSAGEBOX WHEN PROGRAMA FINISH AND CLEAR ENTRY WIDGETS

def window_to_add():
    window_add_products = Toplevel(window)
    width = 400
    height = 400
    #ADD OPTION TO PREVENT THE WINDOW FROM MOVING
    window_add_products.geometry(f"{width}x{height}")
    window_add_products.resizable(False,False)

    # Title Labels
    product_Label = Label(window_add_products,text = "PRODUCT:")
    product_Label.place(x=10,y=20)

    provider_Label = Label(window_add_products,text = "PROVIDER:")
    provider_Label.place(x=10,y=80)

    kind_Label = Label(window_add_products,text = "KIND:")
    kind_Label.place(x=10,y=140)

    description_Label = Label(window_add_products,text = "DESCRIPTION:")
    description_Label.place(x=10,y=200)

    price_Label = Label(window_add_products,text = "PRICE:")
    price_Label.place(x=10,y=260)

    quantity_Label = Label(window_add_products,text = "QUANTITY:")
    quantity_Label.place(x=10,y=320)


    #STRINGVAR
    product_Label = StringVar()
    provider_Label = StringVar()
    kind_Label = StringVar()
    description_Label = StringVar()
    price_Label = StringVar()
    quantity_Label = StringVar()

    #ENTRY
    product_Entry = Entry(window_add_products,textvariable = product_Label,width = 30)
    product_Entry.place(x=10,y=40)

    provider_Entry = Entry(window_add_products,textvariable = provider_Label,width = 30)
    provider_Entry.place(x=10,y=100)

    kind_Entry = Entry(window_add_products,textvariable = kind_Label,width = 30)
    kind_Entry.place(x=10,y=160)

    description_Entry = Entry(window_add_products,textvariable = description_Label,width = 30)
    description_Entry.place(x=10,y=220)

    price_Entry = Entry(window_add_products,textvariable = price_Label,width = 30)
    price_Entry.place(x=10,y=280)

    quantity_Entry = Entry(window_add_products,textvariable = quantity_Label,width = 30)
    quantity_Entry.place(x=10,y=340)

    #CONFIR BUTTON
    confir_button = Button(window_add_products,text= "CONFIRM",bg= "green",command = lambda:add_products(product_Entry,provider_Entry,kind_Entry,description_Entry,price_Entry,quantity_Entry))
    confir_button.place(x=270,y=350)

def window_to_edit():
    print("Edit products")

def window_to_delete():
    print("Delete products")

def consult_products():
    print("consult")

def fuc_create_bill():
    print("created")

def fuc_print_bill():
    print("printing")



# CREATE PRINCIPAL SCREEN 
window = Tk()
window.resizable(False,False)

width = 800
height = 650

x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2) 
window.geometry(f"{width}x{height}+{x}+{y}")

window.config(bg = "#E7E7E7")


# create 2 entry to the app where will receive the database and bill (database label be long and bills label be short and more with)
see_database = Entry(window,width= 70).place(x=10,y=30,height=600)
see_bill = Entry(window,width = 50).place(x=465,y=231,height=400)

scroll_database = Scrollbar(window).place(x=430,y=30,height = 600)
scroll_bill = Scrollbar(window).place(x=765,y=231,height = 400)


#CREATE BILL BUTTONS
create_bill = Button(window,text = "Create",command = lambda:fuc_create_bill()).place(x=660,y=190)
print_bill = Button(window,text = "Print Bill",command = lambda: fuc_print_bill()).place(x=720,y=190)


# MENU BAR OPTIONS
menubar = Menu(window)
window.config(menu=menubar) 

databasemenu = Menu(menubar,tearoff=0)
databasemenu.add_command(label="Select")
databasemenu.add_command(label="Add")
databasemenu.add_separator()
databasemenu.add_command(label="Close")

optionmenu = Menu(menubar,tearoff = 0)
optionmenu.add_command(label="Add Products",command = lambda: window_to_add())
optionmenu.add_command(label="Edit Products",command = lambda: window_to_edit())
optionmenu.add_separator()
optionmenu.add_command(label="Delete Products",command = lambda: window_to_delete())

menubar.add_cascade(label="DataBase", menu=databasemenu)
menubar.add_cascade(label="Options", menu=optionmenu)


# SEARCH BAR (WILL HAVE FILTER,SEARCH PRODUCTS OF DATABASE ETC) (this will serve as consulter) (as defult it will say CONSULT PRODUCT )
img = Image.open('C:\\Users\\Pablo\\Desktop\\programacion\\PROGRAMACION CON PYTHON\\proyectos propios\\Inventary\\M_glass.png')
img = img.resize((30,30))
img = ImageTk.PhotoImage(img)

search = Entry(window,width=41).place(x=465, y=33,height=20)
consult_button = Button(window,image = img,bg= "white",command = lambda: consult_products())
consult_button.place(x=720,y=25)

window.mainloop()