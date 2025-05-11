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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: Any):
        """Принимает на вход параметры товара в словаре,
        возвращает созданный объект класса Product"""
        return cls(**new_product)

    @property  # type: ignore
    def price(self) -> Any:
        """Возвращает значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """Проверяет на корректность значение новой цены,
        в случае соответствия критериям обновляет ее в атрибуте"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if self.__price > new_price:
                user_answer = (input("Цена ниже предыдущей, понизить цену? y/n")).lower()
                if user_answer == "y":
                    self.__price = new_price
                else:
                    self.__price = self.__price
            else:
                self.__price = new_price
