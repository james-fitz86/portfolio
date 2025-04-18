from flask import Flask
from routes import routes_blueprint, register_error_handlers
from models import init_shelve
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

init_shelve()

app.register_blueprint(routes_blueprint)

register_error_handlers(app)
