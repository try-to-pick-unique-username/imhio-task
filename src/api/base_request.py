import json
import allure
import requests


class BaseRequest:

    def __init__(self, app, config, headers=None):
        self.app = app
        self.config = config
        self.response_status_code = None
        self.response_body = None
        self.headers = headers

    @property
    def baseuri(self):
        return self.config.environment.get('schema', None) + self.config.environment.get('host', None)

    def send_request(self, method, url=None, **kwargs):
        if url is None:
            url = self.baseuri
        print(f'Sending {method} request to the {url}')
        response = requests.request(method.upper(), url=url, headers=self.headers, **kwargs)
        self.response_status_code = response.status_code
        content = response.content.decode()
        if content.__len__() is not 0:
            try:
                self.response_body = json.loads(content)
            except json.decoder.JSONDecodeError:
                self.response_body = content
            allure.attach(content, 'Response body')

    @allure.step('Validating response status code; expected - {expected_code}')
    def validate_status(self, expected_code: int):
        if not expected_code == self.response_status_code:
            actual_code = self.response_status_code
            raise AssertionError(f'Got {actual_code} status code in response')
