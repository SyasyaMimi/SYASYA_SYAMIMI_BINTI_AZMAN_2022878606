import tkinter as tk
from tkinter import ttk
import mysql.connector

# CONNECT MYSQL DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel_management"
)

# CURSOR OBJECT TO EXECUTE SQL QUERIES
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    Type_Of_Package = (Type_of_Package_combobox.get())
    Packs = int(Packs_entry.get())
    Customer_Name = Customer_Name_entry.get()
    contact_number = Contact_Number_entry.get()
    Ic_number = Ic_Number_entry.get()


 #  the price below is to defined the value from your selections
    Package_prices = {
        "Package A": 650,
        "Package B": 500,
        "Package C": 750,
            
    }
    
    # Calculate the total price. This will be derived from your selection (Package, Pack).
    Total_Price = (Package_prices[Type_Of_Package] * Packs)
    print(Total_Price)

    # INSERT DATA TO DATABASE
    sql = "INSERT INTO hotel_booking (Type_Of_Package, Packs, Customer_Name, Contact_number, Ic_number, Total_Price) VALUES (%s, %s, %s,%s,%s,%s)"
    val = (Type_Of_Package, Packs, Customer_Name, contact_number, Ic_number, Total_Price)
    mycursor.execute(sql, val)
    mydb.commit()

    #Function to collect data
    output_label.configure(text=f"Type Of Package: {Type_Of_Package}, Family Packs: {Packs}, Customer Full Name {Customer_Name}, Contact Number: {contact_number}, Ic Number: {Ic_number}, Total Package: {Total_Price}")
    
    
 # Your Main window, You need to have the title, geometry
root = tk.Tk()
root.title("Hotel Management")
root.geometry('600x800') 

frame = tk.Frame(root)
frame.pack()

 # Page Title
label = tk.Label(root, text='HOTEL BOOKING', font=("ARIAL",14, "bold"))
label.pack(ipadx=10, ipady=10)
  
# Prices List by using textbox
prices_text = tk.Text(root, height=10, width=45)
prices_text.pack(pady=20)
    
 # The defined list by using pricebox
prices_text.insert(tk.END, "Package & Prices:\n\n")
prices_text.insert(tk.END, "Package A: Spa and sauna \nPrice: RM650\n\n")
prices_text.insert(tk.END, "Package B: Small kitchen \nPrice: RM500\n\n")
prices_text.insert(tk.END, "Package C: Swimming pool and cuisine \nPrice: RM700\n\n")
prices_text.configure(state='disabled')  

frame = tk.Frame(root)
frame.pack()
    

Hotel_Booking_frame=tk.LabelFrame(frame, text="Booking Information",font=("arial",10,"bold"))
Hotel_Booking_frame.grid(row=7, column=0)


Type_of_Package=tk.Label(Hotel_Booking_frame, text="Type Of Package")
Type_of_Package_combobox=ttk.Combobox(Hotel_Booking_frame, values=["Package A", "Package B", "Package C"])
Type_of_Package.grid(row=9, column=0)
Type_of_Package_combobox.grid(row=9, column=1)

Packs_label=tk.Label(Hotel_Booking_frame, text="Family Pack")
Packs_label.grid(row=11, column=0)
Packs_entry=tk.Entry(Hotel_Booking_frame)
Packs_entry.grid(row=11, column=1)

Customer_Name_label=tk.Label(Hotel_Booking_frame, text="Customer Full Name")
Customer_Name_label.grid(row=13, column=0)
Customer_Name_entry=tk.Entry(Hotel_Booking_frame)
Customer_Name_entry.grid(row=13, column=1)

Contact_Number_label=tk.Label(Hotel_Booking_frame, text="Phone Number")
Contact_Number_label.grid(row=15, column=0)
Contact_Number_entry=tk.Entry(Hotel_Booking_frame)
Contact_Number_entry.grid(row=15, column=1)

Ic_Number_label=tk.Label(Hotel_Booking_frame, text="Ic Number")
Ic_Number_label.grid(row=17, column=0)
Ic_Number_entry=tk.Entry(Hotel_Booking_frame)
Ic_Number_entry.grid(row=17, column=1)


for widget in Hotel_Booking_frame.winfo_children():
    widget.grid_configure(padx=15, pady=10)

# Save Button and calculate
save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output label
label = tk.Label(root, text='Total Package', font=("Arial",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()