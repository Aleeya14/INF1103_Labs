import os

from file_handling import FILENAME, load_inventory, save_inventory
from product import PhysicalProduct, DigitalProduct

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

    print("\nSelect Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")
    type_choice = input("Enter choice (1-2): ").strip()

    if type_choice == "1":
        weight = read_number("Weight (kg): ", float)
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif type_choice == "2":
        download_size = read_number("Download Size (MB): ", float)
        product = DigitalProduct(product_id, name, price, stock, download_size)
    else:
        print("Invalid product type choice. Product creation cancelled.")
        return

    inventory.add_product(product)
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
    print("-" * 52)
    product.display_information()
    print(f"Fulfilment Info: {product.get_fulfilment_info()}")
    
    # If it implements the CanBeShipped interface, display shipping cost
    if hasattr(product, "calculate_shipping_cost"):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 52)

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