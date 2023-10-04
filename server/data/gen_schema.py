import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
DATA_DIR = os.path.join(BASE_DIR, "data", "spotify-2023.csv")

if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR, verbose=True)
    conn = sqlite3.connect("db.sqlite")
    df.to_sql("songs", conn, if_exists="replace", index=True, index_label="id")
    conn.close()
