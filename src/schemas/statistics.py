from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Statistics(BaseModel):
    id: int
    created_at: datetime
    name: str
    value: float

class ShowStatistics(BaseModel):
    id: int
    id_river: int
    created_at: datetime
    name: str
    value: float

class InsertStatistics(BaseModel):
    id_river: int
    created_at: datetime
    name: str
    value: float

class UpdateStatistics(BaseModel):
    id: int
    id_river: int
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    value: Optional[float] = None

class DeleteStatistics(BaseModel):
    id: int
    id_river: int