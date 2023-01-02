from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import AlbumInDB, ArtistBase, TrackInDB
from models.models import Albumes, Artist, Track, MediaType, Genre


class MusicRepository:

    async def get_all_albumes(self, db: Session) -> List[AlbumInDB]:
        blog_list: List[AlbumInDB] = db.query(Albumes).all()
        return blog_list

    async def get_all_albumes_by_artist(self, db: Session, id: int) -> List[AlbumInDB]:
        blog_list: List[AlbumInDB] = db.query(
            Albumes).filter(Albumes.ArtistId == id).all()
        return blog_list

    async def get_all_artist(self, db: Session) -> List[ArtistBase]:
        blog_list: List[ArtistBase] = db.query(Artist).all()
        return blog_list

    async def get_artist_by_id(self, *, id: int, db: Session) -> ArtistBase:
        artist: ArtistBase = db.query(Artist).get(id)
        return artist

    async def get_tracks_by_album(self, *, id: int, db: Session) -> List[TrackInDB]:
        songs: List[TrackInDB] = db.query(
            Track).filter(Track.AlbumId == id).all()
        return songs

    async def get_tracks_by_artist(self, *, id: int, db: Session) -> List[TrackInDB]:
        songs: List[TrackInDB] = db.query(
            Track).join(Albumes, Track.AlbumId == Albumes.AlbumId).filter(Albumes.ArtistId == id).all()
        return songs

    async def get_track_by_id(self, *, id: int, db: Session) -> TrackInDB:
        song: TrackInDB = db.query(Track).get(id)
        genre: Genre = db.query(Genre).get(song.GenreId)
        media_type: MediaType = db.query(MediaType).get(song.MediaTypeId)
        song.Genre = str(genre.Name) if genre else None
        song.MediaType = str(media_type.Name) if media_type else None
        return song
