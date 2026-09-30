from pydantic import BaseModel
from typing import List

class Panel(BaseModel):
    title: str
    description: str
    dialogue: str = ""
    image_prompt: str

class ComicOutline(BaseModel):
    title: str
    character_name: str
    panels: List[Panel]

class PromptRequest(BaseModel):
    prompt: str
    character_name: str = "Hero"
    setting: str = "World"
    tone: str = "heroic"
    style: str = "comic"
    model_config = {"extra": "allow"}
