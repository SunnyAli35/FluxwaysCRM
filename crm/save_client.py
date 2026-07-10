import csv
import os

DATABASE = "data/clients.csv"

def save_client(name, company, service, package, price):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(DATABASE)

    with open(DATABASE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Client",
                "Company",
                "Service",
                "Package",
                "Price"
            ])

        writer.writerow([
            name,
            company,
            service,
            package,
            price
        ])

    print("Client saved to CRM.")
