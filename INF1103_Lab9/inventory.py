from product import Product

class Inventory:
    """Manages a COLLECTION of Product objects (Single Responsibility)."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a product. Returns False if the ID already exists."""
        if self.search_product(product.get_product_id()):
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the matching Product, or None if not found."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_products(self):
        """Return a copy of the product list (used when saving)."""
        return list(self.__products)
    
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
    inventory.display_all()
    found = inventory.search_product("P002")
    print("\nSearch P002:", found.get_name() if found else "Not found")