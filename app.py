print("=" * 40)
print("        FLUXWAYS CRM v3")
print("=" * 40)
print("1. Generate Proposal")
print("2. Search Client")
print("3. View Dashboard")
print("4. View All Clients")
print("5. Edit Client")
print("6. Delete Client")
print("7. Exit")
print("=" * 40)

choice = input("Select an option: ")

import os

if choice == "1":
    os.system("python proposal_generator_v6.py")

elif choice == "2":
    os.system("python lead_search_db.py")

elif choice == "3":
    os.system("python dashboard_db.py")

elif choice == "4":
    os.system("python clients_list.py")

elif choice == "5":
    os.system("python edit_client.py")

elif choice == "6":
    os.system("python delete_client.py")

elif choice == "7":
    print("Goodbye!")

else:
    print("Invalid option.")
