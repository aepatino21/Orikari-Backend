from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cinematography(BaseModel):
    id_movie: int
    id_river: int
    created_at: datetime
    id_multimedia: int
    title: str
    type: str
    publication_year: datetime
    director: str
    duration: str
    language: str
    description: str

class InsertCinematography(BaseModel):
    id_river: int
    created_at: datetime
    id_multimedia: int
    title: str
    type: str
    publication_year: datetime
    director: str
    duration: str

class UpdateCinematography(BaseModel):
    id_river: int
    created_at: Optional[datetime]
    id_multimedia: Optional[int]
    title: Optional[str]
    type: Optional[str]
    publication_year: Optional[datetime]
    director: Optional[str]
    duration: Optional[str]

class DeleteCinematography(BaseModel):
    id_movie: int
    id_river: int
    id_multimedia: int
    