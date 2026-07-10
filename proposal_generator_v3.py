print("=== FLUXWAYS SOLUTIONS ===")

name = input("Client Name: ")
company = input("Company Name: ")
service = input("Service Needed: ")

service_lower = service.lower()

if "ai" in service_lower:
    price = "N250,000"
elif "crm" in service_lower:
    price = "N200,000"
elif "lead" in service_lower:
    price = "N150,000"
else:
    price = "N100,000"

proposal = f"""
==============================
FLUXWAYS SOLUTIONS PROPOSAL
==============================

Client: {name}
Company: {company}

Requested Service:
{service}

Recommended Price:
{price}

Timeline:
2 Weeks

Thank you for choosing Fluxways Solutions.
"""

filename = name.replace(" ", "_") + "_Proposal.txt"

with open(filename, "w") as file:
    file.write(proposal)

print(proposal)
print(f"Proposal saved as: {filename}")
