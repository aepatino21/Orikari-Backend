from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Projects(BaseModel):
    id_project: int
    id_user: int
    id_user_multimedia: int
    created_at: datetime
    title: str
    project: str
    category: str

class InsertProjects(BaseModel):
    id_user: int
    id_user_multimedia: int
    created_at: datetime
    title: str
    project: str
    category: str

class UpdateProjects(BaseModel):
    id_project: int
    id_user: int
    id_user_multimedia: int
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    project: Optional[str] = None
    category: Optional[str] = None

class DeleteProjects(BaseModel):
    id_project: int
    id_user: int
    id_user_multimedia: int
