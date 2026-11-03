import json
import os
from datetime import datetime

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.json")

def load_inventory(filename=FILENAME):
    """Load inventory and transaction history from JSON if the file exists."""
    print("DEBUG looking for:", filename)
    if os.path.exists(filename):
        print("inventory.json found.")
        try:
            with open(filename, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            print("DEBUG data:", data)
            print("Inventory loaded successfully.")
            return data.get("products", []), data.get("transactions", [])
        except (json.JSONDecodeError, OSError) as e:
            print("DEBUG error:", e)
            print("Error reading file. Starting with empty inventory.")
    else:
        print("inventory.json not found. Starting with empty inventory.")
    return [], []

def record_transaction(transactions, kind, product_id, amount):
    """Store every transaction amount (history, not just a running total)."""
    transactions.append({
        "type": kind,
        "product_id": product_id,
        "amount": round(amount, 2),
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    })

def find_product(inventory, product_id):
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None

def read_number(prompt, cast):
    while True:
        try:
            value = cast(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# ---------- Core functions ----------
def add_product(inventory, transactions):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    if find_product(inventory, product_id):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    price = read_number("Price: ", float)
    stock = read_number("Stock Quantity: ", int)
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    record_transaction(transactions, "add", product_id, price * stock)
    print("\nProduct added successfully!")

def update_stock(inventory, transactions):
    print("\nUpdate Stock")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if not product:
        print("\nProduct not found.")
        return
    print(f"\nProduct Found:\nName: {product['name']}\nCurrent Stock: {product['stock']}")
    new_stock = read_number("\nNew Stock Quantity: ", int)
    change = new_stock - product["stock"]
    product["stock"] = new_stock
    record_transaction(transactions, "update", product["id"], change * product["price"])
    print("\nStock updated successfully!")

def search_product(inventory):
    print("\nSearch Product")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if not product:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print("-" * 48)
    print(f"ID: {product['id']}\nName: {product['name']}\n"
          f"Price: ${product['price']:.2f}\nStock: {product['stock']}")
    print("-" * 48)

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    if not inventory:
        print("Inventory is empty.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)

def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Exit")
    print("----------------------------")

def main():
    print("=" * 42)
    print("INVENTORY MANAGEMENT SYSTEM (Phase 2)")
    print("=" * 42)
    inventory, transactions = load_inventory()
    while True:
        show_menu()
        choice = input("\nEnter option: ").strip()
        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory, transactions)
        elif choice == "3":
            update_stock(inventory, transactions)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("\nProgram terminated.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()