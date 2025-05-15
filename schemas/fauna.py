from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Fauna(BaseModel):
    id_animal:int
    created_at: datetime
    id_river: int
    id_multimedia: int
    name: str
    scientific_name: str
    description: str
    weight: str
    size: str
    location: str
    diet: str

class InsertFauna(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    name: str
    scientific_name: str
    description: str
    weight: str
    size: str
    location: str
    diet: str

class UpdateFauna(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    scientific_name: Optional[str] = None
    description: Optional[str] = None
    weight: Optional[str] = None
    size: Optional[str] = None
    location: Optional[str] = None
    diet: Optional[str] = None

class DeleteFauna(BaseModel):
    id_animal: int
    id_river: int
    id_multimedia: int
