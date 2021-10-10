from flask_wtf import CSRFProtect
from flask import Flask
from routes.routes_bp import routes_bp

ACTIVE_ENDPOINTS = [('/primark', routes_bp)]

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()
