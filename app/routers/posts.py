from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from app.db.database import get_db
from app.schemas.posts import PostCreate,PostResponse
from app.crud.posts import create_post, get_posts
from app.core.security import get_current_user
from app.models.posts import Post

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_posts(post: PostCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_post = create_post(db, user_id=current_user.id, content=post.content, media_url=post.media_url)
    return new_post

@router.get("/userfeed", response_model=List[PostResponse], status_code=status.HTTP_200_OK)
def get_user_posts(db:Session= Depends(get_db), current_user=Depends(get_current_user)):
    gets = get_posts(db,current_user.id)
    return gets
