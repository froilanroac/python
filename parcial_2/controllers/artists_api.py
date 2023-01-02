from http.client import HTTPException
from fastapi import APIRouter,  Depends, HTTPException, status
from repositories.music_repository import MusicRepository
from schemas.schemas import AlbumInDB, ArtistBase, ArtistInDB
from typing import List
from sqlalchemy.orm import Session
from dependencies import get_music_repo, get_db

router = APIRouter(
    prefix="/singers",
    tags=["Singers"],
)


@router.get("/", response_model=List[ArtistInDB], status_code=status.HTTP_200_OK)
async def get_all_artist(
    db: Session = Depends(get_db),
    music_repo: MusicRepository = Depends(get_music_repo),
) -> List[ArtistInDB]:
    artist = await music_repo.get_all_artist(db=db)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return artist


@router.get("/{id}", response_model=List[AlbumInDB], status_code=status.HTTP_200_OK)
async def get_albumes_by_artist(
    id: int,
    db: Session = Depends(get_db),
    music_repo: MusicRepository = Depends(get_music_repo),
) -> ArtistBase:
    albumes = await music_repo.get_all_albumes_by_artist(db=db, id=id)
    if not albumes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return albumes
