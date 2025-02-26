import streamlit as st
from notes import Note, NoteBook

if "notebook" not in st.session_state:
    st.session_state.notebook = NoteBook()
nb = st.session_state.notebook  # Use the session-stored notebook


# initialize session states
if "notes" not in st.session_state:
    st.session_state.notes = []
if "titles" not in st.session_state:
    st.session_state.titles = []

st.title("NoteBook")
st.markdown("Feel free to add and search for notes!")

#search button
query = st.text_input("Search", "")
if st.button("Search"):
    if query:
        st.write("#### Search Results:")
        results = nb.search(query)

        if results:
            for title in results:
                st.write(f"- **{title}**")  # Displays matched titles
        else:
            st.warning("No matching notes found.")

title = st.text_input("Title")
content = st.text_area("Content")

#add button
if st.button("Add"):
    if title:
        nb.add(title, content)
        st.session_state.notes = nb.notes
        st.session_state.titles.append(title)
        st.rerun()  # refresh

# side panel to store notes
with st.sidebar:
    st.write("### Notes")
    if nb.notes:  # Check if there are notes
        selected_title = st.selectbox('Select a note:', [note.title for note in nb.notes])

        if selected_title:
            note_obj = nb.retrieve_note(selected_title)  # Get the note object
            if note_obj:
                st.write(f"**Title:** {note_obj.title}")
                st.write(f"**Content:** {note_obj.content}")