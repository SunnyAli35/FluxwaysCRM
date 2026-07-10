import os

while True:
    print("\n" + "=" * 40)
    print("      FLUXWAYS CRM")
    print("=" * 40)
    print("1. Generate Proposal")
    print("2. Search Client")
    print("3. View Dashboard")
    print("4. Exit")
    print("=" * 40)

    choice = input("Select an option: ")

    if choice == "1":
        os.system("python proposal_generator_v6.py")

    elif choice == "2":
        os.system("python lead_search.py")

    elif choice == "3":
        os.system("python crm/dashboard.py")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
