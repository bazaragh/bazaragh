import pytest
import os
from flask import template_rendered
from flask.helpers import get_root_path

from app.app import create_app
from app.app import db

from sqlalchemy import text


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


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture(autouse=True)
def reload_database_data(app):
    yield
    with open(os.path.join(get_root_path("app"), "tests", "pzio.sql"), encoding='UTF-8') as file:
        query = text(file.read())
        with app.app_context():
            db.session.execute(query)
