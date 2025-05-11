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
    created_at: Optional[datetime]
    title: Optional[str]
    author: Optional[str]
    publication_year: Optional[str]
    summary: Optional[str]

class DeleteLiterature(BaseModel):
    id_literature: int
    id_river: int
    id_multimedia: int