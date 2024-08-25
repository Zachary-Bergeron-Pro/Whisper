from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
