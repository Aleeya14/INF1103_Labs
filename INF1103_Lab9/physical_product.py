from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    """Represents a physical product with an added weight attribute."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping via courier."

    def calculate_shipping_cost(self):
        return 5.00 + (self.__weight * 3.00)

    def to_dict(self):
        return {
            "type": "physical",
            "id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight
        }