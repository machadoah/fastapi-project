from fastapi import FastAPI

from app.db.schema import Base, engine
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routes
app.include_router(user.router)
