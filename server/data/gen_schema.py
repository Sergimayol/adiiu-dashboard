import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
DATA_DIR = os.path.join(BASE_DIR, "data", "spotify-2023.csv")


class Artist:
    """A class representing an artist. The attributes are as follows:

    * artist_name: Name of the artist
    """

    def __init__(self, artist_name: str):
        self.artist_name = artist_name


class Metadata:
    """A class representing the metadata of a song. The attributes are as follows:

    * released_year: Year when the song was released
    * released_month: Month when the song was released
    * released_day: Day of the month when the song was released
    * streams: Total number of streams on Spotify
    * in_spotify_playlists: Number of Spotify playlists the song is included in
    * in_spotify_charts: Presence and rank of the song on Spotify charts
    * in_apple_playlists: Number of Apple Music playlists the song is included in
    * in_apple_charts: Presence and rank of the song on Apple Music charts
    * in_deezer_playlists: Number of Deezer playlists the song is included in
    * in_deezer_charts: Presence and rank of the song on Deezer charts
    * in_shazam_charts: Presence and rank of the song on Shazam charts
    """

    def __init__(
        self,
        released_year: int,
        released_month: int,
        released_day: int,
        streams: int,
        in_spotify_playlists: int,
        in_spotify_charts: int,
        in_apple_playlists: int,
        in_apple_charts: int,
        in_deezer_playlists: int,
        in_deezer_charts: int,
        in_shazam_charts: int,
    ):
        self.released_year = released_year
        self.released_month = released_month
        self.released_day = released_day
        self.streams = streams
        self.in_spotify_playlists = in_spotify_playlists
        self.in_spotify_charts = in_spotify_charts
        self.in_apple_playlists = in_apple_playlists
        self.in_apple_charts = in_apple_charts
        self.in_deezer_playlists = in_deezer_playlists
        self.in_deezer_charts = in_deezer_charts
        self.in_shazam_charts = in_shazam_charts


class Extra:
    """A class representing the extra information of a song. The attributes are as follows:

    * bpm: Beats per minute, a measure of song tempo
    * key: Key of the song
    * mode: Mode of the song (major or minor)
    """

    def __init__(self, bpm: int, key: str, mode: str):
        self.bpm = bpm
        self.key = key
        self.mode = mode


class Stats:
    """A class representing the statistics of a song. The attributes are as follows:

    * danceability_%: Percentage indicating how suitable the song is for dancing
    * valence_%: Positivity of the song's musical content
    * energy_%: Perceived energy level of the song
    * acousticness_%: Amount of acoustic sound in the song
    * instrumentalness_%: Amount of instrumental content in the song
    * liveness_%: Presence of live performance elements
    * speechiness_%: Amount of spoken words in the song
    """

    def __init__(
        self,
        danceability: float,
        valence: float,
        energy: float,
        acousticness: float,
        instrumentalness: float,
        liveness: float,
        speechiness: float,
    ):
        self.danceability = danceability
        self.valence = valence
        self.energy = energy
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.speechiness = speechiness


class Song:
    """
    A class representing a song. The attributes are as follows:

    * track_name: Name of the song
    * Artists: A list of Artist objects
    * artist_count: Number of artists contributing to the song
    * Metadata: A class representing the metadata of the song
    * Extra: A class representing the extra information of the song
    * Stats: A class representing the statistics of the song
    """

    def __init__(
        self, track_name: str, artists: list[Artist], artist_count: int, metadata: Metadata, extra: Extra, stats: Stats
    ):
        self.track_name = track_name
        self.artists = artists
        assert len(artists) == artist_count, "artist_count must match the number of artists"
        self.artist_count = artist_count
        self.metadata = metadata
        self.extra = extra
        self.stats = stats


def get_csv_data(path, mode="r", encoding="utf-8") -> list[str]:
    with open(path, mode, encoding=encoding) as f:
        return f.readlines()


def process_csv_data(data: list[str]) -> list[Song]:
    """Process the raw CSV data into a list of Song objects."""
    for line in data[:2]:
        ll = line.strip().split(",")
        print(len(ll))
        """
        1. track_name: Name of the song
        2. artist(s)_name: Name of the artist(s) of the song
        3. artist_count: Number of artists contributing to the song
        4. released_year: Year when the song was released
        5. released_month: Month when the song was released
        6. released_day: Day of the month when the song was released
        7. in_spotify_playlists: Number of Spotify playlists the song is included in
        8. in_spotify_charts: Presence and rank of the song on Spotify charts
        9. streams: Total number of streams on Spotify
        10. in_apple_playlists: Number of Apple Music playlists the song is included in
        11. in_apple_charts: Presence and rank of the song on Apple Music charts
        12. in_deezer_playlists: Number of Deezer playlists the song is included in
        13. in_deezer_charts: Presence and rank of the song on Deezer charts
        14. in_shazam_charts: Presence and rank of the song on Shazam charts
        15. bpm: Beats per minute, a measure of song tempo
        16. key: Key of the song
        17. mode: Mode of the song (major or minor)
        18. danceability_%: Percentage indicating how suitable the song is for dancing
        19. valence_%: Positivity of the song's musical content
        20. energy_%: Perceived energy level of the song
        21. acousticness_%: Amount of acoustic sound in the song
        22. instrumentalness_%: Amount of instrumental content in the song
        23. liveness_%: Presence of live performance elements
        24. speechiness_%: Amount of spoken words in the song
        """
        stats = Stats(
            danceability=float(ll[17]),
            valence=float(ll[18]),
            energy=float(ll[19]),
            acousticness=float(ll[20]),
            instrumentalness=float(ll[21]),
            liveness=float(ll[22]),
            speechiness=float(ll[23]),
        )
        extra = Extra(bpm=int(ll[14]), key=ll[15], mode=ll[16])
        metadata = Metadata(
            released_year=int(ll[3]),
            released_month=int(ll[4]),
            released_day=int(ll[5]),
            streams=int(ll[8]),
            in_spotify_playlists=int(ll[6]),
            in_spotify_charts=int(ll[7]),
            in_apple_playlists=int(ll[9]),
            in_apple_charts=int(ll[10]),
            in_deezer_playlists=int(ll[11]),
            in_deezer_charts=int(ll[12]),
            in_shazam_charts=int(ll[13]),
        )
        artists = [Artist(artist_name=name) for name in ll[1].split(",")]
        song = Song(
            track_name=ll[0],
            artists=artists,
            artist_count=len(artists),
            metadata=metadata,
            extra=extra,
            stats=stats,
        )
        print(song)


if __name__ == "__main__":
    data = get_csv_data(DATA_DIR)[1:]  # Remove the header
    songs = process_csv_data(data)
