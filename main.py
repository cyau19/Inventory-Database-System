import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="your_password", 
        database="inventory_db"
    )

def view_inventory():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    items = cursor.fetchall()
    if not items:
        print("\n📭 The inventory is currently empty.")
    else:
        print("\n--- CURRENT STOCK ---")
        print(f"{'ID':<5} {'Name':<20} {'Qty':<10} {'Price':<10}")
        for i in items:
            alert = "⚠️ LOW" if i[2] < 5 else ""
            print(f"{i[0]:<5} {i[1]:<20} {i[2]:<10} ${i[3]:<10} {alert}")
    db.close()

def add_item():
    try:
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, qty, price))
        db.commit()
        print("✅ Item added.")
        db.close()
    except ValueError:
        print("❌ Error: Quantity must be a whole number and Price must be a decimal.")

def update_stock():
    view_inventory()
    product_id = input("\nEnter the ID of the product to update: ")
    
    db = connect_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    if cursor.fetchone() is None:
        print(f"❌ Error: Product ID {product_id} does not exist.")
    else:
        try:
            new_qty = int(input("Enter new quantity: "))
            cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (new_qty, product_id))
            db.commit()
            print("✅ Stock updated.")
        except ValueError:
            print("❌ Error: Please enter a valid number for quantity.")
    db.close()

def delete_item():
    view_inventory()
    product_id = input("\nEnter the ID of the product to DELETE: ")
    
    db = connect_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    if cursor.fetchone() is None:
        print(f"❌ Error: Cannot delete. ID {product_id} not found.")
    else:
        confirm = input(f"Are you sure you want to delete ID {product_id}? (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            db.commit()
            print("🗑️ Item removed.")
        else:
            print("Deletion cancelled.")
    db.close()

while True:
    print("\n--- INVENTORY MANAGER ---")
    print("1. View Stock\n2. Add Item\n3. Update Quantity\n4. Delete Item\n5. Exit")
    choice = input("Select (1-5): ")
    
    if choice == '1': view_inventory()
    elif choice == '2': add_item()
    elif choice == '3': update_stock()
    elif choice == '4': delete_item()
    elif choice == '5': 
        print("Goodbye!")
        break
    else: 
        print(f"❌ Error: '{choice}' is not a valid option. Please choose 1-5.")