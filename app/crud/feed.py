from sqlalchemy.orm import Session, joinedload
from app.models.posts import Post
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status


def get_feed(db:Session):
    return db.query(Post).options(joinedload(Post.user)).order_by(Post.created_at.desc()).all()


