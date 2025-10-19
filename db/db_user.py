from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from .models import DBuser

def create_users(db: Session, request: UserBase):
    new_user = DBuser(
        username = request.username,
        email = request.email,
        password = request.password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(DBuser).all()