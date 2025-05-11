from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Multimedia(BaseModel):
    id: int
    created_at: datetime
    bucket_path: str
    object_path: str
    url: str
    name: str
    extension: str
    
class InsertMultimedia(BaseModel):
    created_at: datetime
    bucket_path: str
    object_path: str
    url: str
    name: str
    extension: str
    

class UpdateMultimedia(BaseModel):
    id: int
    created_at: Optional[datetime]
    bucket_path: Optional[str]
    object_path: Optional[str]
    url: Optional[str]
    name: Optional[str]
    extension: Optional[str]


class DeleteMultimedia(BaseModel):
    id: int