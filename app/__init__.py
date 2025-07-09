from flask import Flask
from flask_cors import CORS
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    print(app.config.get("CORS_ORIGINS"))
    CORS(app, origins=app.config.get("CORS_ORIGINS"))

    from .routes import post

    app.register_blueprint(post.bp)

    return app
