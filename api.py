from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Fluxways CRM API")

@app.get("/")
def home():
    return {
        "message": "Welcome to Fluxways CRM API",
        "status": "Running"
    }

@app.get("/clients")
def get_clients():
    conn = sqlite3.connect("data/fluxways_crm.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name, company, service, package, price, status
    FROM clients
    """)

    rows = cursor.fetchall()
    conn.close()

    clients = []

    for row in rows:
        clients.append({
            "id": row[0],
            "name": row[1],
            "company": row[2],
            "service": row[3],
            "package": row[4],
            "price": row[5],
            "status": row[6]
        })

    return clients
