from task.Task import Task

import firebase_admin
import firebase_admin.db

from firebase_admin import credentials

cred = credentials.Certificate('app/vshacks-project-firebase-adminsdk-guz81-a5d561efbc.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://vshacks-project-default-rtdb.firebaseio.com/"
})

def get_all_tasks(username: str) -> list[Task]:
    """
    Returns a list of all tasks in the database by username.
    """
    ref = firebase_admin.db.reference(f"{username}")
    return [Task.from_dict(task) for task in ref.get()]

print(get_all_tasks("randyzhu"))
