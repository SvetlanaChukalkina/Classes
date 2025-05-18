import pytest

from src.smartphone import Smartphone


def test_smartphone_init(first_smartphone: Smartphone) -> None:
    """Проверка корректности инициализации
    экземпляра класса Smartphone"""
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphones_add(first_smartphone: Smartphone, second_smartphone: Smartphone) -> None:
    """Проверка корректности сложения атрибутов объектов класса"""
    assert (first_smartphone.quantity * first_smartphone.price) + (
        second_smartphone.quantity * second_smartphone.price
    ) == 2580000


def test_smartphones_add_error(first_smartphone: Smartphone) -> None:
    """Проверка работы метода add при сложении
    объекта класса с другим объектом, не относящимся к классу"""
    with pytest.raises(TypeError):
        first_smartphone + 8
