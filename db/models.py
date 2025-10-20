from .database import Base
from sqlalchemy import DateTime, ForeignKey, Integer, Column, String
from sqlalchemy.orm import relationship

class DBuser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DBpost', back_populates='user')
    
class DBpost(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))  # 🔧 اینجا درست شد
    user = relationship('DBuser', back_populates='items')
