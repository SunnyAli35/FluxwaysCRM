import sqlite3

conn = sqlite3.connect("data/fluxways_crm.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, name, company, service, package, price, status
FROM clients
ORDER BY id
""")

rows = cursor.fetchall()

print("=" * 70)
print("              FLUXWAYS CLIENT LIST")
print("=" * 70)

if not rows:
    print("No clients found.")
else:
    for row in rows:
        print(f"ID       : {row[0]}")
        print(f"Client   : {row[1]}")
        print(f"Company  : {row[2]}")
        print(f"Service  : {row[3]}")
        print(f"Package  : {row[4]}")
        print(f"Price    : ${row[5]}")
        print(f"Status   : {row[6]}")
        print("-" * 70)

conn.close()
