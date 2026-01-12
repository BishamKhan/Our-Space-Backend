from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.like import create_like, remove_like
# from app.crud.posts import get_feed
from app.models.user import User
from app.models.posts import Post
from app.schemas.posts import LikeResponse
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/likes", tags=["Likes"])

@router.post("/{post_id}", response_model=LikeResponse)
def like_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return create_like(db, current_user.id, post)

@router.delete("/{post_id}", response_model=LikeResponse)
def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return remove_like(db, current_user.id, post)
