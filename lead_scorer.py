print("=== FLUXWAYS LEAD SCORER ===")

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

print(f"\nLead Score: {score}/100")

if score >= 80:
    print("HOT LEAD 🔥")
elif score >= 50:
    print("WARM LEAD 🟡")
else:
    print("COLD LEAD ❄️")
