import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
DATA_DIR = os.path.join(BASE_DIR, "data", "spotify-2023.csv")
DB_DIR = os.path.join(BASE_DIR, "data", "db.sqlite3")
VERBOSE = True

if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR, verbose=VERBOSE)
    # If the column "artist(s)_name" can contain multiple artists, then we need to split (by ',') it into multiple rows "duplicate" the other columns
    df = df.assign(**{col: df[col].str.split(",") for col in ["artist(s)_name"]}).explode("artist(s)_name")
    # Rename the column "artist(s)_name" to "artist_name"
    df = df.rename(columns={"artist(s)_name": "artist_name"})
    df["artist_name"] = df["artist_name"].str.strip()
    df["artist_name"] = df["artist_name"].replace(["Bad B", ""], ["Bad Bunny", "Unknown"])
    df.info(verbose=VERBOSE)
    conn = sqlite3.connect(DB_DIR)
    df.to_sql("songs", conn, if_exists="replace", index=True, index_label="id")
    conn.close()
