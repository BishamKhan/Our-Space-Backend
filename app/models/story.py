from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Story(Base):
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    media_url = Column(String(255), nullable=True)
    bg_color = Column(String(255), nullable=True)
    is_photo = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    
    user = relationship("User", back_populates="story")