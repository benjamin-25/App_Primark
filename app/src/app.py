from flask_wtf import CSRFProtect
from flask import Flask
from routes.routes_bp import routes_bp
from flask import Blueprint
import os

SECRET_KEY=os.urandom(32)

ACTIVE_ENDPOINTS = [('/primark', routes_bp)]




def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.debug=True
    app.config['SECRET_KEY'] = SECRET_KEY

    # register each active blueprint
    for url, Blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(Blueprint, url_prefix=url)

    return app

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()
    
