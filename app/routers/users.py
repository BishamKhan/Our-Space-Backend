from fastapi import APIRouter, Depends,status, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserLoginResponse, UserUpdate, UpdateProfileImage, UpdateCoverImage, UserSearchResponse, UserProfileResponse
from app.crud.user import get_all_users, update_profile_pic,update_cover_pic, update_user_profile, getUserInfo, SearchUser, get_user_by_username
from app.crud.posts import get_first_post
from app.core.security import get_current_user
from app.models.user import User
from app.models.follow import Follow

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserLoginResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_users(db)

@router.put("/updateProfilePic", response_model=UserLoginResponse)
def updatePic(data: UpdateProfileImage,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return update_profile_pic(db,current_user,data.profile_image)

@router.put("/coverPic", response_model=UserLoginResponse)
def updateCover(data: UpdateCoverImage,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return update_cover_pic(db,current_user,data.cover_image)

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

@router.get("/search", response_model=list[UserSearchResponse])
def search_users(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    return SearchUser(db, q)

@router.get("/{username}", response_model=UserProfileResponse)
def get_user_profile(username: str, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
    user = get_user_by_username(db, username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if current_user follows this user
    follow_relation = db.query(Follow).filter(
        Follow.follower_id == current_user.id,
        Follow.following_id == user.id
    ).first()

    follows = True if follow_relation else False

    first_post = get_first_post(db, user.id)

    return {
        "id":user.id,
        "username": user.username,
        "full_name": user.full_name,
        "bio": user.bio,
        "profile_image": user.profile_image,
        "follows":follows,
        "cover_image": user.cover_image,
        "first_post": first_post
    }