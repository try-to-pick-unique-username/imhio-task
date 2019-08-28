import allure
import pytest

pytestmark = pytest.mark.API


@allure.feature('Customer Feedback')
@allure.title('Submit customer feedback')
@pytest.mark.positive
def test_when_submitting_feedback_should_receive_success_response(app):
    payload = app.JSON_generator.get_feedback()
    app.nps_request.send_feedback(payload)
    app.nps_request.validate_status(expected_code=200)
    app.schema_validator.validate_json('feedback_ok.json', app.nps_request.response_body)


@allure.feature('Customer Feedback')
@allure.title('Submit customer feedback with no body and receive an error')
@pytest.mark.negative
def test_when_submitting_feedback_without_body_should_receive_error(app):
    app.nps_request.send_feedback()
    app.nps_request.validate_status(expected_code=400)
    app.schema_validator.validate_json('feedback_400.json', app.nps_request.response_body)


@allure.feature('Customer Feedback')
@allure.title('Submit customer feedback with empty body and receive an error')
@pytest.mark.negative
def test_when_submitting_empty_feedback_should_receive_error(app):
    payload = {}
    app.nps_request.send_feedback(payload)
    app.nps_request.validate_status(expected_code=400)
    app.schema_validator.validate_json('feedback_400.json', app.nps_request.response_body)


@allure.feature('Customer Feedback')
@allure.title('Submit customer feedback with invalid rate and receive an error')
@pytest.mark.negative
def test_when_submitting_feedback_with_invalid_rate_should_receive_error(app):
    payload = app.JSON_generator.get_feedback(action="11")
    app.nps_request.send_feedback(payload)
    app.nps_request.validate_status(expected_code=400)
    app.schema_validator.validate_json('feedback_400.json', app.nps_request.response_body)
