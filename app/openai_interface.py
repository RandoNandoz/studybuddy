import openai
import dotenv
import os

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# 24 hour schedule, time_required measured in minutes, priority from highest, high, average, low, lowest
tasks = [
    {
        "description": "Work on project",
        "time_required": 120,
        "priority": "highest",
        "diffculty": "high",
        "fun": True
    },
    {
        "description": "Clean the house",
        "time_required": 60,
        "priority": "high",
        "diffculty": "average",
        "fun": False
    },
    {
        "description": "Go to the gym",
        "time_required": 80,
        "priority": "average",
        "diffculty": "lowest",
        "fun": True
    }
]

system_instructions = [
    "Given a list of tasks in Python dictionary format, output a schedule for the day in raw JSON format with no escaping, all on one line, with the descriptions and times in the day to do them. DO NOT OUTPUT ANYTHING ELSE"
]
        
openai.api_key = OPENAI_API_KEY

def create_schedule():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": system_instructions[0]
            },
            {
                "role": "user",
                "content": str(tasks)
            }
        ]
    )
    print(completion)
    # print(completion.choices[0].message)

create_schedule()