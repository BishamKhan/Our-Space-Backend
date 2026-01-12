from pydantic import BaseModel
from datetime import date
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None

    profile_image: Optional[str] = None
    cover_image: Optional[str] = None

class UserLoginResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    bio: Optional[str]
    total_post: Optional[int] =None
    profile_image: Optional[str] = None
    cover_image: Optional[str] = None

    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[date] = None
    username: Optional[str] = None
    email: Optional[str] = None

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserLoginResponse

class UpdateProfileImage(BaseModel):
    profile_image: str