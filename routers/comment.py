from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import Comment, CommentBase
from db.db_comment import create_comment, get_comment

router = APIRouter(prefix='/comment',tags=['comments'])

@router.get('/{id}')
def get_comments(id: int, db: Session = Depends(get_db)):
    return get_comment(db, id)

@router.post('/create')
def build_comment(request: CommentBase, db: Session = Depends(get_db)):
    return create_comment(db, request)