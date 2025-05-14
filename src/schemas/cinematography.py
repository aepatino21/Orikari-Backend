from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cinematography(BaseModel):
    id_movie: int
    id_river: int
    created_at: datetime
    id_multimedia: int
    title: str
    movie_type: str
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
    movie_type: str
    publication_year: datetime
    director: str
    duration: str

class UpdateCinematography(BaseModel):
    id_movie: int
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    movie_type: Optional[str] = None
    publication_year: Optional[datetime] = None
    director: Optional[str] = None
    duration: Optional[str] = None

class DeleteCinematography(BaseModel):
    id_movie: int
    id_river: int
    id_multimedia: int
    