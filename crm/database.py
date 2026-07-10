import sqlite3

DATABASE = "data/fluxways_crm.db"

def get_connection():
    return sqlite3.connect(DATABASE)
