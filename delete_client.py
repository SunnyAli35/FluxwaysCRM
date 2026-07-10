import sqlite3

conn = sqlite3.connect("data/fluxways_crm.db")
cursor = conn.cursor()

client_id = input("Enter Client ID to delete: ")

cursor.execute(
    "DELETE FROM clients WHERE id = ?",
    (client_id,)
)

conn.commit()

if cursor.rowcount > 0:
    print("Client deleted successfully!")
else:
    print("Client ID not found.")

conn.close()
