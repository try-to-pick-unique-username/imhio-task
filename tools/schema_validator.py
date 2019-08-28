import os
import json
import allure
from jsonschema import validate
from jsonschema import exceptions


class SchemaValidator:

    __schema_path = os.path.join('schema')

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def read_to_json(file):
        with open(file, 'r') as f:
            return json.loads(f.read())

    @allure.step('Validating actual response body against the schema {schema_name}')
    def validate_json(self, schema_name, actual_json):
        schema = os.path.join(self.__schema_path, schema_name)
        try:
            validate(actual_json, self.read_to_json(schema))
        except exceptions.ValidationError as err:
            message = err.args[0]
            raise AssertionError(f'{message}')