from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from app.db.database import get_db
from app.schemas.posts import PostCreate,PostResponse
from app.crud.feed import get_feed
from app.core.security import get_current_user

router = APIRouter(
    prefix="/feed",
    tags=["Posts"]
)


@router.get("/", response_model=List[PostResponse], status_code=status.HTTP_200_OK)
def get_user_feed(db:Session= Depends(get_db), current_user=Depends(get_current_user)):
    gets = get_feed(db)
    if not gets:
        raise HTTPException(status_code=404,detail="No post found")
    return gets
