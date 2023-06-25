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
    def __init__(self, description: str, priority: Priority, difficulty: Difficulty, fun: bool):
        self.description = description
        self.priority = priority
        self.difficulty = difficulty
        self.fun = fun
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(d["description"], Priority(d["priority"]), Difficulty(d["difficulty"]), bool(d["fun"]))