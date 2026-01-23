from sqlalchemy.orm import Session
from app.models.story import Story
from datetime import datetime, timedelta
from collections import defaultdict
from app.models.user import User

def StoryCreate(db: Session, user_id: int, data):
    isPhoto = True if data.media_url else False
    add_story = Story(
        user_id= user_id,
        content=  data.content,
        media_url= data.media_url,
        bg_color=data.bg_color,
        is_photo= isPhoto,
        created_at=datetime.utcnow()
    )

    db.add(add_story)
    db.commit()
    db.refresh(add_story)
    return add_story

def get_story(db:Session, user):
    time_limit = datetime.utcnow() - timedelta(minutes=5)
    stories =db.query(Story).filter(user.id == Story.user_id, Story.created_at >= time_limit).order_by(Story.created_at.desc()).all()
    
    if not stories:  # No stories found
        return {"user": user, "stories": []}
    
    return {
        "user": user,
        "stories": stories
    }

def get_all_stories(db:Session, user:int):
    time_limit = datetime.utcnow() - timedelta(hours=15)
    stories = (
        db.query(Story)
        .filter(Story.user_id != user.id, Story.created_at >= time_limit)   # exclude logged-in user
        .order_by(Story.created_at.desc())
        .all()
    )

    if not stories:
        return []

    grouped_stories = defaultdict(list)

    for story in stories:
        grouped_stories[story.user_id].append(story)

    response = []

    for user_id, user_stories in grouped_stories.items():
        user = db.query(User).filter(User.id == user_id).first()

        response.append({
            "user": user,
            "stories": user_stories
        })

    return response
