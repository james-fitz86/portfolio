from flask import Flask
from routes import routes_blueprint

app = Flask(__name__)

app.secret_key = "Replace me with a real secret key for production use"

app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8080)