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
    id_multimedia: int

class InsertArticles(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    title: str
    author: str
    source: str
    summary: str
    
class UpdateArticles(BaseModel):
    id_article: int
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    author: Optional[str] = None
    source: Optional[str] = None
    summary: Optional[str] = None

class DeleteArticles(BaseModel):
    id_article: int
    id_river: int