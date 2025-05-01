from pydantic import BaseModel
from typing import Optional

class RegistrationResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    checked_in: bool

    class Config:
        orm_mode = True

class QRCheckin(BaseModel):
    user_id: int
    event_id: int
