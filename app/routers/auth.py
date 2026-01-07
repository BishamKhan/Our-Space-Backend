from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate
from app.crud.user import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from app.schemas.user import LoginResponse
from app.models.posts import Post

router = APIRouter(tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    return create_user(db, user)


@router.post("/login",response_model=LoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Total posts of user
    total_post = db.query(Post).filter(Post.user_id == user.id).count()

    # Return user with total_posts
    user_data = user.__dict__.copy()
    user_data["total_post"] = total_post

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer",  "user": user_data}
