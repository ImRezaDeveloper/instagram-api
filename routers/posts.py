from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import PostDisplay, PostBase
from db.db_post import create_post

router = APIRouter(prefix='/posts', tags=['posts'])

image_url_types = ['relative', 'absolute']

@router.post('/', response_model=PostDisplay)
def bulid_post(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail='Parameter image_url_type can only take a values relative or absolute')
    return create_post(db, request)