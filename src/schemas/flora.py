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
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    scientific_name: Optional[str] = None
    description: Optional[str] = None
    importance: Optional[str] = None

class DeleteFlora(BaseModel):
    id_plant: int
    id_river: int
    id_multimedia: int
