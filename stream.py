import streamlit as st
from notes import Note, NoteBook

# initialize session states

if "notebook" not in st.session_state:
    st.session_state.notebook = NoteBook()

nb = st.session_state.notebook

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
                st.write(f"- **{title}**")
        else:
            st.warning("No matching notes found.")

title = st.text_input("Title")
content = st.text_area("Content")

#add button
if st.button("Add"):
    if title:
        nb.add(title, content)
        st.rerun()  # refresh

# side panel to store notes
with st.sidebar:
    st.write("### Notes")
    if nb.notes:
        selected_title = st.selectbox('Select a note:', [note.title for note in nb.notes])

        if selected_title:
            nt = nb.retrieve_note(selected_title)
            if nt:
                st.write(f"**Title:** {nt.title}")
                st.write(f"**Content:** {nt.content}")