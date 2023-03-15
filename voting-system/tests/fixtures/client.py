from flask import Flask
from pytest import fixture
from main import create_app


@fixture()
def app():
    app: Flask = create_app(environment="testing")
    app.config.update({"TESTING": True})

    yield app


@fixture()
def client(app):
    return app.test_client()

