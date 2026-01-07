from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserResponse, UserLoginResponse, UserUpdate, UpdateProfileImage
from app.crud.user import get_all_users, update_profile_pic, update_user_profile, getUserInfo
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_users(db)

@router.put("/updateProfilePic", response_model=UserLoginResponse)
def updatePic(data: UpdateProfileImage,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return update_profile_pic(db,current_user,data.profile_image)

@router.put("/updateInfo", response_model=UserLoginResponse, status_code=status.HTTP_200_OK)
def update_profile(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated_user = update_user_profile(db, current_user, data)
    return updated_user

@router.get("/userInfo",response_model=UserLoginResponse)
def get_user_details(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)):
    return getUserInfo(db,current_user)