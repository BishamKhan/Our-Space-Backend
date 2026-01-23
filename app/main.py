from fastapi import FastAPI
from app.routers import auth, users, posts, feed, like, comments, follow, story # IMPORTANT: import models
from app.db.database import Base, engine
from app.models import user  # import all models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

# 🔹 CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, PUT, DELETE
    allow_headers=["*"],   # Authorization, Content-Type
)

# routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(feed.router)
app.include_router(like.router)
app.include_router(comments.router)
app.include_router(follow.router)
app.include_router(story.router)
