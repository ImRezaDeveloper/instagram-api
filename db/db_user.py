from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from .models import DBuser
from db.hashing import Hash

def create_users(db: Session, request: UserBase):
    new_user = DBuser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(DBuser).all()

def get_user_by_username(db: Session, username: str):
    user = db.query(DBuser).filter(DBuser.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'user with username {username} not found!')