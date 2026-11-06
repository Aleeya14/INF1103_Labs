from abc import ABC, abstractmethod

class Product(ABC):
    """Represents and manages ONE product (Abstract Base Class)."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Product decides how a new stock value is treated."""
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}", end="")
 
    def to_dict(self):
        """Used by file handling to save this product."""
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

    @abstractmethod
    def get_fulfilment_info(self):
        """Abstract method that must be implemented by subclasses."""
        pass

class PhysicalProduct(Product):
    """Represents a physical product with an added weight attribute."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        """Reuses parent display behavior and appends physical-specific info."""
        super().display_information()
        print(f" | Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        """Fulfills the abstract method requirement for physical products."""
        return "This product requires physical shipping via courier."

class DigitalProduct(Product):
    """Represents a digital product with an added download size attribute."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        """Reuses parent display behavior and appends digital-specific info."""
        super().display_information()
        print(f" | Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        """Fulfills the abstract method requirement for digital products."""
        return "This product is delivered digitally via email/download link."

if __name__ == "__main__":

    try:
        print("--- Attempting to instantiate abstract Product class ---")
        abstract_product = Product("P999", "Generic Item", 10.00, 5)
    except TypeError as e:
        print(f"Caught expected error: {e}\n")

    print("--- Testing Physical Product ---")
    physical_item = PhysicalProduct("P002", "Mechanical Keyboard", 150.00, 30, 1.2)
    physical_item.display_information()
    print(f"Fulfilment: {physical_item.get_fulfilment_info()}")

    print("\n--- Testing Digital Product ---")
    digital_item = DigitalProduct("D001", "Python Masterclass E-Book", 29.99, 100, 45.5)
    digital_item.display_information()
    print(f"Fulfilment: {digital_item.get_fulfilment_info()}")