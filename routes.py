from flask import Blueprint, render_template, abort, request, redirect, url_for, session
from models import get_greeting, get_projects, get_comments, add_comment, delete_comment_by_index, add_like, get_skills, get_experience, add_message, get_messages, delete_message, save_skills, edit_project
from dotenv import load_dotenv
import os
import shelve

routes_blueprint = Blueprint('routes', __name__)

admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")

@routes_blueprint.route('/')
def home():
    greeting = get_greeting()
    return render_template('index.html', greeting=greeting)

@routes_blueprint.route('/about')
def about():
    experience = get_experience()
    return render_template('about.html', experience=experience)

@routes_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@routes_blueprint.route('/submit_contact', methods=[ "POST"])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    add_message(name, email, subject, message)
    return render_template('contact.html', success=True)

   

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
    skill_data = get_skills()
    return render_template('skills.html', skills=skill_data)

@routes_blueprint.route('/admin')
def admin():
    if "username" in session:
        return render_template('admin.html', projects=get_projects(), comments=get_comments(), messages=get_messages(), skills=get_skills())


    return redirect(url_for("routes.home"))

@routes_blueprint.route('/raise_500')
def raise_500_error():
    abort(500)

@routes_blueprint.route('/raise_404')
def raise_404_error():
    abort(404)

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

@routes_blueprint.route("/delete-comment", methods=["POST"])
def delete_comment_route():
    project_id = request.form["project_id"]
    index = int(request.form["index"])
    delete_comment_by_index(project_id, index)
    return redirect(url_for("routes.admin"))

@routes_blueprint.route("/delete-message", methods=["POST"])
def delete_message_route():
    index = int(request.form["index"])
    delete_message(index)
    return redirect(url_for("routes.admin"))

@routes_blueprint.route('/like/<int:project_id>', methods=["POST"])
def likes(project_id):
    add_like(project_id)
    return redirect(url_for("routes.projects"))

@routes_blueprint.route("/admin/skills", methods=["POST"])
def update_skills():
    updated_skills = {}
    for key in request.form:
        try:
            updated_skills[key] = int(request.form[key])
        except ValueError:
            continue

    save_skills(updated_skills)
    return redirect(url_for("routes.admin"))

@routes_blueprint.route("/admin/update-projects", methods=["POST"])
def update_projects():
    edit_project(request.form)
    return redirect(url_for("routes.admin"))

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html', error=error), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html', error=error), 500