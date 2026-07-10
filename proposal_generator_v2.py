print("=== FLUXWAYS SOLUTIONS ===")

name = input("Client Name: ")
company = input("Company Name: ")
service = input("Service Needed: ")

proposal = f"""
==============================
FLUXWAYS SOLUTIONS PROPOSAL
==============================

Client: {name}
Company: {company}

Requested Service:
{service}

Recommended Solution:
- Lead Capture System
- Airtable CRM
- Make Automation
- Claude AI Integration

Timeline:
2 Weeks

Thank you for choosing Fluxways Solutions.
"""

filename = name.replace(" ", "_") + "_Proposal.txt"

with open(filename, "w") as file:
    file.write(proposal)

print(proposal)
print(f"Proposal saved as: {filename}")
