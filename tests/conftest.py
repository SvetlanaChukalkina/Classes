import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны как средство коммуникации",
        products=[
            Product(name="Samsung", description="256GB, Серый цвет", price=100.0, quantity=5),
            Product(name="iPhone", description="512GB, Черный цвет", price=300.0, quantity=2),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product(name="LG", description="43 Inch", price=2000.0, quantity=5),
            Product(name="Samsung", description="32 Inch", price=1000.0, quantity=4),
            Product(name="Sber", description="57 Inch", price=3000.0, quantity=3),
        ],
    )


@pytest.fixture
def product() -> Product:
    return Product(name="Sber", description="57 Inch", price=3000.0, quantity=3)


@pytest.fixture
def test_category_iterator(second_category: Category) -> CategoryIterator:
    return CategoryIterator(second_category)


@pytest.fixture
def first_product() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 100.0, 5)


@pytest.fixture
def second_product() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 200.0, 8)


@pytest.fixture
def first_smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def second_smartphone() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def first_lawngrass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_lawngrass() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
