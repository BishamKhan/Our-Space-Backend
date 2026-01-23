from pydantic import BaseModel, field_validator
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


class CreateStory(BaseModel):
    content: Optional[str] = None
    media_url: Optional[str] = None
    bg_color: Optional[str] = None

    @field_validator("content", mode="before")
    @classmethod
    def validate_story(cls, value, info):
        media_url = info.data.get("media_url")


    @field_validator("content", mode="before")
    @classmethod
    def validate_story(cls, value, info):
        media_url = info.data.get("media_url")

        # ❌ neither content nor media
        if not value and not media_url:
            raise ValueError("Either content or media_url is required")

        # ✅ must always return the value
        return value

class SingleStoryResponse(BaseModel):
    id: int
    content: Optional[str]
    media_url: Optional[str]
    bg_color: Optional[str]
    is_photo: bool
    created_at: datetime

    class Config:
        orm_mode = True

class StoryResponse(BaseModel):
    stories:List[SingleStoryResponse]
    user: UserResponse

    class Config:
        orm_mode = True
