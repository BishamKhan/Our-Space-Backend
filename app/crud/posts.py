from sqlalchemy.orm import Session
from app.models.posts import Post
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status

def create_post(db: Session, user_id: int, content: str,media_url:str):
    
    add_post = Post(
        user_id=user_id,
        content=content,
        media_url=media_url,
        created_at=datetime.utcnow()
    )

    db.add(add_post)
    db.commit()
    db.refresh(add_post)
    return add_post

def get_posts(db:Session, user_id:int):
    return db.query(Post).filter(user_id == Post.user_id).order_by(Post.created_at.desc()).all()

def get_first_post(db: Session, user_id: int):
    return (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .order_by(Post.created_at.asc())
        .first()
    )