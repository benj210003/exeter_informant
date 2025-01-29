# main.py
from fastapi import FastAPI
from server.models import StoryCreate
from server.models import StoryRead
from server.database import db_init
from server.database import db_connection

db_init()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Exeter Informant"}

@app.post("/stories/")
def create_story(story_data: StoryCreate):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO stories (title, story) VALUES (?, ?)",
        (story_data.title, story_data.story)
    )

    conn.commit()
    id = cursor.lastrowid
    conn.close()

    return StoryRead(id = id, title = story_data.title, story = story_data.story)

@app.get("/stories/")
def get_stories():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM stories",
    )
    
    rows = cursor.fetchall()
    conn.close()

    return [StoryRead(id=story[0], title=story[1], story=story[2]) for story in rows]

@app.put("/stories/{story_id}")
def edit_story(story_id: int, story_data: StoryCreate):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE stories SET title = ?, story = ? WHERE id = ?",
        (story_data.title, story_data.story, story_id,)
    )

    conn.commit()
    conn.close

    return StoryRead(id=story_id, title=story_data.title, story=story_data.title)

@app.delete("/stories/{story_id}")
def delete_story(story_id: int):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM stories WHERE id = ?",
        (story_id,)
    )

    conn.commit()
    conn.close()

    return {"message": f"Story {story_id} deleted succesfully"}