from http.client import HTTPException
from fastapi import APIRouter,  Depends, HTTPException, status
from repositories.music_repository import MusicRepository
from schemas.schemas import TrackInDB
from typing import List
from sqlalchemy.orm import Session
from dependencies import get_music_repo, get_db

router = APIRouter(
    prefix="/singer",
    tags=["Singer"],
)


@router.get("/{id}", response_model=List[TrackInDB], status_code=status.HTTP_200_OK)
async def get_all_tracks_by_artist(
    id: int,
    db: Session = Depends(get_db),
    music_repo: MusicRepository = Depends(get_music_repo),
) -> List[TrackInDB]:
    albumes = await music_repo.get_tracks_by_artist(db=db, id=id)
    if not albumes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return albumes
