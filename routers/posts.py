from fastapi import Depends, APIRouter, HTTPException, status, File, UploadFile
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import PostDisplay, PostBase
from db.db_post import create_post, get_all_posts
import shutil, os

router = APIRouter(prefix='/posts', tags=['posts'])

image_url_types = ['relative', 'absolute']

@router.post('/', response_model=PostDisplay)
def bulid_post(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail='Parameter image_url_type can only take a values relative or absolute')
    return create_post(db, request)

@router.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    return get_all_posts(db)

@router.post('/upload')
def upload_image(image: UploadFile = File(...)):
    upload_dir = "images"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, image.filename)
    
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {
        'image': image.filename,
        'image_type': image.content_type
    }