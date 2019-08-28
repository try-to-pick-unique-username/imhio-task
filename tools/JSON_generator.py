import random

from tools.data_generator import DataGenerator
from model.feedback import Feedback


class JSONGenerator:


    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self.data = DataGenerator()

    def get_feedback(self, action=None):
        feedback = self.data.get_text()
        if action is None:
            action = str(random.randint(0, 11))
        return Feedback(action, feedback).__dict__