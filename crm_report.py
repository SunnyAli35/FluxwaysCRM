import csv

print("=== FLUXWAYS CRM REPORT ===")

hot = 0
warm = 0
cold = 0
total = 0

with open("leads.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        total += 1

        status = row[4].strip()

        if status == "HOT":
            hot += 1
        elif status == "WARM":
            warm += 1
        elif status == "COLD":
            cold += 1

print(f"Total Leads: {total}")
print(f"HOT Leads: {hot}")
print(f"WARM Leads: {warm}")
print(f"COLD Leads: {cold}")
