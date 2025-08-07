import json
from pathlib import Path


def get_users():
    path = Path(r"C:\Users\jriyaz\Documents\users.json")
    data = path.read_text()
    data = json.loads(data)
    return data
