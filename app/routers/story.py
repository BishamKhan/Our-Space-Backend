from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from app.db.database import get_db
from app.schemas.story import CreateStory, StoryResponse, SingleStoryResponse
from app.crud.story import StoryCreate, get_story, get_all_stories
from app.core.security import get_current_user
from app.models.posts import Post

router = APIRouter(
    prefix="/story",
    tags=["Story"]
)


@router.post("/", response_model=SingleStoryResponse, status_code=status.HTTP_201_CREATED)
def create_story(story: CreateStory , db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_story= StoryCreate(db, user_id=current_user.id, data=story)
    return new_story

@router.get("/user", response_model=StoryResponse, status_code=status.HTTP_200_OK)
def get_user_stories(db:Session= Depends(get_db), current_user=Depends(get_current_user)):
    gets = get_story(db,current_user)
    return gets

@router.get("/all", response_model=List[StoryResponse], status_code=status.HTTP_200_OK)
def all_stories(db:Session= Depends(get_db), current_user=Depends(get_current_user)):
    gets = get_all_stories(db,current_user)
    return gets