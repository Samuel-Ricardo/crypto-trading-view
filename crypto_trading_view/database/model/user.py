from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from index import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    favorites = relationship('Favorite', backref='user', lazy='subquery')