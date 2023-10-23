from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .songs import (
    get_artists_occurences,
    get_songs,
    get_songs_mode_vs_streams,
    get_songs_releasedyear_vs_numsongs,
    get_artists_with_most_streams,
    get_songs_with_most_streams,
    get_songs_from_artist,
)

app = FastAPI()
origins = ["http://localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["Content-Disposition"],
    max_age=600,
)


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/songs")
async def read_songs():
    songs = get_songs()
    return {"total_songs": len(songs), "songs": songs[:10]}


@app.get("/songs/mode-streams")
async def mode_streams():
    data = get_songs_mode_vs_streams()
    total_streams = sum([row["streams"] for row in data])
    data = [dict(row) for row in data]
    for row in data:
        row["name"] = row.pop("mode")
        row["y"] = row.pop("streams") / total_streams

    return {"data": data}


@app.get("/songs/releaseday-numsongs")
async def releaseday_numsongs():
    data = get_songs_releasedyear_vs_numsongs()
    data = [[row[0], row[1]] for row in data]

    return {"data": data}


@app.get("/songs/artist-occurences")
async def artist_occurences():
    data = get_artists_occurences()
    data = [{"name": row[0].lstrip(), "weight": row[1]} for row in data]

    return {"data": data}


@app.get("/songs/artist-moststreams")
async def artist_moststreams():
    data = get_artists_with_most_streams()
    data = [[row[0], row[1]] for row in data]

    return {"data": data}


@app.get("/songs/songs-moststreams")
async def songs_moststreams():
    data = get_songs_with_most_streams()
    data = [[row[0], row[1]] for row in data]

    return {"data": data}


@app.get("/songs/{artist}")
async def songs_artist(artist: str):
    data = get_songs_from_artist(artist)
    data = [[row[0], row[1]] for row in data]
    return {"data": data}
