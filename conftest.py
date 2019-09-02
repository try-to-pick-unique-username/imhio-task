import pytest

from application import Application


@pytest.fixture(scope='session')
def app():
    application = Application()
    return application
