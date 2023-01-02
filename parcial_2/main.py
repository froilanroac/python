from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.home_api import router as home_router
from controllers.artists_api import router as artists_api
from controllers.albumes_api import router as albumes_api
from controllers.artist_api import router as artist_api
from controllers.tracks_api import router as tracks_api
from config_db import Base, engine


def get_application():

    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title="Parcial 2",
        description="Music Store API",
        version="0.1.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(home_router, tags=["Home"])
    app.include_router(artists_api, prefix="/music-store/api/v1")
    app.include_router(albumes_api, prefix="/music-store/api/v1")
    app.include_router(artist_api, prefix="/music-store/api/v1")
    app.include_router(tracks_api, prefix="/music-store/api/v1")

    return app


app = get_application()
