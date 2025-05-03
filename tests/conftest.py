import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны как средство коммуникации",
        products=[
            Product(name="Samsung", description="256GB, Серый цвет", price=100.0, quantity=5),
            Product(name="iPhone", description="512GB, Черный цвет", price=300.0, quantity=2)
        ]

    )

@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product(name="LG", description="43 Inch", price=2000.0, quantity=5),
            Product(name="Samsung", description="32 Inch", price=1000.0, quantity=4),
            Product(name="Sber", description="57 Inch", price=3000.0, quantity=3)
        ]

    )


@pytest.fixture
def product():
    return Product(name="Sber", description="57 Inch", price=3000.0, quantity=3)