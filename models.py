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
            db["skills"] = data["skills_details"]

def get_projects():
    with shelve.open("data/data_store") as db:
        return db.get("projects", [])

def get_comments():
    with shelve.open("data/data_store") as db:
        return db.get("comments", {})

def get_skills():
    with shelve.open("data/data_store") as db:
        return db.get("skills", {})

def add_comment(project_id, name, message):
    with shelve.open("data/data_store", writeback=True) as db:
        comments = db.get("comments", {})
        comments.setdefault(project_id, []).append({"name": name, "message": message})
        db["comments"] = comments
        db.sync()

def add_like(project_id):
    with shelve.open("data/data_store", writeback=True) as db:
        projects = db.get("projects", [])
        for project in projects:
            if project["id"] == project_id:
                project["likes"] += 1
                break
        db["projects"] = projects
        db.sync()

def delete_comment_by_index(project_id, index):
    with shelve.open("data/data_store", writeback=True) as db:
        comments = db.get("comments", {})
        project_id = int(project_id)
        if project_id in comments and 0 <= index < len(comments[project_id]):
            del comments[project_id][index]
            db["comments"] = comments
            db.sync()

def get_experience():
    start_date = datetime(2024, 9, 24)
    today = datetime.now()

    months_since = (today.year - start_date.year)*12 + (today.month - start_date.month)
    if today.day < start_date.day:
        months_since -= 1

    return months_since