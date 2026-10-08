from sqlmodel import SQLModel , Field

class User(SQLModel, table=True):
    id : int |None = Field(default=None , primary_key=True)
    username : str

class Post(SQLModel , table=True):
    id: int |None = Field(default=None , primary_key=True)
    content: str
    user_id : int|None = Field(default=None , foreign_key="user.id")