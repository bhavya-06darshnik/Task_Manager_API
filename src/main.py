from fastapi import FastAPI
from src.routes import task, user

app = FastAPI(title="Task Manager API")

# Include routers
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])