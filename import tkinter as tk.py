import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sqltor

# Connecting To MySQL Database
mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
if not mycon.is_connected():
    print("Error connecting to MySQL database")
cursor = mycon.cursor()

# Define functions
def display_customer_details():
    query = "SELECT * FROM customer"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)

def add_customer():
    name = name_entry.get()
    ph_no = int(ph_no_entry.get())
    sim_type = sim_type_var.get()
    plan = plan_entry.get()
    fixed_rental = int(fixed_rental_entry.get())
    query = f"INSERT INTO customer(Name, Ph_No, Sim_Type, Plans, Fixed_rental) VALUES ('{name}', {ph_no}, '{sim_type}', '{plan}', {fixed_rental})"
    cursor.execute(query)
    mycon.commit()
    messagebox.showinfo("Success", "Customer added successfully")

# Create GUI window
root = tk.Tk()
root.title("Telecom Database Management System")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#007bff", foreground="white", padding=5, font=("Helvetica", 10))
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TEntry", background="white", font=("Helvetica", 10))

# Add customer details button
view_btn = ttk.Button(root, text="View Customer Details", command=display_customer_details)
view_btn.pack(pady=10)

# Add customer form
form_frame = ttk.Frame(root)
form_frame.pack(pady=10)

name_label = ttk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ph_no_label = ttk.Label(form_frame, text="Phone Number:")
ph_no_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
ph_no_entry = ttk.Entry(form_frame)
ph_no_entry.grid(row=1, column=1, padx=5, pady=5)

sim_type_label = ttk.Label(form_frame, text="SIM Type:")
sim_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
sim_type_var = tk.StringVar()
sim_type_combobox = ttk.Combobox(form_frame, textvariable=sim_type_var, values=["Prepaid", "Postpaid"])
sim_type_combobox.grid(row=2, column=1, padx=5, pady=5)

plan_label = ttk.Label(form_frame, text="Plan:")
plan_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
plan_entry = ttk.Entry(form_frame)
plan_entry.grid(row=3, column=1, padx=5, pady=5)

fixed_rental_label = ttk.Label(form_frame, text="Fixed Rental:")
fixed_rental_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
fixed_rental_entry = ttk.Entry(form_frame)
fixed_rental_entry.grid(row=4, column=1, padx=5, pady=5)

add_btn = ttk.Button(root, text="Add Customer", command=add_customer)
add_btn.pack(pady=10)

root.mainloop()



# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# import mysql.connector as sqltor

# # Connecting To MySQL Database
# mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
# if not mycon.is_connected():
#     print("Error connecting to MySQL database")
# cursor = mycon.cursor()

# # Define function to display customer details in a table
# def display_customer_details():
#     query = "SELECT * FROM customer"
#     cursor.execute(query)
#     data = cursor.fetchall()
#     for row in data:
#         tree.insert('', tk.END, values=row)

# # Create GUI window
# root = tk.Tk()
# root.title("Telecom Database Management System")
# root.geometry("600x400")
# root.configure(bg="#f0f0f0")

# # Styling
# style = ttk.Style()
# style.theme_use("clam")
# style.configure("TButton", background="#007bff", foreground="white", padding=5, font=("Helvetica", 10))
# style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
# style.configure("TEntry", background="white", font=("Helvetica", 10))

# # Add customer details button
# view_btn = ttk.Button(root, text="View Customer Details", command=display_customer_details)
# view_btn.pack(pady=10)

# # Create Treeview for displaying customer details
# columns = ('Name', 'Phone Number', 'SIM Type', 'Plan', 'Fixed Rental')
# tree = ttk.Treeview(root, columns=columns, show='headings')
# for col in columns:
#     tree.heading(col, text=col)
# tree.pack(fill='both', expand=True)

# root.mainloop()





# from flask import Flask, render_template
# import mysql.connector as sqltor

# app = Flask(__name__)

# # Connect to MySQL Database
# mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
# if not mycon.is_connected():
#     print("Error connecting to MySQL database")
# cursor = mycon.cursor()

# # Define routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/customer_details')
# def customer_details():
#     query = "SELECT * FROM customer"
#     cursor.execute(query)
#     customer_data = cursor.fetchall()
#     return render_template('customer_details.html', customer_data=customer_data)

# # Add more routes for other functionalities as needed

# if __name__ == '__main__':
#     app.run(debug=True)


