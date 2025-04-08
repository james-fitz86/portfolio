from flask import Flask
from routes import routes_blueprint, register_error_handlers
from models import init_shelve

app = Flask(__name__)

app.secret_key = "Replace me with a real secret key for production use"

init_shelve()

app.register_blueprint(routes_blueprint)

register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True, port=8080)