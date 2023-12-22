from fastapi import APIRouter
from models.todos import Todo
from config.DB import collection_name
from  shema.shemas import list_serial
from bson import ObjectId

router = APIRouter()

#GET Request method
@router.get("/todos")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

#POST request method
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))