from pydantic import BaseModel

class StoryCreate(BaseModel):
    title: str
    story: str

class StoryRead(BaseModel):
    id: int
    title: str
    story: str
