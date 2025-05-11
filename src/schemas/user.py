from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    created_at: datetime
    name: str
    password: str
    mail: str
    role: str
    icon_url: Optional[str]
    
class InsertUser(BaseModel):
    username: str
    name: str
    correo: str
    password: str
    role: str
    icon_url: Optional[str]

class UpdateUser(BaseModel):
    id: int
    username: Optional[str]
    name: Optional[str]
    correo: Optional[str]
    password: Optional[str]
    role: Optional[str]
    icon_url: Optional[str]

class UserDelete(BaseModel):
    id: int