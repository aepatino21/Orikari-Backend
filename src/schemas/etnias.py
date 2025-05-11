from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Etnias(BaseModel):
    id_etnia: int
    id_river: int
    id_multimedia: int
    created_at: datetime
    name: str
    description: str

class InsertEtnias(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    name: str
    description: str

class UpdateEtnias(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime]
    name: Optional[str]
    description: Optional[str]

class DeleteEtnias(BaseModel):
    id_etnia: int
    id_river: int
    id_multimedia: int