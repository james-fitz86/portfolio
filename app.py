from flask import Flask, render_template, abort, request, redirect, url_for
from models import get_greeting

app = Flask(__name__)

project_details = [
    {
        "id": 1,
        "name": "City Rovers FC",
        "link": "https://james-fitz86.github.io/cityrovers/",
        "image": "static/images/rovers.png",
        "description": "Website for a local football team.",
        "tags": "HTML, CSS",

    },
    {
        "id": 2,
        "name": "Betty's Bakes",
        "link": "https://james-fitz86.github.io/bettysbakes/",
        "image": "static/images/bettys.png",
        "description": "Website for baking Recipes",
        "tags": "HTML, CSS, Javascript",
    }

]
comment_datastore = {}

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

    return render_template('projects.html', projects=project_details, comments=comment_datastore)

@app.route("/comment_entry", methods=["POST"])
def enter_comment():
    """Enter a comment."""

    name = request.form["name"]
    message = request.form["message"]

    comment_datastore[name] = message

    return redirect(url_for("projects"))

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