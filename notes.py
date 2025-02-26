class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteBook:
    def __init__(self):
        self.notes = []

    def add(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def search(self, term):
        matches = []
        for note in self.notes:
            if term.lower() in note.content.lower():
                matches.append(note.title)
        return matches

    def retrieve_note(self, title):
        for note in self.notes:
            if note.title.lower() == title.lower():
                return note
    
    def all_notes(self):
        return self.notes