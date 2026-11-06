import json
import os

from inventory import Inventory
from product import PhysicalProduct, DigitalProduct

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.json")

def load_inventory(filename=FILENAME):
    """Return an Inventory loaded from JSON (empty if file missing/broken)."""
    inventory = Inventory()
    if os.path.exists(filename):
        print(f"{os.path.basename(filename)} found.")
        try:
            with open(filename, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            for item in data.get("products", []):
                prod_type = item.get("type")
                if prod_type == "physical":
                    product = PhysicalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["weight"]
                    )
                elif prod_type == "digital":
                    product = DigitalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["download_size"]
                    )
                else:
                    continue  # Skip unknown types
                inventory.add_product(product)
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, TypeError):
            print("Error reading file. Starting with empty inventory.")
            inventory = Inventory()
    else:
        print(f"{os.path.basename(filename)} not found. Starting with empty inventory.")
    return inventory

def save_inventory(inventory, filename=FILENAME):
    """Save all products in the Inventory to JSON preserving their types."""
    try:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        data = {"products": [p.to_dict() for p in inventory.get_products()]}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except OSError as e:
        print(f"Error saving inventory: {e}")
        return False