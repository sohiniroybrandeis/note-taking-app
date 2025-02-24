import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = [] #note storage
entries = dict()

@app.route('/', methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        note = request.form.get("note")  #receives input
        entry = request.form.get("content")
        entries[note] = entry
        if note:
            notes.append(note)  #stores note in list
        return redirect(url_for('page'))  #refresh
    
    search = request.args.get("search")  #receives input
    matched_notes = []
    if search:
        for note in notes:
            if search.lower() in note.lower():
                matched_notes.append(note)
    
    return render_template('base.html', notes=notes, matched_notes=matched_notes)  #pass to template

@app.route('/note/<mn>')
def notepage(mn):
    if mn in entries:
        content = entries[mn]
        return render_template('note.html', title=mn, content=content)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)