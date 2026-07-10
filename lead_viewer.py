import csv

print("=== FLUXWAYS LEAD VIEWER ===\n")

with open("leads.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(f"Name: {row[0]}")
        print(f"Budget: N{row[1]}")
        print(f"Urgency: {row[2]}")
        print(f"Score: {row[3]}")
        print(f"Status: {row[4]}")
        print("-" * 30)
