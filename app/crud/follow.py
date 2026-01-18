from sqlalchemy.orm import Session
from app.models.follow import Follow
from app.models.user import User
from fastapi import HTTPException, status


def follow_user(db: Session, follower_id: int, following_id: int):
    if follower_id == following_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot follow yourself"
        )

    existing = db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.following_id == following_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already following"
        )

    follow = Follow(
        follower_id=follower_id,
        following_id=following_id
    )

    db.add(follow)

    db.query(User).filter(User.id == follower_id).update({
        User.following_count: User.following_count + 1
    })

    db.query(User).filter(User.id == following_id).update({
        User.followers_count: User.followers_count + 1
    })

    db.commit()
    return follow


def unfollow_user(db: Session, follower_id: int, following_id: int):
    follow = db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.following_id == following_id
    ).first()

    if not follow:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not following"
        )

    db.delete(follow)

    db.query(User).filter(User.id == follower_id).update({
        User.following_count: User.following_count - 1
    })

    db.query(User).filter(User.id == following_id).update({
        User.followers_count: User.followers_count - 1
    })

    db.commit()


def get_followers(db: Session, user_id: int):
    return (
        db.query(User)
        .join(Follow, Follow.follower_id == User.id)
        .filter(Follow.following_id == user_id)
        .all()
    )


def get_following(db: Session, user_id: int):
    return (
        db.query(User)
        .join(Follow, Follow.following_id == User.id)
        .filter(Follow.follower_id == user_id)
        .all()
    )
