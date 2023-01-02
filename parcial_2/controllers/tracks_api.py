from http.client import HTTPException
from fastapi import APIRouter,  Depends, HTTPException, status
from repositories.music_repository import MusicRepository
from schemas.schemas import TrackInDB
from typing import List
from sqlalchemy.orm import Session
from dependencies import get_music_repo, get_db

router = APIRouter(
    prefix="/song",
    tags=["Song"])


@router.get("/{id}", response_model=TrackInDB, status_code=status.HTTP_200_OK)
async def get_track_detail_by_id(
    id: int,
    db: Session = Depends(get_db),
    music_repo: MusicRepository = Depends(get_music_repo),
) -> TrackInDB:
    track = await music_repo.get_track_by_id(id=id, db=db)
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return track
