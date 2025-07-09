from typing import Literal, Optional
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str
    label: Literal["draft", "in_progress", "scheduled", "published"]
    date: str
    schedule: str


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    label: Optional[Literal["draft", "in_progress", "scheduled", "published"]] = None
    date: Optional[str] = None
    schedule: Optional[str] = None
