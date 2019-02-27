from flask import Flask, session
from config import Config

from datetime import timedelta

from app.main import bp as main_bp




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(main_bp, url_prefix='/main')
    


    return app