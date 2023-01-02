from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def api_home() -> None:
    return {"message": "Welcome to the Music Store API"}
