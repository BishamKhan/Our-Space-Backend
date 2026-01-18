from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    # Optional additional fields
    full_name = Column(String(100), nullable=True)
    bio = Column(String(255), nullable=True)
    profile_image = Column(String(255), nullable=True)
    cover_image = Column(String(255), nullable=True)   
    date_of_birth = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    gender = Column(String(20), nullable=True)
    followers_count = Column(Integer, default=0, nullable=False)
    following_count = Column(Integer, default=0, nullable=False)

    posts = relationship("Post", back_populates="user")
    likes = relationship("Like", back_populates="user")
    comments = relationship("Comment", back_populates="user")