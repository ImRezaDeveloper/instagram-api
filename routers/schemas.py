import datetime
from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        orm_mode=True
        
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    user_id: int

# for postDisplay
class User(BaseModel):
    username: str
    class Config:
        orm_mode=True
        
# for postDisplay
class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime.datetime
    class Config:
        orm_mode=True
                
class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime.datetime
    user: User
    comments: List[Comment]
    class Config:
        orm_mode=True
        
class UserAuth(BaseModel):
    id: int
    username: str
    email: str
        
class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int