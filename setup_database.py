import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/fluxways_crm.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    service TEXT NOT NULL,
    package TEXT NOT NULL,
    price INTEGER NOT NULL,
    proposal_id TEXT,
    status TEXT,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("Fluxways CRM database created successfully.")
