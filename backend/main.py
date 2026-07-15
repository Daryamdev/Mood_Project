
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.data import mood_data

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Настраиваем шаблоны и статику относительно папки backend
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_songs/{mood}")
def get_songs(mood: str):
    songs = mood_data.get(mood, [])
    if songs:
        return {"mood": mood, "songs": songs}
    return {"mood": mood, "songs": []}