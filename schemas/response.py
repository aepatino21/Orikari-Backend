from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Response(BaseModel):
    id_responser: int
    id_foro: int
    id_user: int
    created_at: datetime
    response: str

class InsertResponse(BaseModel):
    id_foro: int
    id_user: int
    created_at: datetime
    response: str

class UpdateResponse(BaseModel):
    id_foro: int
    id_user: int
    created_at: Optional[datetime] = None
    response: Optional[str] = None

class DeleteResponse(BaseModel):
    id_responser: int
    id_foro: int
    id_user: int
