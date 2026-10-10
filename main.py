from fastapi import FastAPI , Request ,Form
from fastapi.responses import RedirectResponse
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

@app.post("/create")
def create_post(content:str = Form(...) , user_id:int=Form(...)):
    with Session(engine) as session:    
        new_post = Post(content=content , user_id = user_id)
        session.add(new_post)
        session.commit()
    return RedirectResponse(url="/" , status_code=303)


@app.post("/delete/{post_id}")
def delete_post(post_id:int):
    with Session(engine) as session:
        post_to_delete = session.get(Post , post_id)
        if post_to_delete:
            session.delete(post_to_delete)
            session.commit()

        return RedirectResponse(url="/" , status_code = 303)

@app.post("/update/{post_id}")
def update_post(post_id:int , new_content:str=Form(...)):
    with Session(engine) as session:
        post_to_edit = session.get(Post , post_id)

        if post_to_edit:
            post_to_edit.content = new_content
            session.add(post_to_edit)
            session.commit()
    return RedirectResponse(url="/" , status_code=303)