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
    "password": "1234",
    "database": "inventary"
}

connection = mysql.connector.connect(**dbConnect)
cursor = connection.cursor()

# THIS FUNCTION SEARCH THE EXISTING CODES IN THE DATABASE
def search_code():
    cursor.execute("SELECT code FROM inventary")
    codes = cursor.fetchall()
    code_table = []

    for c in codes:
        str_code = "".join(c)
        code_table.append(str_code)

    return code_table

# WINDOW AND OPTIONS FOT ADD A NEW PRODUCTS
def add_products(code, product, provider, kind, description, price, quantity, window_add_products):
    code_table = search_code()  # Instance of the search code function

    # Get values for window_to_add
    get_code = str(code.get()).upper()
    get_product = product.get()
    get_provider = provider.get()
    get_kind = kind.get()
    get_description = str(description.get())
    get_price = (price.get())
    get_quantity = (quantity.get())

    data_obtained = [get_code,get_product,get_provider,get_kind,get_description,get_price,get_quantity]

    # Throws an error message when an existing code is placed in the program
    # Even so, I need to put something so that it does not launch the error in console
    if get_code in code_table:
        messagebox.showerror("ERROR", "The product code already exists, use another code", icon = "error")
        window_add_products.lift()  # Put the window in front

    # Avoid errors of programs
    if (len(get_code) or len(get_product) or len(get_provider) or len(get_kind) or len(get_description) or len(get_price) or len(get_quantity)) == 0:
        messagebox.showerror("ERROR","Complete empty spaces",icon="error")

    elif (len(get_code) and len(get_product) and len(get_provider) and len(get_kind) and len(get_description) and len(get_price) and len(get_quantity)) == 0:
        messagebox.showerror("ERROR","You cangt leave empty spaces",icon="error")

    elif (len(get_code) < 5 or len(get_code) > 8):
        messagebox.showerror("ERROR", "The code must be between 5 and 8 characters", icon="error")

    else:
        # Upload data to database
        cursor.execute(f"INSERT INTO inventary VALUES(%s,%s,%s,%s,%s,%s,%s)", data_obtained)
        connection.commit()

        # Messagebox when program finish
        messagebox.showinfo("","Products added succesfully")

        # Clear entry widgets
        code.delete(0, END)
        product.delete(0, END)
        provider.delete(0, END)
        kind.delete(0, END)
        description.delete(0, END)
        price.delete(0, END)
        quantity.delete(0, END)
    
    # Put the window in front
    window_add_products.lift()

def window_to_add():
    window_add_products = Toplevel(window)
    width = 450
    height = 450

    # Place the window in the middle
    x = (window_add_products.winfo_screenwidth() // 2) - (width // 2)
    y = (window_add_products.winfo_screenheight() // 2) - (height // 2)

    window_add_products.geometry(f"{width}x{height}+{x}+{y}")
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

    code_Label = Label (window_add_products, text ="CODE:")
    code_Label.place(x=10,y=260)

    price_Label = Label(window_add_products,text = "PRICE:")
    price_Label.place(x=10,y=320)

    quantity_Label = Label(window_add_products,text = "QUANTITY:")
    quantity_Label.place(x=10,y=380)

    # Stringvar
    product_Label = StringVar()
    provider_Label = StringVar()
    kind_Label = StringVar()
    description_Label = StringVar()
    price_Label = StringVar()
    quantity_Label = StringVar()
    code_Label = StringVar()

    # Entry
    product_Entry = Entry(window_add_products,textvariable = product_Label,width = 30)
    product_Entry.place(x=10,y=40)

    provider_Entry = Entry(window_add_products,textvariable = provider_Label,width = 30)
    provider_Entry.place(x=10,y=100)

    kind_Entry = Entry(window_add_products,textvariable = kind_Label,width = 30)
    kind_Entry.place(x=10,y=160)

    description_Entry = Entry(window_add_products,textvariable = description_Label,width = 30)
    description_Entry.place(x=10,y=220)

    code_Entry = Entry(window_add_products,textvariable = code_Label,width = 30)
    code_Entry.place(x=10,y=280)

    price_Entry = Entry(window_add_products,textvariable = price_Label,width = 30)
    price_Entry.place(x=10,y=340)

    quantity_Entry = Entry(window_add_products,textvariable = quantity_Label,width = 30)
    quantity_Entry.place(x=10,y=400)

    # Confirm button
    confir_button = Button(window_add_products,text= "CONFIRM",bg= "green",command = lambda:add_products(code_Entry,product_Entry,provider_Entry,kind_Entry,description_Entry,price_Entry,quantity_Entry,window_add_products))
    confir_button.place(x=270,y=410)


# WINDOW AND OPTIONS FOR DELETE PRODUCTS

# Delete button options
def delete_button(code, window_delete_by_code):
    get_code = str(code.get()).upper()
    code_table = search_code()
    window_del_by_code = window_delete_by_code # window instance

    # In case the user leaves the space empty
    if len (get_code) <= 0:
        messagebox.showerror("ERROR", "Complete empty spaces", icon="error")

    # Condition that serves to eliminate the existing codes and show error when it does not exist
    elif get_code in code_table:
        cursor.execute(f'delete from inventary where code = "{get_code}"')
        connection.commit()
        messagebox.showinfo("","product remove successfully")

        # Clear entry widgets
        code.delete(0, END)

    else:
        messagebox.showerror("ERROR", "The code doesn't exist", icon="error")

    window_del_by_code.lift()  # Put the window in front

# Function to remove products by code
def delete_by_code(window_del_products):

    window_del_by_code = Toplevel(window)
    width = 250
    height = 100
    
    # Destroy the main delete window
    window_del_products.destroy()

    # Place the window in the middle
    x = (window_del_by_code.winfo_screenwidth() // 2) - (width // 2)
    y = (window_del_by_code.winfo_screenheight() // 2) - (height // 2)

    window_del_by_code.geometry(f"{width}x{height}+{x}+{y}")
    window_del_by_code.resizable(False, False)

    # Label for the CODE
    code_label = Label(window_del_by_code, text= "Enter the product code")
    code_label.place(x=18,y=20)

    # Stringvar
    code_label = StringVar()

    # Entry for the ICODE
    code_entry = Entry(window_del_by_code,textvariable = code_label,width=10) 
    code_entry.place(x=20,y=50)

    # Confirmation button product removal
    code_button = Button(window_del_by_code,text="Delete",bg="#01DF01",command = lambda: delete_button(code_entry, window_del_by_code))
    code_button.place(x=140,y=46)

# Delete all function
def delete_all(window_del_products):
    window_del_products.iconify() # Hide the window

    first_message = messagebox.askyesno("", "you are about to delete all the information from the database, do you want to continue?", icon="warning")
    if first_message == True:
        second_message = messagebox.askokcancel("","click on accept to delete the information from the database",icon= "error")
        if second_message == True:
            cursor.execute("truncate table inventary")
            connection.commit()
            messagebox.showinfo("", "information successfully removed")
            window_del_products.destroy() 

        else:
            window_del_products.deiconify() # Reappear window
    else:
        window_del_products.deiconify() # Reappear window


def window_to_delete():
    # I would like an option that when the X (exit button of the windows) is given, the window reappears with the option to delete information
    window_del_products = Toplevel(window)
    width = 250
    height = 150

    # Place the window in the middle
    x = (window_del_products.winfo_screenwidth() // 2) - (width // 2)
    y = (window_del_products.winfo_screenheight() // 2) - (height // 2)

    window_del_products.geometry(f"{width}x{height}+{x}+{y}")
    window_del_products.resizable(False, False)

    del_code_button = Button(window_del_products, text= "Delete by code", bg= "#01DF01", command = lambda:delete_by_code(window_del_products))
    del_code_button.place(x=87,y= 40)

    del_all_button = Button(window_del_products, text="Delete All", bg="#FF0040", command=lambda: delete_all(window_del_products))
    del_all_button.place(x=100, y=100)

#WINDOW AND OPTIONS FOR EDIT PRODUCTS

# Ask id of the program to edit, when the user put Id must appear boxes with the information to edit.
# create a entry box in the top of window for introduce ID
# under box, create new boxes where upload the informarion of that ID

def window_to_edit():
    print("Edit products")

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


# Create 2 entry to the app where will receive the database and bill (database label be long and bills label be short and more with)
see_database = Entry(window,width= 70).place(x=10,y=30,height=600)
see_bill = Entry(window,width = 50).place(x=465,y=231,height=400)

scroll_database = Scrollbar(window).place(x=430,y=30,height = 600)
scroll_bill = Scrollbar(window).place(x=765,y=231,height = 400)


# CREATE BILL BUTTONS
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
img = Image.open('C:\\Users\\paibl\\OneDrive\\Escritorio\\programacion\\PROGRAMACION CON PYTHON\\proyectos propios\\Inventary\\M_glass.png')
img = img.resize((30,30))
img = ImageTk.PhotoImage(img)

search = Entry(window,width=41).place(x=465, y=33,height=20)
consult_button = Button(window,image = img,bg= "white",command = lambda: consult_products())
consult_button.place(x=720,y=25)

window.mainloop()
