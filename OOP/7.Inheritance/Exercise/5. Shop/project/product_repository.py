from typing import List
from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def __repr__(self):
        return '\n'.join([f"{product.name}: {product.quantity}" for product in self.products])
