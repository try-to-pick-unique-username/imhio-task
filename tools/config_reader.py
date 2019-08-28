import yaml
import os

class ConfigurationReader:


    __config = os.path.join('config.yaml')

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self.endpoints = self.read(self.__config).get("endpoints", None)
        self.environment = self.read(self.__config).get("environment", None)


    @staticmethod
    def read(file):
        with open(file, 'r') as stream:
            return yaml.safe_load(stream)