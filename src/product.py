from typing import Any


class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
