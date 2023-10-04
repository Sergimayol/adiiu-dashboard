import sqlite3
from typing import Optional, Union, Any, List
from .config import DB_PATH


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def execute_sql(sql, params=None, commit=True, fetchone=False, fetchall=False) -> Optional[Union[Any, List[Any]]]:
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
