from flask import Flask, Blueprint
from app.entrypoint.vote_resource import votes


def create_app(environment: str) -> Flask:
    app = Flask(__name__)
    api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")
    api_v1.register_blueprint(votes)
    app.register_blueprint(api_v1)

    return app