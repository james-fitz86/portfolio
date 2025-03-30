from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)