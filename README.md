# Telecommunication Database Management System

This project provides a database management system for a telecommunication service provider, offering functionalities for both users and administrators. This README will guide you through the setup, usage, and features of the system.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Database Schema](#database-schema)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
    - [User Functionalities](#user-functionalities)
    - [Admin Functionalities](#admin-functionalities)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This project is a database management system implemented using MySQL for managing customer details, plans, recharges, invoices, data usage, call logs, and more for a telecommunication service provider. It includes functionalities for both regular users and administrators.

## Features

### User Functionalities
- View plan details
- Recharge mobile number
- View available prepaid plans
- Check invoice history
- Check recharge history
- Check data usage
- View call logs
- View and use coupons
- Update profile
- View profile
- Get store information near user's address
- Check raised tickets

### Admin Functionalities
- Add new customer
- Delete customer
- Check call records
- View raised tickets

## Database Schema

The database schema includes the following tables:
- `customer`: Stores customer details.
- `plans`: Contains details of available prepaid plans.
- `recharge`: Records recharge transactions.
- `invoice`: Stores invoice details.
- `data_usage`: Records data usage sessions.
- `call_records`: Stores call log details.
- `coupon`: Contains details of available coupons.
- `personal`: Stores personal information of users.
- `store`: Contains store information near user's address.
- `ticket`: Stores information about raised tickets.

For detailed schema information, refer to the PDF documentation provided in the repository.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/telecommunication-dbms.git
   cd telecommunication-dbms
   ```
   
2. Install dependencies:
   
   Ensure you have Python and MySQL installed. You can install the necessary Python packages using:
   ```sh
   pip install mysql-connector-python
   ```
   
3. Database Setup :
   
   - Create a MySQL database named tele_dbms.
   - Run the SQL script provided in the repository to create the necessary tables and populate them with initial data.
   
4. Configure Database Connection:
   Update the connect_to_database function in the script to match your MySQL credentials:

   ```python
   def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="your_mysql_username",
            password="your_mysql_password",
            database="tele_dbms"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None
   ```

## Usage

  ```sh
  python main.py
  ```

  **User Functionalities**
  
  1. **User Login**
     - Enter your username and password to log in.
       
  2. **Menu Options**

     - Choose from various options to view plan details, recharge mobile, check invoice history, etc.
    
  **Admin Functionalities**
  
  1. **Admin Login**
     - Enter the admin username and password to log in.
       
  2. **Menu Options**

     - Choose from options to add new customer, delete customer, check call records, and view raised tickets.
    
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
   
2. Create a new branch for your feature:
   ```sh
   git checkout -b feature-name
   ```
   
3. Create a new branch for your feature:
   ```sh
   git commit -am 'Add new feature'
   ```
   
4. Create a new branch for your feature:
   ```sh
   git push origin feature-name
   ```
   
5. Create a new branch for your feature:


## License

  This project is licensed under the MIT License. See the LICENSE file for details.
