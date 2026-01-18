from sqlalchemy.orm import Session
from app.models.comments import Comment
from app.models.posts import Post
from fastapi import APIRouter, Depends, HTTPException, status

def create_comment(db: Session, user_id: int, post_id: Post, content:str ):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # existing = db.query(Comment).filter(Like.user_id==user_id, Like.post_id==post.id).first()
    # if existing:
    #     return existing

    commentIt = Comment(
        content=content,
        user_id=user_id, post_id=post_id)
    post.comments_count += 1
    db.add(commentIt)
    db.commit()
    db.refresh(commentIt)
    return commentIt

def Get_comment(db:Session,current_user,post_id):
    Comments = db.query(Comment).filter(Post.id == post_id).first()

    if not Comments:
        raise HTTPException(status_code=404, detail="No comments found")
    
    return Comments

# def remove_like(db: Session, user_id: int, post: Post):
#     like = db.query(Like).filter(Like.user_id==user_id, Like.post_id==post.id).first()
#     if like:
#         post.likes_count -= 1
#         db.delete(like)
#         db.commit()
#     return like
