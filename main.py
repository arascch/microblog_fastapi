from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from database import engine
from models import User , Post

app = FastAPI()

SQLModel.metadata.create_all(engine)