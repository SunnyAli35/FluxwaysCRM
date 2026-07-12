from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Fluxways CRM API")

class Client(BaseModel):
    name: str
    company: str
    service: str
    package: str
    price: float
    status: str

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

@app.post("/clients")
def create_client(client: Client):
    conn = sqlite3.connect("data/fluxways_crm.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clients (name, company, service, package, price, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (client.name, client.company, client.service, client.package, client.price, client.status))

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {"id": new_id, **client.dict()}

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    conn = sqlite3.connect("data/fluxways_crm.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM clients WHERE id = ?", (client_id,))
    existing = cursor.fetchone()

    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Client not found")

    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    conn.close()

    return {"message": f"Client {client_id} deleted successfully"}