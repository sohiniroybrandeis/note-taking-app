import streamlit as st


# Initialize session state correctly
if "notes" not in st.session_state:
    st.session_state.notes = []
if "titles" not in st.session_state:
    st.session_state.titles = []
if "contents" not in st.session_state:
    st.session_state.contents = []

st.title("NoteBook")
st.markdown("Feel free to add and search for notes!")

# Search functionality
query = st.text_input("Search", "")
if st.button("Search"):
    if query:
        st.write("#### Search Results:")
        results = [
            note for note in st.session_state.notes 
            if query.lower() in note["content"].lower()
        ]

        if results:
            for note in results:
                st.write(f"- **{note['title']}**")  # Displays matched titles
        else:
            st.warning("No matching notes found.")

# Input fields for adding a note
title = st.text_input("Title")
content = st.text_area("Content")

# Button to add note
if st.button("Add"):
    if title:  # Ensure title is not empty
        note = {"title": title, "content": content}
        st.session_state.notes.append(note)
        st.session_state.titles.append(title)
        st.session_state.contents.append(content)
        st.rerun()  # Refresh UI to update sidebar

# Sidebar with notes
with st.sidebar:
    st.write("### Your Notes")
    if st.session_state.titles:
        selected_note = st.selectbox('Select a note:', st.session_state.titles)

        # Display selected note content
        if selected_note:
            index = st.session_state.titles.index(selected_note)
            st.write(f"**Title:** {selected_note}")
            st.write(f"**Content:** {st.session_state.contents[index]}")