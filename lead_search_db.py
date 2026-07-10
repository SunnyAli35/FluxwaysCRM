import sqlite3

DATABASE = "data/fluxways_crm.db"

name = input("Enter client name to search: ").strip()

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
SELECT name, company, service, package, price, proposal_id, status, created_at
FROM clients
WHERE name LIKE ?
""", (f"%{name}%",))

rows = cursor.fetchall()

if rows:
    print("\n===== CLIENT FOUND =====")
    for row in rows:
        print(f"Client      : {row[0]}")
        print(f"Company     : {row[1]}")
        print(f"Service     : {row[2]}")
        print(f"Package     : {row[3]}")
        print(f"Price       : ${row[4]}")
        print(f"Proposal ID : {row[5]}")
        print(f"Status      : {row[6]}")
        print(f"Date        : {row[7]}")
        print("-" * 40)
else:
    print("Client not found.")

conn.close()
