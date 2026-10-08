from fastapi import FastAPI , Request,Form
from sqlmodel import SQLModel, create_engine , Session,select
from database import engine
from models import User , Post
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


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

@app.post("/create")
def create_post(content: str = Form(...), user_id: int=Form(...)):
    with Session(engine) as session:
        new_post = Post(content=content , user_id=user_id)
        session.add(new_post)
        session.commit()
    return RedirectResponse(url="/" , status_code=303)