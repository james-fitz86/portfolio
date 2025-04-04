from flask import Blueprint, render_template, abort, request, redirect, url_for, session
from models import get_greeting, get_projects, get_comments, add_comment
from dotenv import load_dotenv
import os

routes_blueprint = Blueprint('routes', __name__)

admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")

@routes_blueprint.route('/')
def home():
    greeting = get_greeting()
    return render_template('index.html', greeting=greeting)

@routes_blueprint.route('/about')
def about():
    return render_template('about.html')

@routes_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@routes_blueprint.route('/projects')
def projects():

    return render_template('projects.html', projects=get_projects(), comments=get_comments())

@routes_blueprint.route("/comment_entry/<int:project_id>", methods=["POST"])
def enter_comment(project_id):
    """Enter a comment."""

    name = request.form["name"]
    message = request.form["message"]

    add_comment(project_id, name, message)
    
    return redirect(url_for("routes.projects"))

@routes_blueprint.route('/skills')
def skills():
    return render_template('skills.html')

@routes_blueprint.route('/admin')
def admin():
    if "username" in session:
        return render_template('admin.html', projects=get_projects(), comments=get_comments())


    return redirect(url_for("routes.home"))

@routes_blueprint.route('/raise_500')
def raise_500_error():
    abort(500)

@routes_blueprint.route("/admin-login-1986", methods=["GET"])
def login():
    """Login page for the app.

    If the user is not logged in, display the login form.
    """

    if "username" in session:
        return redirect(url_for("routes.home"))


    return render_template("login.html")


@routes_blueprint.route("/admin-login-1986", methods=["POST"])
def login_action():
    """Login action for the app (same route as the form)."""

    username = request.form.get("username")
    password = request.form.get("password")

    if username == admin_username and password == admin_password:
        session["username"] = request.form["username"]
        return redirect(url_for("routes.admin"))
    
    return render_template("login.html", error="Invalid input")


@routes_blueprint.route("/logout")
def logout():
    """Logout action for the app.

    This removes the user from the session.

    Note that semantically, this should be a POST request,
    but using GET for logging out is simpler and popular.
    """
    session.pop("username", None)

    return redirect(url_for("routes.home"))

@routes_blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

@routes_blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', error=error), 500