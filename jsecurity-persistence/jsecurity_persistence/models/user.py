from beanie import Document
from pydantic import EmailStr, BaseModel
from typing import Optional


class User(Document):
    email: EmailStr
    password: str
    is_active: bool = False
    role: str = 'user'

    class Settings:
        name = 'users'
        indexes = ['email']


class UpdateUser(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]
    role: Optional[str]
