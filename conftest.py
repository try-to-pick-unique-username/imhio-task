import pytest

from application import Application


@pytest.fixture(scope='session')
def app():
    application = Application()
    return application


# @pytest.fixture(scope='session')
# def company_setup(app, request):
#     app.setup_company()
#     def company_teardown():
#         app.clean_company()
#     request.addfinalizer(company_teardown)
