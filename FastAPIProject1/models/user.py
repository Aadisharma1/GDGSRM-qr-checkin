
from sqlalchemy import Column, String, Integer, Enum
from app.database import Base
import enum

class RoleEnum(str, enum.Enum):
    student = "student"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    student_id = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.student)
