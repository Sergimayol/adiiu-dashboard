from .db import execute_sql


def get_songs():
    return execute_sql("SELECT * FROM songs", fetchall=True)


def get_songs_mode_vs_streams():
    return execute_sql(
        "SELECT mode, SUM(streams) AS streams FROM songs GROUP BY mode ORDER BY streams DESC",
        fetchall=True,
    )


def get_songs_releasedyear_vs_numsongs():
    return execute_sql(
        # GET released year as unix timestamp
        "SELECT released_year, COUNT(*) AS numsongs FROM songs GROUP BY released_year HAVING released_year >= 2000 ORDER BY released_year ASC",
        fetchall=True,
    )
def get_artists_with_most_streams():
    return execute_sql(
       "SELECT artist_name, SUM(streams) AS streams  FROM songs GROUP BY artist_name ORDER BY streams DESC LIMIT 0,10",
        fetchall=True,
    )

def get_songs_with_most_streams():
    return execute_sql(
        #Problema con LOVE GROWS 
       "SELECT track_name, SUM(streams) AS streams FROM songs GROUP BY track_name ORDER BY streams DESC  LIMIT 0,20",
        fetchall=True,
    )

def get_artists_occurences():
    return execute_sql(
        # The occurrences must be >=3
        "SELECT artist_name, COUNT(*) AS occurences FROM songs GROUP BY artist_name HAVING occurences >= 3 ORDER BY occurences DESC",
        fetchall=True,
    )
