import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")
DB_SCHEMA_PATH = os.path.join(BASE_DIR, "data", "schema.sql")
