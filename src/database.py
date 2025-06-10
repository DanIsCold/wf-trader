import sqlite3
from pathlib import Path

DB_PATH = Path("data/warframe_market.db")

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   item_name TEXT,
                   seller TEXT,
                   price REAL,
                   order_type TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
    conn.commit()
    conn.close()