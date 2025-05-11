from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Society(BaseModel):
    id: int
    id_river: int
    id_multimedia: int
    created_at: datetime
    title: str
    description: str
    category: str

class InsertSociety(BaseModel):
    id_river: int
    id_multimedia: int
    created_at: datetime
    title: str
    description: str
    category: str

class UpdateSociety(BaseModel):
    id: int
    id_river: int
    id_multimedia: int
    created_at: Optional[datetime]
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]

class DeleteSociety(BaseModel):
    id: int