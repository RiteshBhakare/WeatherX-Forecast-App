from flask import Flask
from .routes import main  # Assuming you registered a Blueprint called "main"

from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env file

API_KEY = os.getenv("WEATHER_API_KEY")

def create_app():
    app = Flask(__name__)
    
    # Configuration (optional)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    # Register Blueprints
    app.register_blueprint(main)

    return app
