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
    created_at: Optional[datetime] = None
    bucket_path: Optional[str] = None
    object_path: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    extension: Optional[str] = None


class DeleteMultimedia(BaseModel):
    id: int