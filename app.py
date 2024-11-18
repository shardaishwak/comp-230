from yaspin import yaspin
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from tabulate import tabulate
import os
import sqlite3
from queries import *
from contextlib import closing
from helpers import *
from createObjects import *
import datetime


def get_input_values(entity_name, fields):
    """
    Prompt the user to create a new entry by providing values for all fields.
    """
    print(f"\n--- Create New {entity_name.capitalize()} ---")
    values = {}
    for field in fields:
        value = input(f"Enter {field}: ").strip()
        values[field] = value

    return values.values()






# Utility for displaying tables
def display_table(headers, data):
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))



def create_address(cursor: sqlite3.Cursor):
    address_fields = ["Street", "City", "Postcode", "Country"]
    address_values = get_input_values("address", address_fields)
    with yaspin(text=f"Creating new address...", color="cyan") as spinner:
        address_id = createAddress(cursor, *address_values)
        spinner.ok("✔")
    return address_id

def create_user(cursor: sqlite3.Cursor, address_id):
    user_fields = ["Name", "Gender", "Date of Birth", "Phone Number"]
    user_values = get_input_values("user", user_fields)

    with yaspin(text=f"Creating new user...", color="cyan") as spinner:
        user_id = createUser(cursor, *user_values, address_id)
        spinner.ok("✔")
    
    return user_id


def prompt_get_or_create_user(cursor: sqlite3.Cursor, entity_name):
    user_id = None
    while True:
        user_choice = input(f"Do you want to create a new user for this {entity_name}? (y/n): ").strip().lower()
        if user_choice == "n":
            user_id = input(f"Enter the user ID: ").strip()
            if not user_id:
                print("User ID is required.")
                continue
            user = getUserDetails(cursor, user_id)
            if not user:
                print(f"No user found with ID {user_id}.")
                continue
            break
        else: 
            address_id = create_address(cursor)
            user_id = create_user(cursor, address_id)
            break
    return user_id

# def conditional_create(cursor: sqlite3.Cursor, entity_name, create_function, create_args, check_function):
#     """
#     Check if an entity already exists in the database before creating a new entry.
#     """
#     entity_id = None
#     while True:
#         entitiy_choice = input(f"Do you want to create a new {entity_name}? (y/n): ").strip().lower()
#         if entitiy_choice == "n":
#             entity_id = input(f"Enter the {entity_name} ID: ").strip()
#             if not entity_id:
#                 print(f"{entity_name} ID is required.")
#                 continue
#             user = check_function(cursor, entity_id)
#             if not user:
#                 print(f"No {entity_name} found with ID {entity_id}.")
#                 continue
#             break
#         else: 
#             entity_id = create_function(cursor, *create_args)
#             break


# Dashboard
def dashboard(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Dashboard...", color="cyan") as spinner:
        # Placeholder: Add SQL queries here
        summary_cards = {
            "Total Offices": getTotalOffices(cursor),
            "Total Staff": getTotalStaff(cursor),
            "Total Owners": getTotalOwners(cursor),
            "Total Drivers": getTotalDrivers(cursor),
            "Total Taxis": getTotalTaxis(cursor),
            "Total Contracts": getTotalContracts(cursor),
            "Total Clients": getTotalClients(cursor),
            "Active Jobs": getTotalActiveJobs(cursor),
        }
        recent_activity = getRecentActivity(cursor)
        spinner.ok("✔")
    print("\n--- Dashboard Summary ---")
    for key, value in summary_cards.items():
        print(f"{key}: {value}")
    print("\n--- Recent Jobs ---")
    display_table(data=recent_activity, headers=[desc[0] for desc in cursor.description])







# Office Management
def office_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Offices...", color="cyan") as spinner:
        # Placeholder: SQL query to fetch office list
        offices = getOffices(cursor)
        spinner.ok("✔")
    display_table(data=offices, headers=[desc[0] for desc in cursor.description])

def office_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the office ID: ").strip()
    with yaspin(text=f"Fetching details for Office {entity_id}...", color="cyan") as spinner:
        # Placeholder: SQL query to fetch office details
        office_info = getOfficeDetails(cursor, entity_id)
        print(office_info   )
        if not office_info:
            spinner.fail(f"No details found for office with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Office Details ---")
    display_table(data=[office_info], headers=[desc[0] for desc in cursor.description])
    
def office_create(cursor: sqlite3.Cursor):
    address_id = create_address(cursor)
    
    office_fields = ["Phone Number"]
    office_values = get_input_values("office", office_fields)
    with yaspin(text=f"Creating new office...", color="cyan") as spinner:
        # Placeholder: Replace with logic to create new entry in DB
        office_id = createOffice(cursor, address_id, *office_values)
        spinner.ok("✔")
    print(f"New office created with ID: {office_id}")


# Staff Management
def staff_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Staff...", color="cyan") as spinner:
        # Placeholder: SQL query to fetch staff list
        staff = getStaffs(cursor)
        spinner.ok("✔")
    display_table(data=staff, headers=[desc[0] for desc in cursor.description])

def staff_details(cursor):
    entity_id = input(f"Enter the staff ID: ").strip()
    with yaspin(text=f"Fetching details for Staff {entity_id}...", color="cyan") as spinner:
        # Placeholder: SQL query to fetch staff details
        staff_info = getStaffDetails(cursor, entity_id)
        if not staff_info:
            spinner.fail(f"No details found for staff with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Staff Details ---")
    display_table(data=[staff_info], headers=[desc[0] for desc in cursor.description])

def staff_create(cursor: sqlite3.Cursor):
    user_id = prompt_get_or_create_user(cursor, "staff")

    staff_fields = ["Office ID", "Role", "NIN"]
    staff_values = get_input_values("staff", staff_fields)

    with yaspin(text=f"Creating new staff...", color="cyan") as spinner:
        staff_id = createStaff(cursor, user_id, *staff_values)
        spinner.ok("✔")

    print(f"New staff created with ID: {staff_id}")


# Drivers
def driver_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Drivers...", color="cyan") as spinner:
        drivers = getDrivers(cursor)
        spinner.ok("✔")
    display_table(data=drivers, headers=[desc[0] for desc in cursor.description])

def driver_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the driver ID: ").strip()
    with yaspin(text=f"Fetching details for Driver {entity_id}...", color="cyan") as spinner:
        driver_info = getDriverDetails(cursor, entity_id)
        if not driver_info:
            spinner.fail(f"No details found for driver with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Driver Details ---")
    display_table(data=[driver_info], headers=[desc[0] for desc in cursor.description])

def driver_create(cursor: sqlite3.Cursor):
    user_id = prompt_get_or_create_user(cursor, "driver")

    driver_fields = ["Owner ID (default none)", "Taxi ID", "NIN", "Licence No"]
    driver_values = get_input_values("driver", driver_fields)

    with yaspin(text=f"Creating new driver...", color="cyan") as spinner:
        # today in YYYY-MM-DD format
        today = datetime.date.today().strftime("%Y-%m-%d")
        driver_id = createDriver(cursor, user_id, str(today), *driver_values)
        spinner.ok("✔")

    print(f"New driver created with ID: {driver_id}")

# Owner
def owner_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Owners...", color="cyan") as spinner:
        owners = getOwners(cursor)
        spinner.ok("✔")
    display_table(data=owners, headers=[desc[0] for desc in cursor.description])

def owner_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the owner ID: ").strip()
    with yaspin(text=f"Fetching details for Owner {entity_id}...", color="cyan") as spinner:
        owner_info = getOwnerDetails(cursor, entity_id)
        if not owner_info:
            spinner.fail(f"No details found for owner with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Owner Details ---")
    display_table(data=[owner_info], headers=[desc[0] for desc in cursor.description])

def owner_create(cursor: sqlite3.Cursor):
    user_id = prompt_get_or_create_user(cursor, "owner")

    owner_fields = ["Office ID", "NIN"]
    owner_values = get_input_values("owner", owner_fields)

    with yaspin(text=f"Creating new owner...", color="cyan") as spinner:
        owner_values = list(owner_values)
        owner_id = createOwner(cursor, office_id=owner_values[0], user_id=user_id, NIN=owner_values[1])
        spinner.ok("✔")

    print(f"New owner created with ID: {owner_id}")

# Taxi
def taxi_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Taxis...", color="cyan") as spinner:
        taxis = getTaxis(cursor)
        spinner.ok("✔")
    display_table(data=taxis, headers=[desc[0] for desc in cursor.description])

def taxi_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the taxi ID: ").strip()
    with yaspin(text=f"Fetching details for Taxi {entity_id}...", color="cyan") as spinner:
        taxi_info = getTaxiDetails(cursor, entity_id)
        if not taxi_info:
            spinner.fail(f"No details found for taxi with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Taxi Details ---")
    display_table(data=[taxi_info], headers=[desc[0] for desc in cursor.description])

def taxi_create(cursor: sqlite3.Cursor):
    owner_id = input(f"Enter the owner ID: ").strip()
    registration_number = input(f"Enter the registration number: ").strip()
    capacity = input(f"Enter the capacity: ").strip()

    with yaspin(text=f"Creating new taxi...", color="cyan") as spinner:
        taxi_id = createTaxi(cursor, owner_id, registration_number, capacity)
        spinner.ok("✔")

    print(f"New taxi created with ID: {taxi_id}")


# Business client
def business_client_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Business Clients...", color="cyan") as spinner:
        business_clients = getBusinessClients(cursor)
        spinner.ok("✔")
    display_table(data=business_clients, headers=[desc[0] for desc in cursor.description])

def business_client_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the business client ID: ").strip()
    with yaspin(text=f"Fetching details for Business Client {entity_id}...", color="cyan") as spinner:
        business_client_info = getBusinessClientDetails(cursor, entity_id)
        if not business_client_info:
            spinner.fail(f"No details found for business client with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Business Client Details ---")
    display_table(data=[business_client_info], headers=[desc[0] for desc in cursor.description])

def business_client_create(cursor: sqlite3.Cursor):
    address_id = create_address(cursor)
    hst_number = input(f"Enter the HST number: ").strip()

    with yaspin(text=f"Creating new business client...", color="cyan") as spinner:
        business_client_id = createBusinessClient(cursor, hst_number, address_id)
        # create client
        client_id = createClient(cursor, business_client_id=business_client_id)
        spinner.ok("✔")

    print(f"New business client created with ID: {business_client_id}")

# Private client
def private_client_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Private Clients...", color="cyan") as spinner:
        private_clients = getPrivateClients(cursor)
        spinner.ok("✔")
    display_table(data=private_clients, headers=[desc[0] for desc in cursor.description])

def private_client_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the private client ID: ").strip()
    with yaspin(text=f"Fetching details for Private Client {entity_id}...", color="cyan") as spinner:
        private_client_info = getPrivateClientDetails(cursor, entity_id)
        if not private_client_info:
            spinner.fail(f"No details found for private client with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Private Client Details ---")
    display_table(data=[private_client_info], headers=[desc[0] for desc in cursor.description])

def private_client_create(cursor: sqlite3.Cursor):
    user_id = prompt_get_or_create_user(cursor, "private client")

    with yaspin(text=f"Creating new private client...", color="cyan") as spinner:
        today = datetime.date.today().strftime("%Y-%m-%d")
        private_client_id = createPrivateClient(cursor, user_id, today)
        # create client
        client_id = createClient(cursor, private_client_id=private_client_id)
        spinner.ok("✔")

    print(f"New private client created with ID: {private_client_id}")

# Contracts
def contract_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Contracts...", color="cyan") as spinner:
        contracts = getContracts(cursor)
        spinner.ok("✔")
    display_table(data=contracts, headers=[desc[0] for desc in cursor.description])

def contract_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the contract ID: ").strip()
    with yaspin(text=f"Fetching details for Contract {entity_id}...", color="cyan") as spinner:
        contract_info = getContractDetails(cursor, entity_id)
        if not contract_info:
            spinner.fail(f"No details found for contract with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Contract Details ---")
    display_table(data=[contract_info], headers=[desc[0] for desc in cursor.description])

def contract_create(cursor: sqlite3.Cursor):
    office_id = input(f"Enter the office ID: ").strip()
    business_client_id = input(f"Enter the business client ID: ").strip()
    signed_on = input(f"Enter the signed on date (YYYY-MM-DD): ").strip()
    no_jobs = input(f"Enter the number of jobs: ").strip()
    flat_fees = input(f"Enter the flat fees: ").strip()

    with yaspin(text=f"Creating new contract...", color="cyan") as spinner:
        contract_id = createContract(cursor, office_id, business_client_id, signed_on, no_jobs, flat_fees)
        spinner.ok("✔")

    print(f"New contract created with ID: {contract_id}")

# job
def job_list(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Jobs...", color="cyan") as spinner:
        jobs = getJobs(cursor)
        spinner.ok("✔")
    display_table(data=jobs, headers=[desc[0] for desc in cursor.description])

def job_details(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the job ID: ").strip()
    with yaspin(text=f"Fetching details for Job {entity_id}...", color="cyan") as spinner:
        job_info = getJobDetails(cursor, entity_id)
        if not job_info:
            spinner.fail(f"No details found for job with ID {entity_id}.")
            return
        spinner.ok("✔")
    print("\n--- Job Details ---")
    display_table(data=[job_info], headers=[desc[0] for desc in cursor.description])

def job_create(cursor: sqlite3.Cursor):
    driver_id = input(f"Enter the driver ID: ").strip()
    client_id = input(f"Enter the client ID: ").strip()
    mileage = input(f"Enter the mileage: ").strip()
    charge = input(f"Enter the charge: ").strip()
    start_time = input(f"Enter the start time (YYYY-MM-DD HH:MM:SS): ").strip()
    end_time = input(f"Enter the end time (YYYY-MM-DD HH:MM:SS): ").strip()
    
    address_id = create_address(cursor)

    with yaspin(text=f"Creating new job...", color="cyan") as spinner:
        job_id = createJob(cursor, driver_id, client_id, mileage, charge, start_time, end_time, address_id, status="PENDING", failure_reason=None, contract_id=None)
        spinner.ok("✔")

    print(f"New job created with ID: {job_id}")

# Main Application Loop
def display_menu():
    """
    Display the list of available commands to the user.
    """
    print("\n--- Available Commands ---")
    print("dashboard - View dashboard overview")

    print("offices - Manage and view office details")
    print("offices get - Get office details")
    print("offices create - Create a new office")

    print("staff - Manage and view staff details")
    print("staff get - Get staff details")
    print("staff create - Create a new staff")

    print("drivers - View list of drivers")
    print("drivers details - Get driver details")
    print("drivers create - Create a new driver")

    print("taxis - View list of taxis")
    print("taxis get - Get taxi details")
    print("taxis create - Create a new taxi")

    print("owners - View list of owners")
    print("owners get - Get owner details")
    print("owners create - Create a new owner")

    print("business clients - View list of clients")
    print("business clients get - Get client details")
    print("business clients create - Create a new client")

    print("private clients - View list of private clients")
    print("private clients get - Get private client details")
    print("private clients create - Create a new private client")

    print("contracts - View list of contracts")
    print("contracts get - Get contract details")
    print("contracts create - Create a new contract")

    print("job - View list of jobs")
    print("job get - Get job details")
    print("job create - Create a new job")


    print("clear - Clear the screen")
    print("cmd - Display this menu")

    print("4. quit - Exit the application")
    print("---------------------------")

def main(cursor: sqlite3.Cursor):
    options = WordCompleter(
        [
            "dashboard",
            "offices",
            "offices get",
            "offices create",
            "staff",
            "staff get",
            "staff create",
            "drivers",
            "drivers get",
            "drivers create",
            "owners",
            "owners get",
            "owners create"
            "taxis",
            "taxis get",
            "taxis create",
            "business clients",
            "business clients get",
            "business clients create",
            "private clients",
            "private clients get",
            "private clients create",
            "contracts",
            "contracts get",
            "contracts create",
            "jobs",
            "jobs get",
            "jobs create",
            "cmd",
            "clear",
            "quit",
        ],
        ignore_case=True,
    )
    print("Welcome to the Management System!")
    display_menu()
    while True:
        user_input = prompt("\nEnter command: ", completer=options)
        if user_input == "dashboard":
            dashboard(cursor)
        elif user_input == "offices":
            office_list(cursor)
        elif user_input == ("offices get"):
            office_details(cursor)
        elif user_input == ("offices create"):
            office_create(cursor)
        elif user_input == "staff":
            staff_list(cursor)
        elif user_input == "staff get":
            staff_details(cursor)
        elif user_input == "staff create":
            staff_create(cursor)
        elif user_input == "drivers":
            driver_list(cursor)
        elif user_input == "drivers details":
            driver_details(cursor)
        elif user_input == "drivers get":
            driver_create(cursor)
        elif user_input == "taxis":
            taxi_list(cursor)
        elif user_input == "taxis get":
            taxi_details(cursor)
        elif user_input == "owners":
            owner_list(cursor)
        elif user_input == "owners get":
            owner_details(cursor)
        elif user_input == "owners create":
            owner_create(cursor)
        elif user_input == "taxis create":
            taxi_create(cursor)
        elif user_input == "business clients":
            business_client_list(cursor)
        elif user_input == "business clients get":
            business_client_details(cursor)
        elif user_input == "business clients create":
            business_client_create(cursor)
        elif user_input == "private clients":
            private_client_list(cursor)
        elif user_input == "private clients get":
            private_client_details(cursor)
        elif user_input == "private clients create":
            private_client_create(cursor)
        elif user_input == "contracts":
            contract_list(cursor)
        elif user_input == "contracts get":
            contract_details(cursor)
        elif user_input == "contracts create":
            contract_create(cursor)
        elif user_input == "jobs":
            job_list(cursor)
        elif user_input == "jobs get":
            job_details(cursor)
        elif user_input == "jobs create":
            job_create(cursor)
        elif user_input == "cmd":
            display_menu()
        elif user_input == "clear":
            os.system("clear")
        elif user_input == "quit":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid command. Please choose a valid option.")

if __name__ == "__main__":
    with closing(sqlite3.connect('database.db')) as connection:
        connection.row_factory = sqlite3.Row

        with closing(connection.cursor()) as cursor:
            main(cursor)
            connection.commit()

