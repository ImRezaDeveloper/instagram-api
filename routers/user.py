from db.db_user import create_users, get_users
from sqlalchemy.orm.session import Session
from routers.schemas import UserBase, UserDisplay
from db.models import DBuser
from fastapi import APIRouter, Depends
from db.database import get_db


router = APIRouter(prefix='/user', tags=['user'])

@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return create_users(db, request)

@router.get('/')
def get_user(db: Session = Depends(get_db)):
    return get_users(db)