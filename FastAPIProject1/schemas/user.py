
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class RoleEnum(str, Enum):
    student = "student"
    admin = "admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    student_id: Optional[str] = None
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    student_id: Optional[str]
    role: RoleEnum

    class Config:
        orm_mode = True
