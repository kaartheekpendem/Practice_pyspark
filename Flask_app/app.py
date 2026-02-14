from flask import Flask
from config import Config
from routes.hello import hello_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(hello_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()