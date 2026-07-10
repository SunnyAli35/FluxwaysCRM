import csv

print("=== FLUXWAYS LEAD SCORER V3 ===")

name = input("Lead Name: ")
budget = int(input("Client Budget (N): "))

while True:
    urgency = input("Urgency (high/medium/low): ").lower()

    if urgency in ["high", "medium", "low"]:
        break

    print("Invalid input. Please enter high, medium, or low.")

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

if status == "HOT":
    proposal = f"""
==============================
FLUXWAYS SOLUTIONS PROPOSAL
==============================

Client: {name}

Lead Score: {score}
Status: {status}

Recommended Package:
AI Automation Package

Estimated Investment:
N250,000

Timeline:
2 Weeks

Thank you for choosing Fluxways Solutions.
"""

    filename = name.replace(" ", "_") + "_Proposal.txt"

    with open(filename, "w") as file:
        file.write(proposal)

    print(f"Proposal generated: {filename}")

print("Lead saved to leads.csv")
