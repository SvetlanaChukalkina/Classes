from typing import Any

import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.smartphone import Smartphone


def test_category_init(first_category: Category, second_category: Category) -> None:
    """Тестирование инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны как средство коммуникации"
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор"
    assert len(first_category.products_list) == 2
    assert len(second_category.products_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_products_property(first_category: Category) -> None:
    """Проверка вывода списка товаров в виде строк в заданном формате"""
    assert first_category.products == "Samsung, 100.0 руб. Остаток: 5 шт.\n\niPhone, 300.0 руб. Остаток: 2 шт.\n\n"


def test_products_setter(first_category: Category, product: list[Any]) -> None:
    """Проверка корректности работы сеттера, добавляющего
    продукт в атрибут products и прибавляющего 1
    к класс-атрибуту «счетчик продуктов»"""
    assert len(first_category.products_list) == 2
    first_category.products = product
    assert len(first_category.products_list) == 3


def test_category_str(first_category: Category) -> Any:
    """Проверка корректности строкового представления"""
    assert str(first_category) == "Смартфоны, количество продуктов: 7 шт."


def test_iterator(test_category_iterator: CategoryIterator) -> None:
    """Проверка корректности работы итератора"""
    iter(test_category_iterator)
    assert test_category_iterator.index == 0
    assert next(test_category_iterator).name == "LG"
    assert next(test_category_iterator).name == "Samsung"
    assert next(test_category_iterator).name == "Sber"

    with pytest.raises(StopIteration):
        next(test_category_iterator)


def test_products_setter_error(first_category: Category, product: list[Any]) -> None:
    """Проверка поведения программы при добавлении
    не продукта в атрибут products"""
    with pytest.raises(TypeError):
        first_category.products = "0"


def test_products_setter_smartphone(first_category: Category, first_smartphone: Smartphone) -> None:
    """Проверка поведения программы при добавлении
    объекта класса Smartphone в атрибут products"""
    first_category.products = first_smartphone
    first_category.products_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_middle_price(first_category: Category, category_without_product: Category) -> None:
    """Проверка корректности вычисления среднего ценника товаров в категории"""
    assert int(first_category.middle_price()) == 57
    assert category_without_product.middle_price() == 0
