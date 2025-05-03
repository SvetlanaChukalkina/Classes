class Category:
    """Класс для представления категорий"""
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products