import csv

print("=== FLUXWAYS LEAD SCORER V2 ===")

name = input("Lead Name: ")
budget = int(input("Client Budget (N): "))
urgency = input("Urgency (high/medium/low): ").lower()

score = 0

if budget >= 500000:
    score += 50
elif budget >= 200000:
    score += 30
else:
    score += 10

if urgency == "high":
    score += 50
elif urgency == "medium":
    score += 30
else:
    score += 10

if score >= 80:
    status = "HOT"
elif score >= 50:
    status = "WARM"
else:
    status = "COLD"

print(f"\nLead Score: {score}/100")
print(f"Status: {status}")

with open("leads.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, budget, urgency, score, status])

print("Lead saved to leads.csv")
