from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserMultimedia(BaseModel):
    id_user_multimedia: int
    id_user: int
    created_at: datetime
    bucket_path: str
    object_path: str
    url: str
    name: str
    extension: str

class InsertUserMultimedia(BaseModel):
    id_user: int
    created_at: datetime
    bucket_path: str
    object_path: str
    url: str
    name: str
    extension: str

class UpdateUserMultimedia(BaseModel):
    id_user: int
    created_at: Optional[datetime]
    bucket_path: Optional[str]
    object_path: Optional[str]
    url: Optional[str]
    name: Optional[str]
    extension: Optional[str]

class DeleteUserMultimedia(BaseModel):
    id_user_multimedia: int
    id_user: int