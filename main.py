from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine , Session,select
from database import engine
from models import User , Post

app = FastAPI()

SQLModel.metadata.create_all(engine)

@app.get("/")
def show_feed():
    with Session(engine) as session:
        statement = select(Post)
        posts = session.exec(statement).all()
