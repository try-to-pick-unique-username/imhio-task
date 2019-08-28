import allure

from src.api.base_request import BaseRequest


class NPSRequest(BaseRequest):

    def __init__(self, app, config):
        super(NPSRequest, self).__init__(app, config)

    @property
    def uri(self):
        return self.baseuri + self.config.endpoints.get('nps', None)

    @allure.step('Sending user feedback')
    def send_feedback(self, payload=None):
        self.send_request(method='post', url=self.uri, json=payload)


