### File structure:
- notes.py: Contains a notebook module that is imported into each framework to carry out notebook functions.
- stream.py: Streamlit application that can create, add, or search for a note, as well as display them.
- app.py: Flask application that can opens up a mini-website to create, add, or search for a note, as well as display them.
- api.py: FastAPI provides an API to the notes using endpoints that are specified upon running it.
- requirements.txt
- static (directory)
  -   styles.css: CSS styles for Flask application.
- templates (directory)
  - base.html: Base HTML file for website
  - note.html: HTML file to display webpage with individual note, extends Base file.

To run:
### The API
uvicorn api:app --reload

### The Website
python app.py

### The streamlit application
streamlit run stream.py
