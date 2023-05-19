import pytest
from app.app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.testing = True
    app.config.update({
        "ENV": "test",
        "DB_HOST": "vps.sokoloowski.pl",
        "DB_NAME": "pzio",
        "DB_PORT": 3306,
        "DB_USER": "pzio",
        "DB_PASSWORD": "OhAfodyhDB",
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
