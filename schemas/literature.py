from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Literature(BaseModel):
    id_literature: int
    id_river: int
    id_multimedia: int
    created_at: datetime
    title: str
    author: str
    publication_year: Optional[date]
    summary: str

class InsertLiterature(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    title: str
    author: str
    publication_year: Optional[date]
    summary: str

class UpdateLiterature(BaseModel):
    id_literature: int
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[str] = None
    summary: Optional[str] = None

class DeleteLiterature(BaseModel):
    id_literature: int
    id_river: int
    id_multimedia: int