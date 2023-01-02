from sqlalchemy import Boolean, Column, DateTime, Integer, String, Float
from config_db import Base


class Albumes(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(Integer)


class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)


class Track(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)


class Genre(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)


class MediaType(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
