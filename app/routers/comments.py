from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.comments import create_comment, Get_comment
# from app.crud.posts import get_feed
from app.models.user import User
from app.models.posts import Post
from app.schemas.posts import LikeResponse
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/comment", tags=["Comments"])

@router.post("/{post_id}", response_model=LikeResponse)
def Comment_post(post_id: int, content:str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_comment(db, current_user.id, post_id, content)


@router.get("/{post_id}", response_model=LikeResponse)
def Get_Comment_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return Get_comment(db, current_user.id, post_id)


# @router.delete("/{post_id}", response_model=LikeResponse)
# def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     post = db.query(Post).filter(Post.id==post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return remove_like(db, current_user.id, post)
