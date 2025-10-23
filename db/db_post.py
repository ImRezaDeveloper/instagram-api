from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from routers.schemas import PostBase
from db.models import DBpost
import datetime

def create_post(db: Session, request: PostBase):
    new_post = DBpost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.user_id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(DBpost).all()

def delete_post(db: Session, id: int):
    post = db.query(DBpost).filter(DBpost.id == id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail=f'there is no post with this id : {id}')
    
    db.delete(post)
    db.commit()
    return post