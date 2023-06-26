from enum import Enum


class Difficulty(Enum):
    EASIEST = "Easiest"
    EASY = "Easy"
    AVERAGE = "Average"
    HARD = "Hard"
    HARDEST = "Hardest"


class Priority(Enum):
    LOWEST = "Lowest"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    HIGHEST = "Highest"


class Task:
    def __init__(
        self, description: str, priority: Priority, difficulty: Difficulty, fun: bool, time_required: int
    ):
        self.description = description
        self.priority = priority
        self.difficulty = difficulty
        self.fun = fun
        self.time_required = time_required

    def __getitem__(self, key):
        return getattr(self, key)

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            d["description"],
            Priority(d["priority"]),
            Difficulty(d["difficulty"]),
            bool(d["fun"]),
            time_required=int(d["time_required"]),
        )
    
    def __dict__(self):
        return {
            "description": self.description,
            "difficulty": self.difficulty.value,
            "fun": self.fun,
            "priority": self.priority.value,
            "time_required": self.time_required
        }


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
    return [Task.from_dict(task) for task in ref.get().values()]

def add_task(task: Task, username: str) -> None:
    """
    Adds a task to the database.
    """
    ref = firebase_admin.db.reference(f"{username}")
    ref.push(task.__dict__())

def delete_task(key, username: str) -> None:
    """
    Deletes a task from the database.
    """
    ref = firebase_admin.db.reference(f"{username}")
    ref.delete(task.__dict__())