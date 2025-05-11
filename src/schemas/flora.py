from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Flora(BaseModel):
    id_plant: int
    id_river: int
    id_multimedia: int
    created_at: datetime
    name: str
    scientific_name: str
    description: str
    importance: str

class InsertFlora(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    name: str
    scientific_name: str
    description: str
    importance: str

class UpdateFlora(BaseModel):
    id_plant: int
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime]
    name: Optional[str]
    scientific_name: Optional[str]
    description: Optional[str]
    importance: Optional[str]

class DeleteFlora(BaseModel):
    id_plant: int
    id_river: int
    id_multimedia: int