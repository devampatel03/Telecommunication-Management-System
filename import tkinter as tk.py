# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# import mysql.connector as sqltor

# # Connecting To MySQL Database
# mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
# if not mycon.is_connected():
#     print("Error connecting to MySQL database")
# cursor = mycon.cursor()

# # Define functions
# def display_customer_details():
#     query = "SELECT * FROM customer"
#     cursor.execute(query)
#     data = cursor.fetchall()
#     for row in data:
#         print(row)

# def add_customer():
#     name = name_entry.get()
#     ph_no = int(ph_no_entry.get())
#     sim_type = sim_type_var.get()
#     plan = plan_entry.get()
#     fixed_rental = int(fixed_rental_entry.get())
#     query = f"INSERT INTO customer(Name, Ph_No, Sim_Type, Plans, Fixed_rental) VALUES ('{name}', {ph_no}, '{sim_type}', '{plan}', {fixed_rental})"
#     cursor.execute(query)
#     mycon.commit()
#     messagebox.showinfo("Success", "Customer added successfully")

# # Create GUI window
# root = tk.Tk()
# root.title("Telecom Database Management System")
# root.geometry("400x300")
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

# # Add customer form
# form_frame = ttk.Frame(root)
# form_frame.pack(pady=10)

# name_label = ttk.Label(form_frame, text="Name:")
# name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# name_entry = ttk.Entry(form_frame)
# name_entry.grid(row=0, column=1, padx=5, pady=5)

# ph_no_label = ttk.Label(form_frame, text="Phone Number:")
# ph_no_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
# ph_no_entry = ttk.Entry(form_frame)
# ph_no_entry.grid(row=1, column=1, padx=5, pady=5)

# sim_type_label = ttk.Label(form_frame, text="SIM Type:")
# sim_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
# sim_type_var = tk.StringVar()
# sim_type_combobox = ttk.Combobox(form_frame, textvariable=sim_type_var, values=["Prepaid", "Postpaid"])
# sim_type_combobox.grid(row=2, column=1, padx=5, pady=5)

# plan_label = ttk.Label(form_frame, text="Plan:")
# plan_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
# plan_entry = ttk.Entry(form_frame)
# plan_entry.grid(row=3, column=1, padx=5, pady=5)

# fixed_rental_label = ttk.Label(form_frame, text="Fixed Rental:")
# fixed_rental_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
# fixed_rental_entry = ttk.Entry(form_frame)
# fixed_rental_entry.grid(row=4, column=1, padx=5, pady=5)

# add_btn = ttk.Button(root, text="Add Customer", command=add_customer)
# add_btn.pack(pady=10)

# root.mainloop()



# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import messagebox
# # import mysql.connector as sqltor

# # # Connecting To MySQL Database
# # mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
# # if not mycon.is_connected():
# #     print("Error connecting to MySQL database")
# # cursor = mycon.cursor()

# # # Define function to display customer details in a table
# # def display_customer_details():
# #     query = "SELECT * FROM customer"
# #     cursor.execute(query)
# #     data = cursor.fetchall()
# #     for row in data:
# #         tree.insert('', tk.END, values=row)

# # # Create GUI window
# # root = tk.Tk()
# # root.title("Telecom Database Management System")
# # root.geometry("600x400")
# # root.configure(bg="#f0f0f0")

# # # Styling
# # style = ttk.Style()
# # style.theme_use("clam")
# # style.configure("TButton", background="#007bff", foreground="white", padding=5, font=("Helvetica", 10))
# # style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
# # style.configure("TEntry", background="white", font=("Helvetica", 10))

# # # Add customer details button
# # view_btn = ttk.Button(root, text="View Customer Details", command=display_customer_details)
# # view_btn.pack(pady=10)

# # # Create Treeview for displaying customer details
# # columns = ('Name', 'Phone Number', 'SIM Type', 'Plan', 'Fixed Rental')
# # tree = ttk.Treeview(root, columns=columns, show='headings')
# # for col in columns:
# #     tree.heading(col, text=col)
# # tree.pack(fill='both', expand=True)

# # root.mainloop()





# # from flask import Flask, render_template
# # import mysql.connector as sqltor

# # app = Flask(__name__)

# # # Connect to MySQL Database
# # mycon = sqltor.connect(host="127.0.0.1", user="root", passwd="mysql", database="tele_dbms")
# # if not mycon.is_connected():
# #     print("Error connecting to MySQL database")
# # cursor = mycon.cursor()

# # # Define routes
# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/customer_details')
# # def customer_details():
# #     query = "SELECT * FROM customer"
# #     cursor.execute(query)
# #     customer_data = cursor.fetchall()
# #     return render_template('customer_details.html', customer_data=customer_data)

# # # Add more routes for other functionalities as needed

# # if __name__ == '__main__':
# #     app.run(debug=True)


# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="mysql",
#     database="tele_dbms"
# )

# # Function to handle login for both user and admin
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     if username == "user" and password == "userpass":
#         user_menu()
#     elif username == "admin" and password == "adminpass":
#         admin_menu()
#     else:
#         messagebox.showerror("Error", "Invalid username or password")

# # Function to display user menu
# def user_menu():
#     window.destroy()  # Close login window
#     user_window = tk.Tk()
#     user_window.title("User Menu")

#     # Add functionality buttons
#     def get_plan_details():
#         cursor = conn.cursor()
#         # Your logic to fetch plan details based on user data
#         cursor.close()

#     plan_details_button = tk.Button(user_window, text="My Plan Details", command=get_plan_details)
#     plan_details_button.pack()

#     # Add other functionality buttons here

#     user_window.mainloop()

# # Function to display admin menu
# def admin_menu():
#     window.destroy()  # Close login window
#     admin_window = tk.Tk()
#     admin_window.title("Admin Menu")

#     # Add functionality buttons
#     def add_new_customer():
#         cursor = conn.cursor()
#         # Your logic to add a new customer
#         cursor.close()

#     add_customer_button = tk.Button(admin_window, text="Add New Customer", command=add_new_customer)
#     add_customer_button.pack()

#     # Add other functionality buttons here

#     admin_window.mainloop()

# # GUI setup for login
# window = tk.Tk()
# window.title("Login")

# # Create labels and entry fields for username and password
# username_label = tk.Label(window, text="Username:")
# username_label.grid(row=0, column=0, padx=10, pady=5)
# username_entry = tk.Entry(window)
# username_entry.grid(row=0, column=1, padx=10, pady=5)

# password_label = tk.Label(window, text="Password:")
# password_label.grid(row=1, column=0, padx=10, pady=5)
# password_entry = tk.Entry(window, show="*")
# password_entry.grid(row=1, column=1, padx=10, pady=5)

# # Create login button
# login_button = tk.Button(window, text="Login", command=login)
# login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# window.mainloop()
import sys
import mysql.connector

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class UserLoginWidget(QWidget):
    def __init__(self, conn, parent=None):
        super().__init__(parent)
        self.conn = conn

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("User Login")
        
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.handle_login)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Call the user_login function passing the username, password, and conn
        # Display appropriate messages or open the user's functionality window based on the return value
        # For simplicity, let's assume the user_login function returns True if login is successful
        
        # Example:
        # success = user_login(username, password, self.conn)
        # if success:
        #     self.open_user_functionality_window()
        # else:
        #     self.show_error_message("Invalid username or password")

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="mysql",
            database="tele_dbms"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None
def main():
    app = QApplication(sys.argv)
    conn = connect_to_database()

    if conn is None:
        sys.exit()

    user_login_widget = UserLoginWidget(conn)
    user_login_widget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
