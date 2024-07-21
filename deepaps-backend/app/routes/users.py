from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.users import User as User_Schema
from app.models.users import User as User_Model

users_router = APIRouter()


@users_router.get("/", response_model=List[User_Schema])
def get_users(db: Session = Depends(get_db)):
    return db.query(User_Model).all()
