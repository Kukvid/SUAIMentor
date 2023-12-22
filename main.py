import sys

from fastapi import FastAPI
from routs.route import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static",
                html=True),
    name="static",
)

app.include_router(router)