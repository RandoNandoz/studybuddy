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
