import uvicorn
from fastapi import FastAPI
from database import engine, Base
import routers

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(routers.router, prefix="/document")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
