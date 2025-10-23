from sqlalchemy.orm.session import Session
from db.models import DBcomment
from routers.schemas import CommentBase
import datetime

def create_comment(db: Session, request: CommentBase):
    new_comment = DBcomment(
        username = request.username,
        text = request.text,
        post_id = request.post_id,
        timestamp = datetime.datetime.now()
    )
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comment(db: Session, id: int):
    return db.query(DBcomment).filter(DBcomment.id == id).all()