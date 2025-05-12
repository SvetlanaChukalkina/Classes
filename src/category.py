from typing import Optional

from src.product import Product


class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Возвращает строковое отображение в заданном виде для объектов класса"""
        products_sum = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {products_sum} шт."

    @property  # type: ignore
    def products(self) -> str:
        """Выводит список товаров в виде строк в заданном формате"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, new_product: Product) -> None:
        """Добавляет продукт в приватный атрибут products"""
        self.__products.append(new_product)

    @products.setter  # type: ignore
    def products(self, new_product: Product) -> None:
        """Добавляет продукт в атрибут products,
        прибавляет 1 к класс-атрибуту «счетчик продуктов»"""
        self.add_product(new_product)
        Category.product_count += 1

    @property
    def products_list(self) -> list:
        """Выводит список товаров в виде списка"""
        return self.__products
