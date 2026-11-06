import os

from file_handling import FILENAME, load_inventory, save_inventory
from product import Product


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


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def add_product_menu(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    if inventory.search_product(product_id):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    price = read_number("Price: ", float)
    stock = read_number("Stock Quantity: ", int)
    inventory.add_product(Product(product_id, name, price, stock))
    print("\nProduct added successfully!")


def update_stock_menu(inventory):
    print("\nUpdate Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if not product:
        print("\nProduct not found.")
        return
    print(f"\nProduct Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
    product.update_stock(read_number("\nNew Stock Quantity: ", int))
    print("\nStock updated successfully!")


def search_product_menu(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if not product:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print("-" * 48)
    print(f"ID: {product.get_product_id()}\nName: {product.get_name()}\n"
          f"Price: ${product.get_price():.2f}\nStock: {product.get_stock()}")
    print("-" * 48)


def main():
    print("=" * 42)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 42 + "\n")
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("\nEnter option: ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            print("\nSaving inventory...")
            if save_inventory(inventory):
                print(f"Inventory saved successfully to {os.path.basename(FILENAME)}.")
        elif choice == "6":
            print("\nSaving inventory before exit...")
            if save_inventory(inventory):
                print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")