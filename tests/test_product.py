def test_product_init(product):
    """Тестирование инициализации класса Product"""
    assert product.name == "Sber"
    assert product.description == "57 Inch"
    assert product.price == 3000.0
    assert product.quantity == 3
