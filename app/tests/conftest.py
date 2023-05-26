import pytest
from app.app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.testing = True
    app.config.update({
        "ENV": "test",
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
