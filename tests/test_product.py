from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(product: Product) -> None:
    """Тестирование инициализации класса Product"""
    assert product.name == "Sber"
    assert product.description == "57 Inch"
    assert product.price == 3000.0
    assert product.quantity == 3


def test_new_product() -> None:
    """Проверка корректности создания объекта с заданными параметрами"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_product_update(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестирование корректности обновления цены
    после проверки на соответствие заданным критериям"""
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 15000
    assert product.price == 15000


def test_product_str(first_product: Product) -> None:
    """Проверка корректности строкового представления"""
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 100.0 руб. Остаток: 5 шт.\n"


def test_product_add(first_product: Product, second_product: Product) -> None:
    """Проверка корректности сложения атрибутов"""
    assert (first_product.quantity * first_product.price) + (second_product.quantity * second_product.price) == 2100
