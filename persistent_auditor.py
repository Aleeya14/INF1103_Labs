def get_valid_input():
    """Prompt for stock quantity. Returns a valid non-negative int or quit."""

    while True:
        stock = input("Enter stock quantity (or type 'quit' to finish); ").strip()

        if stock.lower() == "quit":
            return "quit"

        if not stock.isdigit():
            print("Error: Please enter a valid positive integer.")
            return None

        value = int(stock)
        if value < 0:
            print("Error: Negative stock quantities are not allowed.")
            return None

        return value


def process_delivery(current_total, new_value):
    """Add new_value to current_total and return the updated total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return 10% tax on a single delivery amount."""
    return amount * 0.10


def generate_report(total_units, deliveries_processed, failed_attempts):
    """Print the final summary report."""
    print("\n--- Inventory Report ---")
    print(f"Total Units in Inventory: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

INVENTORY_FILE = "inventory.txt"

def load_inventory():
    """Read saved inventory total and transaction history from the inventory file.
 
    Returns a tuple (total, history_list). If the file does not exist,
    starts with an empty inventory (0, []) and does not raise an error.
    """
    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.read().splitlines()
 
        if not lines:
            return 0, []
 
        total = int(lines[0])
        history = [int(line) for line in lines[1:] if line.strip() != ""]
        return total, history
 
    except FileNotFoundError:
        return 0, []


def save_inventory(total, history):
    """Save the final inventory total and transaction history to the inventory file."""
    with open(INVENTORY_FILE, "w") as file:
        file.write(f"{total}\n")
        for entry in history:
            file.write(f"{entry}\n")


inventory, transaction_history = load_inventory()
deliveries_processed = 0
failed_entries = 0

while True:
    result = get_valid_input()

    if result == "quit":
        save_inventory(inventory, transaction_history)
        print(f"\nTransaction history: {transaction_history}")
        break

    if result is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, result)
    transaction_history.append(result)
    tax = calculate_tax(result)
    deliveries_processed += 1

    print(f"Stock accepted. Delivery tax: {tax:.2f} | Current inventory: {inventory}")

generate_report(inventory, deliveries_processed, failed_entries)