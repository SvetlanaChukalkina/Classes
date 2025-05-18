from typing import Any

from src.product import Product


class LawnGrass(Product):
    """Класс для представления травы газонной, наследник класса Product"""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> float:
        if type(other) is LawnGrass:
            return (self.quantity * self.price) + (other.quantity * other.price)
        raise TypeError
