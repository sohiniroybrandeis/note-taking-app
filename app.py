import os
from flask import Flask, render_template, request, redirect, url_for
from notes import Note, NoteBook

app = Flask(__name__)

nb = NoteBook()

@app.route('/', methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        note = request.form.get("note")  #receives input
        entry = request.form.get("content")
        if note:
            nb.add(note, entry)
        return redirect(url_for('page'))  #refresh
    
    search = request.args.get("search")  #receives input
    matched_notes = []
    if search:
        matched_notes = nb.search(search)
    return render_template('base.html', notes=nb.notes, matched_notes=matched_notes)  #pass to template

@app.route('/note/<mn>')
def notepage(mn):
    note = nb.retrieve_note(mn)
    if note:
        return render_template('note.html', title=note.title, content=note.content)
    return "Note not found", 404

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)