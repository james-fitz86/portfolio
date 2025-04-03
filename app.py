from flask import Flask, render_template, abort, request, redirect, url_for, session
from models import get_greeting

app = Flask(__name__)

app.secret_key = "Replace me with a real secret key for production use"

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
comment_datastore = {
    1: [{'name': 'Joe Bloggs', 'message': 'Thats awesome'}, {'name': 'Bob', 'message': 'Cool'}],
    2: [{'name': 'Jane Doe', 'message': 'Good work!'}, {'name': 'Bill', 'message': 'Love it!'}],
}

admin_username = "James"
admin_password = "abc123xyz"

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

@app.route("/comment_entry/<int:project_id>", methods=["POST"])
def enter_comment(project_id):
    """Enter a comment."""

    name = request.form["name"]
    message = request.form["message"]

    comment_datastore[project_id].append({"name": name, "message": message})
    
    return redirect(url_for("projects"))

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/admin')
def admin():
    if "username" in session:
        print(comment_datastore)
        return render_template('admin.html', projects=project_details, comments=comment_datastore)


    return redirect(url_for("login"))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', error=error), 500

@app.route('/raise_500')
def raise_500_error():
    abort(500)

@app.route("/admin-login-1986", methods=["GET"])
def login():
    """Login page for the app.

    If the user is not logged in, display the login form.
    """

    if "username" in session:
        return redirect(url_for("home"))


    return render_template("login.html")


@app.route("/admin-login-1986", methods=["POST"])
def login_action():
    """Login action for the app (same route as the form)."""
    username = request.form.get("username")
    password = request.form.get("password")

    if username == admin_username and password == admin_password:
        session["username"] = request.form["username"]
        return redirect(url_for("admin"))
    
    return render_template("login.html", error="Inavlid input")


@app.route("/logout")
def logout():
    """Logout action for the app.

    This removes the user from the session.

    Note that semantically, this should be a POST request,
    but using GET for logging out is simpler and popular.
    """
    session.pop("username", None)

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True, port=8080)