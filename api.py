from typing import Union
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request
from markupsafe import escape
from pydantic import BaseModel
import os
from notes import Note, NoteBook

app = FastAPI()
nb = NoteBook()


class Note(BaseModel):
    name: str
    content: str

@app.post("/add", status_code=201)
async def create_note(note: Note):
    nb.add(note.name, note.content)
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

@app.get("/list", response_model=[])
async def get_all_notes():
    return nb.notes


@app.get("/find")
# dictionary including all notes that match the search term
async def find_note(term: str):
    if term:
        matched_notes = nb.search(term)
    return {"term": term, "matched_notes": matched_notes}


@app.get("/note/{title}", response_model=str)  # Ensure correct serialization
async def note_text(title: str):
    note = nb.retrieve_note(title)
    if note:
        return note.content  # Return full Note object (FastAPI will convert it to JSON)
    return "Error: Note not found"  # Handle missing notes


