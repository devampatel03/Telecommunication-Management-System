

import mysql.connector
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
    
# Function to get user's plan details
def get_plan_details(customer,conn):
    
    cursor = conn.cursor()
    if customer['Sim_type'] == 'Prepaid':
        query = "SELECT * FROM plans WHERE Plan_No = %s"
        cursor.execute(query, (customer['Plan_no']))
        plan = cursor.fetchone()
        print("           Your prepaid plan details:")
        print("Plan No:", plan[0])
        print("Price:", plan[1])
        print("Data:", plan[2])
        print("Calls:", plan[3])
        print("SMS:", plan[4])
        print("Validity:", plan[5])
        print("Other Benefits:", plan[6])
        print("\n")
    elif customer['Sim_type'] == 'Postpaid':
        query = "SELECT * FROM billing WHERE Name = %s AND Ph_No = %s"
        cursor.execute(query, (customer['Name'], customer['Ph_No']))
        billing_details = cursor.fetchone()
        print("            Your billing details:")
        print("Usage Rs:", billing_details[2])
        print("Fixed Rental Rs:", billing_details[3])
        print("Total GST:", billing_details[4])
        print("Previous Due:", billing_details[5])
        print("Total Bill:", billing_details[6])
        print("\n")
    cursor.close()

# Function to recharge user's mobile number
def recharge_mobile(customer,conn):
    cursor = conn.cursor()
    mobile_number = customer['Ph_No']
    
    if customer['Sim_type'] == 'Prepaid':
        new_plan_no = str(input("Enter new plan number: "))
    elif customer['Sim_type'] == 'Postpaid':
        recharge_amount = float(input("Enter recharge amount: "))

    if recharge_amount <= 0:
        print("Invalid recharge amount. Please enter a valid amount.")
        return
    # Update user's balance in the database (for prepaid users) or add a new invoice (for postpaid users)
    if customer['Sim_type'] == 'Prepaid':
        query = "UPDATE customer SET Plan_No = %s WHERE Ph_No = %s"
        cursor.execute(query, (new_plan_no, mobile_number))
    elif customer['Sim_type'] == 'Postpaid':
        query="SELECT * from invoice"
        cursor.execute(query)
        invoices=cursor.fetchall()
        invoice_no=invoices[-1][0]+1
        query = "INSERT INTO invoice (Invoice_No,Name, Ph_No, Invoice_Date, Total_Payment, Payment_Mode) VALUES (%s,%s, %s, CURDATE(), %s, %s)"
        cursor.execute(query, (invoice_no,customer['Name'], mobile_number, recharge_amount, 'Online Payment'))
    conn.commit()
    print("Recharge successful!")
    print("\n")
    cursor.close()

# Function to get details of all prepaid plans available
def get_prepaid_plans(customer,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM plans"
    cursor.execute(query)
    prepaid_plans = cursor.fetchall()
    print("          Prepaid Plans Available:")
    for plan in prepaid_plans:
        print("Plan No:", plan[0])
        print("Price:", plan[1])
        print("Data:", plan[2])
        print("Calls:", plan[3])
        print("SMS:", plan[4])
        print("Validity:", plan[5])
        print("Other Benefits:", plan[6])
        print("\n")
    cursor.close()

# Function to get invoice history
def get_invoice_history(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM invoice WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    invoice_history = cursor.fetchall()
    print("           Your invoice history:")
    for invoice in invoice_history:
        print("Invoice No:", invoice[0])
        print("Invoice Date:", invoice[4])
        print("Total Payment:", invoice[5])
        print("Payment Mode:", invoice[6])
        print("\n")
    cursor.close()

# Function to get recharge history
def get_recharge_history(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM recharge WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    recharge_history = cursor.fetchall()
    print("             Your recharge history:")
    for recharge in recharge_history:
        print("Recharge ID:", recharge[0])
        print("Recharge Date:", recharge[4])
        print("Recharge Amount:", recharge[7])
        print("Payment Mode:", recharge[8])
        print("\n")
    cursor.close()

# Function to check data usage
def check_data_usage(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM data_usage WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    data_usage = cursor.fetchone()
    print("              Your data usage:")
    print("Session Start Time:", data_usage[2])
    print("Session End Time:", data_usage[3])
    print("Data Usage (GB):", data_usage[4])
    print("Remaining Data (GB):", data_usage[5])
    print("\n")
    cursor.close()

# Function to check call logs
def check_call_logs(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM call_records WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    call_logs = cursor.fetchall()
    print("               Your call logs:")
    for log in call_logs:
        print("Call Logs Per Day:", log[2])
        print("Call Received Hour Min:", log[3])
        print("Call Ended Hour Min:", log[4])
        print("Call Duration Hour Min:", log[5])
        print("Location of Phone Number:", log[6])
        print("\n")
    cursor.close()

# Function to get user's coupons
def get_coupons(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM coupon "
    cursor.execute(query)
    coupons = cursor.fetchall()
    print("               Your coupons:")
    for coupon in coupons:
        print("Coupon No:", coupon[0])
        print("Brand:", coupon[1])
        print("Price:", coupon[2])
        print("Valid Upto:", coupon[3])
        print("\n")
    cursor.close()

# Function to update user's profile
def update_profile(user,conn):
    cursor = conn.cursor()
    # Fetch user's current profile details
    query = "SELECT * FROM personal WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    current_profile = cursor.fetchone()
    print("                Current Profile Details:")
    print("Name:", current_profile[0])
    print("Phone Number:", current_profile[1])
    print("Alternate Phone Number:", current_profile[2])
    print("Address:", current_profile[3])
    print("Email ID:", current_profile[4])
    print("Date of Birth:", current_profile[5])
    print("Aadhaar Number:", current_profile[6])
    print("\n")
    # Ask user for updated details
    new_name = input("Enter new name (leave empty to keep current): ").strip() or current_profile[0]
    new_alt_ph_no = input("Enter new alternate phone number (leave empty to keep current): ").strip() or current_profile[2]
    new_address = input("Enter new address (leave empty to keep current): ").strip() or current_profile[3]
    new_email = input("Enter new email ID (leave empty to keep current): ").strip() or current_profile[4]
    new_dob = input("Enter new date of birth (YYYY-MM-DD) (leave empty to keep current): ").strip() or current_profile[5]
    # Update user's profile in the database
    query = "UPDATE personal SET Name = %s, Alt_Ph_No = %s, Address = %s, Email_ID = %s, DOB = %s WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (new_name, new_alt_ph_no, new_address, new_email, new_dob, user['Name'], user['Ph_No']))
    conn.commit()
    print("\n")
    print("Profile updated successfully!")
    print("\n")
    cursor.close()

# Function to view user's profile
def view_profile(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM personal WHERE Name = %s AND Ph_No = %s"
    cursor.execute(query, (user['Name'], user['Ph_No']))
    profile_details = cursor.fetchone()
    print("             Your Profile:")
    print("Name:", profile_details[0])
    print("Phone Number:", profile_details[1])
    print("Alternate Phone Number:", profile_details[2])
    print("Address:", profile_details[3])
    print("Email ID:", profile_details[4])
    print("Date of Birth:", profile_details[5])
    print("Aadhaar Number:", profile_details[6])
    print("\n")
    cursor.close()

# Function to get store information near user's address
def get_store_information(user,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM store WHERE Address = %s"
    cursor.execute(query, (user['Address'],))
    store_info = cursor.fetchall()
    print("                 Store Information Near Your Address:")
    for store in store_info:
        print("Store No:", store[0])
        print("Address:", store[1])
        print("City:", store[2])
        print("Contact No:", store[3])
        print("\n")

    cursor.close()

# Function to get user's raised tickets
def get_tickets(customer,conn):
    cursor = conn.cursor()
    query = "SELECT * FROM ticket WHERE Cust_ID = %s"
    cursor.execute(query, (customer['Cust_ID'],))
    tickets = cursor.fetchall()
    print("                  Your raised tickets:")
    for ticket in tickets:
        print("Ticket No:", ticket[0])
        print("Issue:", ticket[1])
        print("Date Raised:", ticket[3])
        print("Ticket Status:", ticket[4])
        print("\n")

    cursor.close()

# Function to add new customer (admin functionality)
def add_new_customer(conn):
    cursor = conn.cursor()
    print("                 Add New Customer:")
    query="SELECT * FROM customer "
    cursor.execute(query)
    customers=cursor.fetchall()
    cust_id=customers[-1][0]+1
    name = str(input("Enter customer name: "))
    ph_no = int(input("Enter customer phone number: "))
    alt_no = int(input("Enter customer's alternate phone number: "))
    address = str(input("Enter customer address: "))
    email = str(input("Enter customer email ID: "))
    dob = str(input("Enter customer date of birth (YYYY-MM-DD): "))
    aadhaar = int(input("Enter customer Aadhaar number: "))
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))
    sim_type = str(input("Enter SIM type (Prepaid/Postpaid): "))
    if (sim_type == 'Prepaid'):
        plan_no = str(input("Enter plan number "))
    else:
        plan_no = None
    fixed_rental = float(input("Enter fixed rental: "))
    # Perform validation checks if necessary
    query = "INSERT INTO personal (Name, Ph_No, Alt_Ph_No, Address, Email_ID, DOB, Aadhaar_No, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, ph_no, alt_no, address, email, dob, aadhaar, user_name, password))
    conn.commit()
    query = "INSERT INTO customer (Cust_ID,Name, Ph_No, Sim_type, Plan_No,Fixed_rental) VALUES (%s,%s, %s, %s, %s,%s)"
    cursor.execute(query, (cust_id,name, ph_no, sim_type, plan_no,fixed_rental))
    conn.commit()
    print("\n")
    print("New customer added successfully!")
    print("\n")
    cursor.close()

# Function to delete a customer (admin functionality)
def delete_customer(conn):
    cursor = conn.cursor()
    print("                  Delete a Customer:")
    ph_no = input("Enter customer phone number to delete: ")
    query = "DELETE FROM customer WHERE Ph_No = %s"
    cursor.execute(query, (ph_no))
    conn.commit()
    print("\n")
    print("Customer deleted successfully!")
    print("\n")
    cursor.close()

# Function to check call records (admin functionality)
def check_call_records(conn):
    cursor = conn.cursor()
    print("                Check Call Records:")
    query = "SELECT * FROM call_records"
    cursor.execute(query)
    call_records = cursor.fetchall()
    for record in call_records:
        print("Name:", record[0])
        print("Phone Number:", record[1])
        print("Call Logs Per Day:", record[2])
        print("Call Received Hour Min:", record[3])
        print("Call Ended Hour Min:", record[4])
        print("Call Duration Hour Min:", record[5])
        print("Location of Phone Number:", record[6])
        print("\n")
    cursor.close()


# Function to check tickets raised (admin functionality)
def check_tickets_raised(conn):
    cursor = conn.cursor()
    print("                Tickets Raised:")
    query = "SELECT * FROM ticket"
    cursor.execute(query)
    tickets = cursor.fetchall()
    for ticket in tickets:
        print("Ticket No:", ticket[0])
        print("Issue:", ticket[1])
        print("Customer ID:", ticket[2])
        print("Date Raised:", ticket[3])
        print("Ticket Status:", ticket[4])
        print("\n")

    cursor.close()

def user_login(conn):
    cursor = conn.cursor()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        query = "SELECT * FROM personal WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        user_data = cursor.fetchone()
        if user_data:
            user = dict(zip([column[0] for column in cursor.description], user_data))
            query2 = "SELECT * FROM customer WHERE Name = %s"
            cursor.execute(query2, (user['Name'],))
            customer_data = cursor.fetchone()
            customer = dict(zip([column[0] for column in cursor.description], customer_data))
            print("\n")
            print("                      Login successful!")
            print("\n")
            cursor.close()
            return user, customer
        else:
            print("Invalid username or password. Please try again.")


# Function to handle admin login
def admin_login(conn):
    cursor = conn.cursor()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "admin123":
            print("\n")
            print("                       Login successful!")
            print("\n")
            cursor.close()
            return True
        else:
            print("Invalid admin username or password. Please try again.")


# Main function
def main():
    conn = connect_to_database()
    if conn is None:
        return

    while True:
        print("                                          Glad to have you back!")
        print("\n")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            user,customer = user_login(conn)
            if user:
                user_functionality(conn, user,customer)
        elif choice == "2":
            if admin_login(conn):
                admin_functionality(conn)
                
        elif choice == "3":
            print("                              Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


def user_menu():
    print("                                          How can we help you today?")
    print("\n")
    print("1. My Plan Details")
    print("2. Recharge My Mobile Number")
    print("3. Get Details of All Prepaid Plans Available")
    print("4. Invoice History")
    print("5. Recharge History")
    print("6. Check Data Usage")
    print("7. Check My Call Logs")
    print("8. My Coupons")
    print("9. Update My Profile")
    print("10. View My Profile")
    print("11. Get Store Information Near My Address")
    print("12. My Tickets Raised")
    print("13. Logout")
    print("\n")
# Function to display admin menu
def admin_menu():
    print("                                          How can we help you today?")
    print("\n")
    print("1. Add New Customer")
    print("2. Delete a Customer")
    print("3. Check Call Records")
    print("4. Tickets Raised")
    print("5. Logout")
    print("\n")
   


# User functionality
def user_functionality(conn, user,customer):
    while True:
        user_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            get_plan_details(customer,conn)
        elif choice == "2":
            recharge_mobile(customer,conn)
        elif choice == "3":
            get_prepaid_plans(customer,conn)
        elif choice == "4":
            get_invoice_history(user,conn)
        elif choice == "5":
            get_recharge_history(user,conn)
        elif choice == "6":
            check_data_usage(user,conn)
        elif choice == "7":
            check_call_logs(user,conn)
        elif choice == "8":
            get_coupons(user,conn)
        elif choice == "9":
            update_profile(user,conn)
        elif choice == "10":
            view_profile(user,conn)
        elif choice == "11":
            get_store_information(user,conn)
        elif choice == "12":
            get_tickets(customer,conn)
        elif choice == "13":
            print("                           Come back soon!  Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Admin functionality
def admin_functionality(conn):
    while True:
        admin_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_new_customer(conn)
        elif choice == "2":
            delete_customer(conn)
        elif choice == "3":
            check_call_records(conn)
        elif choice == "4":
            check_tickets_raised(conn)
        elif choice == "5":
            print("                          Come back soon!  Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
