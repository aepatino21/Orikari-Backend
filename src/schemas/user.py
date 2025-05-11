from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    created_at: datetime
    name: str
    correo: str
    password: str
    rol: str
    is_expert: bool
    
class UserGet(BaseModel):
    id: int
    username: str
    created_at: datetime
    name: str
    correo: str
    rol: str
    is_expert: bool

class UserCreate(BaseModel):
    username: str
    name: str
    correo: str
    password: str
    rol: str
    is_expert: bool

class UserUpdate(BaseModel):
    username: str
    name: str
    correo: str
    password: str
    rol: str

class UserDelete(BaseModel):
    id: int
    username: str
    created_at: datetime
    name: str
    correo: str
    password: str
    rol: str
    is_expert: bool