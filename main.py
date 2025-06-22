import mysql.connector
import tkinter as tk
from tkinter import ttk

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',  # Replace with your MySQL password
    database='database_name'  # Replace with your database name
)

cursor = conn.cursor() # Create a cursor object to execute SQL queries
cursor.execute("SELECT id, name, email FROM Users")
users = cursor.fetchall()
#-------------------------------FUNCTIONS-------------------------------------------------
def show_users():
    cursor.execute("SELECT id, name, email FROM Users")
    users = cursor.fetchall()
    # Clear the tree
    for i in tree.get_children():
        tree.delete(i)
    # Update columns
    tree['columns'] = ('ID', 'Name', 'Email')
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Email', text='Email')
    # Insert users
    for user in users:
        tree.insert('', 'end', values=user)
    root.title("Users List")
#function to show users

def show_orders():
    query = """
    SELECT 
        users.id AS user_id,
        users.name AS user_name,
        orders.id AS order_id,
        orders.order_date,
        products.id AS product_id,
        products.name AS product_name,
        orderitems.quantity
    FROM users
    JOIN orders ON users.id = orders.user_id
    JOIN orderitems ON orders.id = orderitems.order_id
    JOIN products ON orderitems.product_id = products.id
    """
    cursor.execute(query)
    orders = cursor.fetchall()
    #Stored search results in a list named orders

    columns = ['user_id', 'user_name', 'order_id', 'order_date', 'product_id', 'product_name', 'quantity']
    # Clear the tree
    for i in tree.get_children():
        tree.delete(i)
    # Update columns
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col.replace('_', ' ').title())
    # Insert orders
    for order in orders:
        tree.insert('', 'end', values=order)
    root.title("Orders List")
#function to show orders


#----------------------------------- GUI setup---------------------------------------------
#
# Create the main window
root = tk.Tk()
root.title("User List")
root.geometry("1400x300")

tree = ttk.Treeview(root, columns=('ID', 'Name', 'Email'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')

for user in users:
    tree.insert('', 'end', values=user)

tree.pack(expand=True, fill='both')

orders_button = tk.Button(root, text="Show Orders", command=show_orders)
orders_button.pack(pady=5)

users_button = tk.Button(root, text="Show Users", command=show_users)
users_button.pack(pady=5)

root.mainloop()