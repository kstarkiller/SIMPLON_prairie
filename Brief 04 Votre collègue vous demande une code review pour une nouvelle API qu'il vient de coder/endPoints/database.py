import sqlite3
from fastapi import HTTPException

def get_db_connection(db):
    try:
        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row
        return con
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))