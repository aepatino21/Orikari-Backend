from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Foro(BaseModel):
    id_Comentario: int
    id_Usuario: int
    contenido: str
    categoria: str

class ForoGet(BaseModel):
    id_Comentario: int
    id_Usuario: int
    contenido: str
    created_at: datetime
    categoria: str

class ForoCreate(BaseModel):
    id_Usuario: int
    contenido: str
    created_at: datetime
    categoria: str

class ForoUpdate(BaseModel):
    id_Comentario: int
    id_Usuario: int
    contenido: str
    created_at: datetime
    categoria: str

class ForoDelete(BaseModel):
    id_Comentario: int
    id_Usuario: int
    contenido: str
    created_at: datetime
    categoria: str
