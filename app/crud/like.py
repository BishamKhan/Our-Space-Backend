from sqlalchemy.orm import Session
from app.models.like import Like
from app.models.posts import Post

def create_like(db: Session, user_id: int, post: Post):
    existing = db.query(Like).filter(Like.user_id==user_id, Like.post_id==post.id).first()
    if existing:
        return existing
    like = Like(user_id=user_id, post_id=post.id)
    post.likes_count += 1
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def remove_like(db: Session, user_id: int, post: Post):
    like = db.query(Like).filter(Like.user_id==user_id, Like.post_id==post.id).first()
    if like:
        post.likes_count -= 1
        db.delete(like)
        db.commit()
    return like
