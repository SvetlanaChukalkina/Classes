from typing import Any

from src.category import Category


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
    assert first_category.products == "Samsung, 100.0 руб. Остаток: 5 шт.\niPhone, 300.0 руб. Остаток: 2 шт.\n"


def test_products_setter(first_category: Category, product: list[Any]) -> None:
    """Проверка корректности работы сеттера, добавляющего
    продукт в атрибут products и прибавляющего 1
    к класс-атрибуту «счетчик продуктов»"""
    assert len(first_category.products_list) == 2
    first_category.products = product
    assert len(first_category.products_list) == 3
