from flask import Flask, render_template, abort
from models import get_greeting

app = Flask(__name__)

@app.route('/')
def home():
    greeting = get_greeting()
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', error=error), 500

@app.route('/raise_500')
def raise_500_error():
    abort(500)

if __name__ == '__main__':
    app.run(debug=True, port=8080)