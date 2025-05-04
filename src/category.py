from typing import Any


class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: Any, description: Any, products: Any = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
