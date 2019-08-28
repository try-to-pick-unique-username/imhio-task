from tools.config_reader import ConfigurationReader
from tools.schema_validator import SchemaValidator
from tools.JSON_generator import JSONGenerator
from src.api.base_request import BaseRequest
from src.api.nps_request import NPSRequest


class Application:
    def __init__(self):
        self.config = ConfigurationReader()
        self.schema_validator = SchemaValidator()
        self.JSON_generator = JSONGenerator()
        self.base_request = BaseRequest(self, self.config)
        self.nps_request = NPSRequest(self, self.config)