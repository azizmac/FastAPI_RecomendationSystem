from fastapi import FastAPI

app = FastAPI()

# Include routes
from src.API.v1.endpoints import router
app.include_router(router)

# Setup database
from src.db.database import init_db
init_db()