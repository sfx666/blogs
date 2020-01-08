from flask import Flask

from App.ext import init_app
from App.settings import Config
from App.views import register_blueprint


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config.get('default', 'devalop'))

    init_app(app)

    register_blueprint(app)

    return app










