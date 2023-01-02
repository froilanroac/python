from datetime import datetime
from typing import Text
from pydantic import BaseModel
from pydantic.schema import Optional


class AlbumBase(BaseModel):

    AlbumId: int
    Title: str
    ArtistId: int


class AlbumInDB(AlbumBase):

    AlbumId: int
    Title: str
    ArtistId: int

    class Config:
        orm_mode = True


class ArtistBase(BaseModel):

    ArtistId: int
    Name: str


class ArtistInDB(ArtistBase):

    ArtistId: int
    Name: str

    class Config:
        orm_mode = True


class TrackBase(BaseModel):

    TrackId: int
    Name: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: Optional[str]
    Milliseconds: int
    Bytes: int
    UnitPrice: float


class TrackInDB(TrackBase):

    TrackId: int
    Name: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: Optional[str]
    Milliseconds: int
    Bytes: int
    UnitPrice: float

    class Config:
        orm_mode = True
