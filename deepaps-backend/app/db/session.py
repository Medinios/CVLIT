import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import env

engine = create_engine(
    f"postgresql://{env.db_username}:{env.db_password}@{env.db_host}/")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
