from fastapi import FastAPI , Request
from sqlmodel import SQLModel, create_engine , Session,select
from database import engine
from models import User , Post
from fastapi.templating import Jinja2Templates

app = FastAPI()

SQLModel.metadata.create_all(engine)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def show_feed(request:Request):
    with Session(engine) as session:
        statement = select(Post)
        posts = session.exec(statement).all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"posts":posts}
    )