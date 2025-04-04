from datetime import datetime
import shelve
import json

def get_greeting():
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
    with shelve.open('data/data_store') as db:
        if "projects" not in db or "comments" not in db:
            with open("data/data.json") as f:
                data = json.load(f)
            db["projects"] = data["project_details"]
            db["comments"] = {int(k): v for k, v in data["comment_datastore"].items()}

def get_projects():
    with shelve.open("data/data_store") as db:
        return db.get("projects", [])

def get_comments():
    with shelve.open("data/data_store") as db:
        return db.get("comments", {})

def add_comment(project_id, name, message):
    with shelve.open("data/data_store", writeback=True) as db:
        comments = db.get("comments", {})
        comments.setdefault(project_id, []).append({"name": name, "message": message})
        db["comments"] = comments
        db.sync()