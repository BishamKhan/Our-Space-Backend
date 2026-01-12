from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from datetime import datetime

class UserResponse(BaseModel):
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

class LikeResponse(BaseModel):
    user: UserResponse
    created_at: datetime

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    content: Optional[str]
    media_url: Optional[str]

class PostResponse(BaseModel):
    id: int
    content: Optional[str]
    media_url: Optional[str]
    created_at: datetime
    likes_count: int
    likes: List[LikeResponse]  # all likers
    user: UserResponse

    class Config:
        orm_mode = True