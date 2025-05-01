from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    date: datetime

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    date: datetime

    class Config:
        orm_mode = True
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    student_id: Optional[str]
    role: RoleEnum
