from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Multimedia(BaseModel):
    id: int
    created_at: datetime
    bucket_path: str
    object_path: str
    url: str
    
class MultimediaGet(BaseModel):
    bucket_path: str
    object_path: str
    url: str

class MultimediaCreate(BaseModel):
    bucket_path: str
    object_path: str
    url: str
    created_at: datetime

class MultimediaUpdate(BaseModel):
    id: int
    bucket_path: str
    object_path: str
    url: str
    created_at: datetime

class MultimediaDelete(BaseModel):
    id: int
    bucket_path: str
    object_path: str
    url: str
    created_at: datetime