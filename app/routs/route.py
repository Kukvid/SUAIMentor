from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from models.todos import Todo
from config.DB import collection_name
from shema.shemas import list_serial

templates = Jinja2Templates(directory="FrontEND")

router = APIRouter()


#GET Request method
@router.get("/todos")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

#GET Request method
@router.get("/main", response_class=FileResponse)
async def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "url_for_main": "/main", "url_for_teachers": "/teachers", "url_for_documentation": "/documentation"})

#GET Request method
@router.get("/documentation", response_class=FileResponse)
async def get_docs(request: Request):
    return templates.TemplateResponse("documentation.html", {"request": request, "url_for_main": "/main", "url_for_teachers": "/teachers", "url_for_documentation": "/documentation"})

#GET Request method
@router.get("/teachers", response_class=FileResponse)
async def get_teachers(request: Request):
    return templates.TemplateResponse("teachers.html", {"request": request, "url_for_main": "/main", "url_for_teachers": "/teachers", "url_for_documentation": "/documentation"})

#GET Request method
@router.get("/teachers/{teacher_id}", response_class=FileResponse)
async def get_teacher(request: Request, teacher_id: int):
    person_info = list_serial(collection_name.find())[teacher_id]
    person_name = person_info["first_name"] + " " + person_info["last_name"] + " " + person_info["middle_name"]
    return templates.TemplateResponse("template_teacher.html", {"request": request, "name": person_name, "post": person_info["post"], "department" : person_info["department"],
                                    "email": person_info["mail"], "answer1": person_info["answer1"], "answer2": person_info["answer2"]
                                    ,"answer3": person_info["answer3"], "answer4": person_info["answer4"], "answer5": person_info["answer5"],
                                    "answer6": person_info["answer6"], "url_for_main": "/main", "url_for_teachers": "/teachers", "url_for_documentation": "/documentation"})

#POST request method
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))

