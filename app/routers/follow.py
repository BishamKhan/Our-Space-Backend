from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.follow import follow_user, get_followers, get_following, unfollow_user
from app.core.security import get_current_user

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/{user_id}")
def follow(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    follow_user(db, current_user.id, user_id)
    return {"message": "User followed successfully"}

@router.delete("/{user_id}")
def unfollow(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    unfollow_user(db, current_user.id, user_id)
    return {"message": "User unfollowed successfully"}

@router.get("/followers/{user_id}")
def followers(user_id: int, db: Session = Depends(get_db)):
    return get_followers(db, user_id)


@router.get("/following/{user_id}")
def following(user_id: int, db: Session = Depends(get_db)):
    return get_following(db, user_id)
