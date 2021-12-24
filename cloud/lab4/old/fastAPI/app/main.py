from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

fake_notes = [{"note_id" : 0,"title":"Title1","text":"Text1"},
              {"note_id" : 1,"title":"Title2","text":"Text2"},
              {"note_id" : 2,"title":"Title3","text":"Text3"},
              {"note_id" : 3,"title":"Title4","text":"Text4"}]


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8080/items",
    "http://127.0.0.1:8080/items/",
    "http://*/",
    "http://127.0.0.1:80/note/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Note(BaseModel):
    note_id: int
    title: str
    text: str
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/note/")
def read_note():
    return fake_notes


@app.post("/note/")
async def create_note(note: Note):
    return note
