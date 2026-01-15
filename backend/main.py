from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.data import mood_data
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()


templates=Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


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
    songs = mood_data.get(mood,[])
    if songs:
        return {"mood": mood, "songs": songs}
    return {"mood": mood, "songs": []}
