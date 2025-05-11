from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class River(BaseModel):
    id: int
    id_multimedia: int
    created_at: datetime
    name: str

class InsertRiver(BaseModel):
    id_multimedia: int
    created_at: datetime
    name: str

class UpdateRiver(BaseModel):
    id: int
    id_multimedia: int
    created_at: Optional[datetime]
    name: Optional[str]

class DeleteRiver(BaseModel):
    id: int
    id_multimedia: int