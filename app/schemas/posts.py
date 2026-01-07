from pydantic import BaseModel
from typing import Optional
from datetime import date
from datetime import datetime


class UserInfo(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    bio: Optional[str]
    profile_image: Optional[str] = None
    cover_image: Optional[str] = None

    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    created_at: datetime

    class Config:
        orm_mode = True
        
class PostCreate(BaseModel):
    content: str
    media_url: Optional[str] = None


class PostResponse(BaseModel):
    id:int
    content: str
    media_url: Optional[str] = None
    created_at: datetime  # Pydantic will parse datetime
    user: UserInfo 

    class Config:
        orm_mode = True
