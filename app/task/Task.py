from Difficulty import Difficulty
from Priority import Priority
class Task:
    def __init__(self, description: str, priority: Priority, difficulty: Difficulty, fun: bool):
        self.description = description
        self.priority = priority
        self.difficulty = difficulty
        self.fun = fun
    
    def __getitem__(self, key):
        return getattr(self, key)