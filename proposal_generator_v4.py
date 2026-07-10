import config

print(f"=== {config.COMPANY_NAME} ===")

name = input("Client Name: ")
company = input("Company Name: ")
service = input("Service Needed: ")

package = "Professional"

print("\n==============================")
print("FLUXWAYS SOLUTIONS PROPOSAL")
print("==============================")
print(f"Client: {name}")
print(f"Company: {company}")
print(f"Service: {service}")
print(f"Recommended Package: {package}")
print(f"Price: ${config.PACKAGES[package]['price']}")
print(f"Timeline: {config.PACKAGES[package]['timeline']}")
print("\nThank you for choosing Fluxways Solutions!")
