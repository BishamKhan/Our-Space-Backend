from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password


def create_user(db: Session, user):
    user = User(
        username= user.username,
        email= user.email,
        full_name= user.full_name,
        password=hash_password(user.password),
        gender=user.gender,
        date_of_birth=user.date_of_birth,

        profile_image=user.profile_image,
        cover_image=user.cover_image
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_all_users(db: Session):
    return db.query(User).all()


def update_profile_pic(db:Session,user,profile_image_url:str):
    user.profile_image = profile_image_url

    db.commit()
    db.refresh(user)
    return user

def update_user_profile(db: Session, user: User, data):
    if data.full_name is not None:
        user.full_name = data.full_name

    if data.bio is not None:
        user.bio = data.bio

    if data.date_of_birth is not None:
        user.date_of_birth = data.date_of_birth

    if data.username is not None:
        user.username = data.username

    if data.email is not None:
        user.email = data.email

    db.commit()
    db.refresh(user)
    return user


def getUserInfo(db:Session, user):
    return db.query(User).filter(user.id == User.id).first()