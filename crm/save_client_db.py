from crm.database import get_connection

def save_client(name, company, service, package, price, proposal_id, status, created_at):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO clients
    (name, company, service, package, price, proposal_id, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        company,
        service,
        package,
        price,
        proposal_id,
        status,
        created_at
    ))

    conn.commit()
    conn.close()

    print("Client saved to SQLite successfully!")
