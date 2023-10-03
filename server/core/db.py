import sqlite3
from .config import DB_PATH, DB_SCHEMA_PATH


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    with open(DB_SCHEMA_PATH) as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def execute_sql(sql, params=None, commit=True, fetchone=False, fetchall=False):
    conn = get_db()
    cur = conn.cursor()
    if params is None:
        params = []
    cur.execute(sql, params)
    data = None
    if commit:
        conn.commit()
    if fetchone:
        data = cur.fetchone()
    if fetchall:
        data = cur.fetchall()
    conn.close()
    return data
