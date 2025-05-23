from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class River(BaseModel):
    id: int
    created_at: datetime
    name: str

class InsertRiver(BaseModel):
    created_at: datetime
    name: str

class UpdateRiver(BaseModel):
    id: int
    created_at: Optional[datetime] = None
    name: Optional[str] = None

class DeleteRiver(BaseModel):
    id: int