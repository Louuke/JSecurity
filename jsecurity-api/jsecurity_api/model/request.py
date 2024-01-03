from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=256)
