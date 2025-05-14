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
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

class DeleteSociety(BaseModel):
    id: int
    id_river: int
    id_multimedia: int