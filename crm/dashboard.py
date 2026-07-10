import csv
import os

DATABASE = "data/clients.csv"

print("=" * 40)
print("      FLUXWAYS CRM DASHBOARD")
print("=" * 40)

if not os.path.exists(DATABASE):
    print("No client database found.")
    exit()

total_clients = 0
total_revenue = 0
latest_client = None

with open(DATABASE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_clients += 1
        total_revenue += int(row["Price"])
        latest_client = row["Client"]

print(f"Total Clients   : {total_clients}")
print(f"Total Revenue   : ${total_revenue}")

if latest_client:
    print(f"Latest Client   : {latest_client}")

print("=" * 40)
