import os
import config
from crm.save_client import save_client

print("=== Fluxways Solutions ===")

name = input("Client Name: ")
company = input("Company Name: ")
service = input("Service Needed: ")

package = "Professional"
price = config.PACKAGES[package]["price"]
timeline = config.PACKAGES[package]["timeline"]

proposal = f"""
=================================
FLUXWAYS SOLUTIONS PROPOSAL
=================================

Client: {name}
Company: {company}
Service: {service}

Recommended Package: {package}
Price: ${price}
Timeline: {timeline}

Thank you for choosing Fluxways Solutions!
"""

print(proposal)

# Create proposals folder if it doesn't exist
os.makedirs("proposals", exist_ok=True)

filename = f"proposals/{name.replace(' ', '_')}_Proposal.txt"

with open(filename, "w") as file:
    file.write(proposal)

print(f"Proposal saved successfully as: {filename}")

# Save client to CRM
save_client(
    name,
    company,
    service,
    package,
    price
)

print("Client saved to CRM successfully!")
