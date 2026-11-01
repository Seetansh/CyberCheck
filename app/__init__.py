from flask import Flask, render_template
from app.config import(
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)
from dotenv import load_dotenv
from app.routes.auth import auth_bp
from app.routes.public import public_bp
from app.routes.scanner import scanner_bp
from app.routes.user import user_bp

def create_app(configClass = DevelopmentConfig):
    
    # load env variables
    load_dotenv()

    # create flask app
    app = Flask(__name__, template_folder='templates', static_folder='static')
    # loading configuration
    app.config.from_object(configClass)

    # registering bp
    app.register_blueprint(auth_bp, url_prefix = '/auth')
    app.register_blueprint(public_bp)
    app.register_blueprint(scanner_bp, url_prefix = '/scanner')
    app.register_blueprint(user_bp, url_prefix = "/user")

    app.secret_key = "secret_key"



    return app
    
