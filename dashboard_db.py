import sqlite3

conn = sqlite3.connect("data/fluxways_crm.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM clients")
total_clients = cursor.fetchone()[0]

cursor.execute("SELECT SUM(price) FROM clients")
total_revenue = cursor.fetchone()[0] or 0

cursor.execute("SELECT name FROM clients ORDER BY id DESC LIMIT 1")
latest = cursor.fetchone()

latest_client = latest[0] if latest else "None"

print("=" * 40)
print("      FLUXWAYS CRM DASHBOARD")
print("=" * 40)
print(f"Total Clients : {total_clients}")
print(f"Total Revenue : ${total_revenue}")
print(f"Latest Client : {latest_client}")
print("=" * 40)

conn.close()
