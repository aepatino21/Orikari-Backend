from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Foro(BaseModel):
    id_post: int
    id_user: int
    content: str
    category: str

class ForoGet(BaseModel):
    id_user: int
    content: str
    created_at: datetime
    category: str

class ForoCreate(BaseModel):
    id_post: int
    id_user: int
    content: str
    created_at: datetime
    category: str
    post_title: str

class ForoUpdate(BaseModel):
    id_post: int
    id_user: int
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    category: Optional[str] = None

class ForoDelete(BaseModel):
    id_post: int
    id_user: int
    content: str
    created_at: datetime
    category: str
