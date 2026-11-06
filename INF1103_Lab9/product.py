class Product:
    """Represents and manages ONE product (Single Responsibility)."""

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
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
 
    def to_dict(self):
        """Used by file handling to save this product."""
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}
    
class PhysicalProduct(Product):
    """Represents a physical product with an added weight attribute."""

    def __init__(self, product_id, name, price, stock, weight):
        # Reuse the parent constructor
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        """Displays the product's existing information alongside its weight."""
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | "
              f"Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | "
              f"Weight: {self.__weight} kg")
        
        
class DigitalProduct(Product):
    """Represents a digital product with an added download size attribute."""

    def __init__(self, product_id, name, price, stock, download_size):
        # Reuse the parent constructor
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        """Displays the product's existing information alongside its download size."""
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | "
              f"Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | "
              f"Download Size: {self.__download_size} MB")
              
if __name__ == "__main__":
    product = Product("P001", "Laptop", 1200.00, 15)
    product.display_information()
    product.update_stock(50)
    product.display_information()


 