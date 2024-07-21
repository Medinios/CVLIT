from pydantic import BaseModel, EmailStr
from typing import List
from uuid import UUID
from datetime import date


class UserBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID
    createdAt: date
    updatedAt: date

    class Config:
        orm_mode = True
