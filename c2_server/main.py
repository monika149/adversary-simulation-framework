from fastapi import FastAPI
from database import Base, engine
from api.endpoints import router as api_router



app = FastAPI(title="Adversary Simulation C2 Server")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "C2 Server is Live!"}


