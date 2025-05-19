import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(first_lawngrass: LawnGrass) -> None:
    """Проверка корректности инициализации
    экземпляра класса LawnGrass"""
    assert first_lawngrass.name == "Газонная трава"
    assert first_lawngrass.description == "Элитная трава для газона"
    assert first_lawngrass.price == 500.0
    assert first_lawngrass.quantity == 20
    assert first_lawngrass.country == "Россия"
    assert first_lawngrass.germination_period == "7 дней"
    assert first_lawngrass.color == "Зеленый"


def test_smartphones_add(first_lawngrass: LawnGrass, second_lawngrass: LawnGrass) -> None:
    """Проверка корректности сложения атрибутов объектов класса"""
    assert (first_lawngrass.quantity * first_lawngrass.price) + (
        second_lawngrass.quantity * second_lawngrass.price
    ) == 16750


def test_smartphones_add_error(first_lawngrass: LawnGrass) -> None:
    """Проверка работы метода add при сложении
    объекта класса с другим объектом, не относящимся к классу"""
    with pytest.raises(TypeError):
        first_lawngrass + 10
