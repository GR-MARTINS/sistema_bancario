import json


def carregar_dados():
    try:
        with open("db.json", "r") as f:
            db = json.load(f)
            return db

    except FileNotFoundError:
        return None
