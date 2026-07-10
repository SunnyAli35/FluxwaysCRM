import csv
import os

DATABASE = "data/clients.csv"

if not os.path.exists(DATABASE):
    print("No CRM database found.")
    exit()

name = input("Enter client name to search: ").strip().lower()

found = False

with open(DATABASE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if name in row["Client"].lower():
            print("\n===== CLIENT FOUND =====")
            print(f"Client : {row['Client']}")
            print(f"Company: {row['Company']}")
            print(f"Service: {row['Service']}")
            print(f"Package: {row['Package']}")
            print(f"Price  : ${row['Price']}")
            found = True

if not found:
    print("Client not found.")
