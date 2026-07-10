import sqlite3

conn = sqlite3.connect("data/fluxways_crm.db")
cursor = conn.cursor()

client_id = input("Enter Client ID to edit: ")

new_service = input("New Service: ")
new_status = input("New Status: ")

cursor.execute("""
UPDATE clients
SET service = ?, status = ?
WHERE id = ?
""", (new_service, new_status, client_id))

conn.commit()

if cursor.rowcount > 0:
    print("Client updated successfully!")
else:
    print("Client ID not found.")

conn.close()
