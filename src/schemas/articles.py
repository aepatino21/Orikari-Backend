from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Articles(BaseModel):
    id_article: int
    created_at: datetime
    title: str
    author: str
    source: str
    summary: str
    id_river: int

class InsertArticles(BaseModel):
    id_river: int
    created_at: datetime
    title: str
    author: str
    source: str
    summary: str
    
class UpdateArticles(BaseModel):
    id_river: int
    created_at: Optional[datetime]
    title: Optional[str]
    author: Optional[str]
    source: Optional[str]
    summary: Optional[str]

class DeleteArticles(BaseModel):
    id_article: int
    id_river: int