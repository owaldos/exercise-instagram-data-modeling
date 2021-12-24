import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_to = Column(Integer)
    user_from = Column(Integer)


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    like = Column(Integer)
       

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250))
    tag = Column(String(250))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    likes = relationship(Likes)


class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media) 
      

class Profiles(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    biography = Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)
    user_to_id = Column(Integer, ForeignKey('followers.id'))
    follower = relationship(Followers)
    user_from_id = Column(Integer, ForeignKey('followers.id'))
    follower= relationship(Followers)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
