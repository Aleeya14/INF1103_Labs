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
        print("-" * 65)
        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()
                print(f"   -> Fulfillment: {product.get_fulfilment_info()}")
                if hasattr(product, "calculate_shipping_cost"):
                    print(f"   -> Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        print("-" * 65)

    def get_products(self):
        """Return a copy of the product list (used when saving)."""
        return list(self.__products)