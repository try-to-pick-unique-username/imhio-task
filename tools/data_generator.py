from faker import Faker
from faker.providers import lorem


class DataGenerator:

    instance = None

    def __init__(self):
        self.fake = Faker()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def get_text(self):
        self.fake.add_provider(lorem)
        return self.fake.sentence()