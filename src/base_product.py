from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс, родительский для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        pass
