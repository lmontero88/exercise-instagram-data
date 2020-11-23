import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    comments = relationship('Comment',back_populates= 'user')
    posts = relationship('Post', back_populates= 'user')
    users_to = relationship('Follower', back_populates='user_to')
    users_from = relationship('Follower', back_populates='user_from')
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer,ForeignKey('user.id'))
    user_to = relationship('User', back_populates= 'users_to')
    user_from = relationship('User', back_populates= 'users_from')

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer,primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('User', back_populates= 'comments' )
    post_id = Column(Integer,ForeignKey('post.post_id'))
    post = relationship('Post', back_populates= 'comments')

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('User', back_populates= 'posts' )
    comments = relationship('Comment', back_populates= 'post')
    medias = relationship( 'MEdia', back_populates= 'posts')

class Media (Base):
    __tablename__ = 'media'
    id_media = Column(Integer,primary_key=True)
    media_type = Column(Integer, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer,ForeignKey('post.post_id'))
    post = relationship('Post,', back_populates= 'posts')
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')