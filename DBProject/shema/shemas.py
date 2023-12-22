from fastapi import FastAPI
from pymongo import MongoClient
from models.todos import Todo

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "last_name": todo["last_name"],
        "first_name": todo["first_name"],
        "middle_name": todo["middle_name"],
        "post": todo["post"],
        "mail": todo["mail"],
        "department": todo["department"],
        "answer1": todo["answer1"],
        "answer2": todo["answer2"],
        "answer3": todo["answer3"],
        "answer4": todo["answer4"],
        "answer5": todo["answer5"],
        "answer6": todo["answer6"]
    }


def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]

