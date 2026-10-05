from sqlmodel import create_engine , SQLModel


sqlite_url = "sqlite:///microblog.db"
engine = create_engine(sqlite_url)