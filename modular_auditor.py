def get_valid_input():
    """Prompt for stock quantity. Returns a valid non-negative int or quit."""

    while True:
        stock = input("Enter stock quantity (or type 'quit' to finish); ").strip()

        if stock.lower() == "quit":
            return "quit"

        if not stock.isdigit():
            print("Error: Please enter a valid positive integer.")
            return None  # signals a failed attempt to the caller

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


inventory = 0
deliveries_processed = 0
failed_entries = 0

while True:
    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, result)
    tax = calculate_tax(result)
    deliveries_processed += 1

    print(f"Stock accepted. Delivery tax: {tax:.2f} | Current inventory: {inventory}")

generate_report(inventory, deliveries_processed, failed_entries)