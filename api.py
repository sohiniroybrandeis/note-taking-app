from typing import Union
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request
from markupsafe import escape
from pydantic import BaseModel
import os

app = FastAPI()
notes = [] #storing notes

class Note(BaseModel):
    name: str
    content: str


@app.post("/add", status_code=201)
async def create_note(note: Note):
    notes.append(note)
    return ("You have successfully added a note!")


@app.get("/")
def read_root():
    return {
        "message": "Hello! In order to use the API, use the following commands:",
        "endpoints": {
            "/": "Read the instructions.",
            "/list": "Access all the added notes.",
            "/find?term=<insert term>": "Find all notes with the search term.",
            "/note/<title>": "Retrieve the content of a note with a specified title.",
        }
    }

@app.get("/list", response_model=list[Note])
async def get_all_notes():
    return notes


@app.get("/find")
# dictionary including all notes that match the search term
async def find_note(term: str):
    matched_notes = []
    if term:
        for note in notes:
            if term.lower() in (note.content).lower():
                matched_notes.append(note.name)
    return {"term": term, "matched_notes": matched_notes}


@app.get("/note/{title}")
# retrieves the text from a specific note.
async def note_text(title: str):
    if title:
        for note in notes:
            if title == (note.name):
                return note.content

