import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites')
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites')


class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites')


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character')
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')
  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
