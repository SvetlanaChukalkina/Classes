from typing import Any


class CategoryIterator:
    def __init__(self, category_obj: Any) -> None:
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
