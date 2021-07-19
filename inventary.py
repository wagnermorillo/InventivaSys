from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# https://stackoverflow.com/questions/31815007/change-icon-for-tkinter-messagebox (This will serve for the moment to change the tkinter icon for something mine)

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


# COMMAND FOR ADD A NEW PRODUCTS TO DATABASE
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
    if get_code in code_table:
        messagebox.showerror("ERROR", "The product code already exists, use another code", icon = "error")
        window_add_products.lift()  # Put the window in front

    # Inside this ELSE is everything necessary to insert the values into the database
    else:
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


#WINDOW AND OPTIONS TO ADD PRODUCTS TO DATABASE
# principal window to add products to database
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

    # This function serves to destroy the current window when the X is given and in turn open the previous window
    def X_options():
        window_del_by_code.destroy()
        window_to_delete()

    window_del_by_code = Toplevel(window) 
    width = 250
    height = 100
    window_del_by_code.protocol("WM_DELETE_WINDOW",X_options)

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

# principal window to delete productos from database
def window_to_delete():
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


# WINDOW AND OPTIONS FOR EDIT PRODUCTS IN DATABASE
# Function used to erase the information within the entrys in the window and unlock the code button
def clear_information(entry_button, update_button, first_code,product_code,product,provider,kind,description,price,quantity):
    entry_button.config(state= "normal") #Enable Code button again / entry_button["state"] = "normal"
    update_button.config(state= "disabled")

    # Remove information from fields
    first_code.delete(0,END)
    product_code.delete(0,END)
    product.delete(0,END)
    provider.delete(0,END)
    kind.delete(0,END)
    description.delete(0, END)
    price.delete(0, END)
    quantity.delete(0, END)
    
    product_code.config(state="disabled")
    product.config(state="disabled")
    provider.config(state="disabled")
    kind.config(state="disabled")
    description.config(state="disabled")
    price.config(state="disabled")
    quantity.config(state="disabled")

# Function connected to the code button, it has all the functions of the same 
def edit_search_info(window_edit_products,entry_button,update_button,first_code,product_code,product,provider,kind,description,price,quantity):
    #Activate the entry fields to be able to write
    product_code.config(state= "normal")
    product.config(state= "normal")
    provider.config(state= "normal")
    kind.config(state= "normal")
    description.config(state= "normal")
    price.config(state= "normal")
    quantity.config(state= "normal")

    codes = search_code()
    code = str(first_code.get()).upper()

    if len(code) < 1:
        messagebox.showerror("ERROR", "complete empty spaces", icon="error")
        window_edit_products.lift()

    elif code in codes: # Main program options
        cursor.execute(f"SELECT * FROM inventary WHERE code = '{code}'")
        info = cursor.fetchall()

        for i in info: # The for will serve to search index by index the data to insert in the entry
            product_code.insert(END,i[0])
            product.insert(END,i[1])
            provider.insert(END,i[2])
            kind.insert(END,i[3])
            description.insert(END,i[4])
            price.insert(END,i[5])
            quantity.insert(END,i[6])

        entry_button.config(state="disabled")  #Block Code button / entry_button["state"] = "disabled" 
        update_button.config(state="normal")

    else:
        messagebox.showerror("ERROR", "The code doesn't exist", icon="error")
        window_edit_products.lift()

# Function that sends the updated information to the database
def update_information(window_edit_products,entry_button,update_button,first_code,product_code,product,provider,kind,description,price,quantity):
    get_first_code = str(first_code.get()).upper()
    get_product_code = str(product_code.get()).upper()
    get_product = str(product.get())
    get_provider = str(provider.get())
    get_kind = str(kind.get())
    get_description = str(description.get())
    get_price = price.get()
    get_quantity = (quantity.get())

    cursor.execute(F"UPDATE inventary SET code ='{get_product_code}',product='{get_product}',provider='{get_provider}',kind='{get_kind}',description='{get_description}',price={get_price},quantity={get_quantity} WHERE code = '{get_first_code}'")
    connection.commit()
    messagebox.showinfo("", "Successful data update",icon ="info")
    clear_information(entry_button, update_button, first_code, product_code, product, provider,kind,description,price,quantity)

    window_edit_products.lift()  # Reappear window

# Principal window for edit products of database
def window_to_edit():
    window_edit_products = Toplevel(window)
    width = 500
    height = 275
    # Place the window in the middle
    x = (window_edit_products.winfo_screenwidth() // 2) - (width // 2)
    y = (window_edit_products.winfo_screenheight() // 2) - (height //2)

    window_edit_products.geometry(f"{width}x{height}+{x}+{y}")
    window_edit_products.resizable(False,False)

    # Title Label
    code_label = Label(window_edit_products,text= "CODE").place(x=50,y=80)
    product_label = Label(window_edit_products,text="PRODUCT").place(x=157,y=80)
    provider_label = Label(window_edit_products, text="PROVIDER").place(x=276,y=80)
    kind_label = Label(window_edit_products, text="KIND").place(x=410,y=80)
    description_label = Label(window_edit_products, text="DESCRIPTION").place(x=88, y=155)
    price_label = Label(window_edit_products, text="PRICE").place(x=288,y=155)
    quantity_label = Label(window_edit_products, text="QUANTITY").place(x=395, y=155)

    # Stringvar
    code_stringvar = StringVar()
    code_label = StringVar()
    product_label = StringVar()
    provider_label = StringVar()
    kind_label = StringVar()
    description_label = StringVar()
    price_label = StringVar()
    quantity_label = StringVar()

    # Entry First row
    first_code_entry = Entry(window_edit_products,textvariable = code_stringvar,width =15)
    first_code_entry.place(x=20, y=30)

    code_entry = Entry(window_edit_products,state="disabled",textvariable = code_label, width =15)
    code_entry.place(x=20, y=100)

    product_entry = Entry(window_edit_products,state="disabled",textvariable= product_label,width =15)
    product_entry.place(x=140, y=100)

    provider_entry = Entry(window_edit_products,state="disabled",textvariable= provider_label, width=15)
    provider_entry.place(x=260, y=100)

    kind_entry = Entry(window_edit_products,state= "disabled",textvariable= kind_label, width=15)
    kind_entry.place(x=380, y=100)

    #Entry Second row
    description_entry = Entry(window_edit_products,state="disabled",textvariable=description_label,width=35)
    description_entry.place(x=20, y=175)

    price_entry = Entry(window_edit_products,state="disabled",textvariable= price_label, width=15)
    price_entry.place(x=260, y=175)

    quantity_entry = Entry(window_edit_products,state="disabled",textvariable= quantity_label, width=15)
    quantity_entry.place(x=380, y=175)
    
    # Buttons
    first_code_button = Button(window_edit_products, text="CODE", bg="#01DF01", command = lambda:edit_search_info(window_edit_products,first_code_button,update_button,first_code_entry,code_entry,product_entry,provider_entry,kind_entry,description_entry,price_entry,quantity_entry))
    first_code_button.place(x=125,y=27)

    clear_button = Button(window_edit_products,text="CLEAR",bg="red",command = lambda:clear_information(first_code_button,update_button,first_code_entry,code_entry,product_entry,provider_entry,kind_entry,description_entry,price_entry,quantity_entry))
    clear_button.place(x=180,y=27)

    update_button = Button(window_edit_products, text="UPDATE",state= "disabled",bg="#01DF01",command = lambda:update_information(window_edit_products,first_code_button,update_button,first_code_entry,code_entry,product_entry,provider_entry,kind_entry,description_entry,price_entry,quantity_entry))
    update_button.place(x=420,y=225)

def consult_products():
    print("consult")

def show_products():
    print("Show")

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

# I need to make the scrollbar work correctly, for that first I want to see the data, to see if it is fixed, if not then I will try with the rowspan and columspan functions so that the movement is possible.
# I would like the columspan and rowspan to work with the number of cells that the database has and so that all the information is seen, I will confirm this later

# Another idea that I have is, put a canvas or an entry behind the listbox, and that it expands to the total size of the entry and so it will grow and decrease according to, and when no more information can be seen, the scrollbar would be used

# Create 2 entry to the app where will receive the database and bill (database label be long and bills label be short and more with)
see_database = Listbox(window,width = 70,height = 600)
see_database.place(x=10,y=30) #Entry(window,width= 70).place(x=10,y=30,height=600)

see_bill = Listbox(window,width=50,height=400)
see_bill.place(x=465,y=231) #Entry(window,width = 50).place(x=465,y=231,height=400)

scroll_database = Scrollbar(window)
scroll_database.place(x=430,y=30,height = 600)

scroll_bill = Scrollbar(window)
scroll_bill.place(x=765,y=231,height = 400)

#in those 4 lines of code, I configure the scrollbar to work according to the list
see_database.configure(yscrollcommand= scroll_database.set)
see_bill.configure(yscrollcommand= scroll_bill.set)

scroll_database.configure(command= see_database.yview)
scroll_bill.configure(command= see_bill.yview)

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