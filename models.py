from datetime import datetime
import shelve
import json

def get_greeting():
    """Return a greeting based on the current time of day."""
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    elif 18 <= current_hour < 23:
        return "Good Evening"
    else:
        return "Hello Night Owl"

def init_shelve():
    """Initialize the shelve database with default data from JSON if keys are missing."""
    with shelve.open('data/data_store') as db:
        if "projects" not in db or "comments" not in db or "messages" not in db:
            with open("data/data.json") as f:
                data = json.load(f)
            db["projects"] = data["project_details"]
            db["comments"] = {int(k): v for k, v in data["comment_datastore"].items()}
            db["skills"] = data["skills_details"]
            db["messages"] = data["contact_datastore"]

def get_projects():
    """Retrieve all project entries from the database."""
    with shelve.open("data/data_store") as db:
        return db.get("projects", [])

def get_comments():
    """Retrieve all comments from the database."""
    with shelve.open("data/data_store") as db:
        return db.get("comments", {})

def get_skills():
    """Retrieve all skill data from the database."""
    with shelve.open("data/data_store") as db:
        return db.get("skills", {})

def get_messages():
    """Retrieve all contact messages from the database."""
    with shelve.open("data/data_store") as db:
        return db.get("messages", [])

def add_message(name, email, subject, message):
    """Add a new contact message to the database."""
    new_message = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message
    }

    with shelve.open('data/data_store', writeback=True) as db:
        messages = db['messages']
        messages.append(new_message)
        db['messages'] = messages
        db.sync()

def add_comment(project_id, name, message):
    """Add a comment to a specific project by ID."""
    with shelve.open("data/data_store", writeback=True) as db:
        comments = db.get("comments", {})
        comments.setdefault(project_id, []).append({"name": name, "message": message})
        db["comments"] = comments
        db.sync()

def add_like(project_id):
    """Increment the like count for a specific project by ID."""
    with shelve.open("data/data_store", writeback=True) as db:
        projects = db.get("projects", [])
        for project in projects:
            if project["id"] == project_id:
                project["likes"] += 1
                break
        db["projects"] = projects
        db.sync()

def delete_comment_by_index(project_id, index):
    """Delete a comment by its index from a specific project's comment list."""
    with shelve.open("data/data_store", writeback=True) as db:
        comments = db.get("comments", {})
        project_id = int(project_id)
        if project_id in comments and 0 <= index < len(comments[project_id]):
            del comments[project_id][index]
            db["comments"] = comments
            db.sync()

def delete_message(index):
    """Delete a message by its index from the message list."""
    with shelve.open("data/data_store", writeback=True) as db:
        messages = db['messages']
        if 0 <= index < len(messages):
            del messages[index]
            db["messages"] = messages
            db.sync()

def get_experience():
    """Calculate and return the number of months since the start date (Sept 24, 2024)."""
    start_date = datetime(2024, 9, 24)
    today = datetime.now()

    months_since = (today.year - start_date.year)*12 + (today.month - start_date.month)
    if today.day < start_date.day:
        months_since -= 1

    return months_since

def save_skills(updated_skills, path="data/data_store"):
    """Save updated skill data to the database."""
    with shelve.open(path, writeback=True) as db:
        db["skills"] = updated_skills
        db.sync()

def edit_project(data, path="data/data_store"):
    """Edit an existing project's data based on its ID."""
    project_id = data.get("id")

    with shelve.open(path, writeback=True) as db:
        current_projects = db.get("projects", [])
        updated_projects = []

        for project in current_projects:
            if str(project["id"]) == project_id:
                updated_projects.append({
                    "id": project["id"],
                    "name": data.get("name", project["name"]),
                    "link": data.get("link", project["link"]),
                    "image": data.get("image", project["image"]),
                    "description": data.get("description", project["description"]),
                    "tags": data.get("tags", project["tags"]),
                    "likes": project["likes"],
                })
            else:
                updated_projects.append(project)

        db["projects"] = updated_projects
        db.sync()

def add_project(data, path="data/data_store"):
    """Add a new project to the database."""
    with shelve.open(path, writeback=True) as db:
        projects = db.get("projects", [])
        new_id = max((p["id"] for p in projects), default=0) + 1

        new_project = {
            "id": new_id,
            "name":data["name"],
            "link":data["link"],
            "image": data["image"],
            "description":data["description"],
            "tags":data["tags"],
            "likes": 0,
        }

        projects.append(new_project)
        db["projects"] = projects
        db.sync()

def delete_project(project_id, path="data/data_store"):
    """Delete a project by its ID from the database."""
    with shelve.open(path, writeback=True) as db:
        projects = db.get("projects", [])
        projects = [p for p in projects if p["id"] != project_id]
        db["projects"] = projects
        db.sync()