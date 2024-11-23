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
from updateQueries import *
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

STAFF_FIELDS = ["role"]

DRIVER_FIELDS = ["NIN"]
USER_FIELDS = ["name", "gender", "date_of_birth", "phone_number"]
JOB_UPDATABLE_FIELDS = ["status", "failure_reason", "pickup_date", "dropoff_date", "charge", "mileage"]
ADDRESS_FIELDS = ["street", "city", "postcode", "country"]


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

# Owner Taxis
def owner_taxis(cursor: sqlite3.Cursor):
    owner_id = input(f"Enter the owner ID: ").strip()
    with yaspin(text=f"Fetching taxis for Owner {owner_id}...", color="cyan") as spinner:
        owner_taxis = getOwnerTaxis(cursor, owner_id)
        if not owner_taxis:
            spinner.fail(f"No taxis found for owner with ID {owner_id}.")
            return
        spinner.ok("✔")
    display_table(data=owner_taxis, headers=[desc[0] for desc in cursor.description])

# Jobs Today
def jobs_today(cursor: sqlite3.Cursor):
    with yaspin(text="Loading Jobs for Today...", color="cyan") as spinner:
        jobs_today = getTodayJobs(cursor)
        spinner.ok("✔")
    display_table(data=jobs_today, headers=[desc[0] for desc in cursor.description])

# Jobs Driver
def jobs_driver(cursor: sqlite3.Cursor):
    driver_id = input(f"Enter the driver ID: ").strip()
    with yaspin(text=f"Fetching jobs for Driver {driver_id}...", color="cyan") as spinner:
        driver_jobs = getDriverJobs(cursor, driver_id)
        if not driver_jobs:
            spinner.fail(f"No jobs found for driver with ID {driver_id}.")
            return
        spinner.ok("✔")
    display_table(data=driver_jobs, headers=[desc[0] for desc in cursor.description])

# Finalize job: id, mileage, charge
def job_finalize(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the job ID: ").strip()
    mileage = input(f"Enter the mileage: ").strip()
    charge = input(f"Enter the charge: ").strip()
    with yaspin(text=f"Finalizing Job {entity_id}...", color="cyan") as spinner:
        finalizeJob(cursor, entity_id, mileage, charge)
        spinner.ok("✔")
    print(f"Job {entity_id} finalized")


# finalize job failed
def job_failed(cursor: sqlite3.Cursor):
    entity_id = input(f"Enter the job ID: ").strip()
    reason = input(f"Enter the failure reason: ").strip()
    with yaspin(text=f"Marking Job {entity_id} as failed ...", color="cyan") as spinner:
        finalizeJobFailed(cursor, entity_id, reason)
        spinner.ok("✔")
    print(f"Job {entity_id} marked as failed")


# Jobs by status
def jobs_by_status(cursor: sqlite3.Cursor):
    status = input(f"Enter the status: ").strip()
    with yaspin(text=f"Fetching jobs with status {status}...", color="cyan") as spinner:
        jobs = getJobsByStatus(cursor, status)
        if not jobs:
            spinner.fail(f"No jobs found with status {status}.")
            return
        spinner.ok("✔")
    display_table(data=jobs, headers=[desc[0] for desc in cursor.description])

# Total income from office
def total_income_from_office(cursor: sqlite3.Cursor):
    office_id = input(f"Enter the office ID: ").strip()
    with yaspin(text=f"Fetching total income from Office {office_id}...", color="cyan") as spinner:
        total_income = getTotalIncomeByOffice(cursor, office_id)
        spinner.ok("✔")
    print(f"Total income from Office {office_id}: {total_income}")

# Total income from driver
def total_income_from_driver(cursor: sqlite3.Cursor):
    driver_id = input(f"Enter the driver ID: ").strip()
    with yaspin(text=f"Fetching total income from Driver {driver_id}...", color="cyan") as spinner:
        total_income = getTotalIncomeByDriver(cursor, driver_id)
        spinner.ok("✔")
    print(f"Total income from Driver {driver_id}: {total_income}")

# Total income by date: user inputs YYYY-MM-DD
def total_income_by_date_at_office(cursor: sqlite3.Cursor):
    date = input(f"Enter the date (YYYY-MM-DD): ").strip()
    office_id = input(f"Enter the office ID: ").strip()
    with yaspin(text=f"Fetching total income from Office {office_id} on {date}...", color="cyan") as spinner:
        total_income = getTotalIncomeByDateAtOffice(cursor, date, office_id)
        spinner.ok("✔")
    print(f"Total income from Office {office_id} on {date}: {total_income}")

# UPDATES

def update_job_prompt(cursor: sqlite3.Cursor):
    job_id = input("Enter the Job ID to update: ").strip()
    
    cursor.execute("SELECT * FROM job WHERE job_id = ?", (job_id,))
    job = cursor.fetchone()
    if not job:
        spinner.fail("✖ The job was not found.")
        return

    print("Fields you can update:")
    for field in JOB_UPDATABLE_FIELDS:
        print(f"- {field}")

    updates = {}
    while True:
        field = input("Enter the field to update (or 'done' to finish): ").strip()
        if field.lower() == "done":
            break
        if field not in JOB_UPDATABLE_FIELDS:
            spinner.fail(f"Invalid field. Choose from: {', '.join(JOB_UPDATABLE_FIELDS)}")
            continue
        value = input(f"✖ Enter the new value for {field}: ").strip()
        updates[field] = value

    if not updates:
        print("No updates provided.")
        return

    with yaspin(text="Updating job...", color="cyan") as spinner:
        success = updateJob(cursor, job_id, updates)
        if success:
            spinner.ok("✔")
            print("Job updated successfully.")
        else:
            spinner.fail("✖ Failed to update the job.")


def update_driver_prompt(cursor: sqlite3.Cursor):
    driver_id = input("Enter the Driver ID to update: ").strip()

    cursor.execute("SELECT * FROM driver WHERE driver_id = ?", (driver_id,))
    driver = cursor.fetchone()
    if not driver:
        print(f"No driver found with ID {driver_id}.")
        return

    cursor.execute("""
        SELECT user.user_id, address.address_id 
        FROM driver 
        JOIN user ON driver.user_id = user.user_id
        JOIN address ON user.address_id = address.address_id
        WHERE driver.driver_id = ?
    """, (driver_id,))
    user_info = cursor.fetchone()
    if not user_info:
        print("Error: Unable to find associated user or address.")
        return
    user_id, address_id = user_info

    print("Fields you can update:")
    all_updatable_fields = DRIVER_FIELDS + USER_FIELDS + ADDRESS_FIELDS
    for field in all_updatable_fields:
        print(f"- {field}")

    updates = {}
    while True:
        field = input("Enter the field to update (or 'done' to finish): ").strip()
        if field.lower() == "done":
            break
        if field not in all_updatable_fields:
            print(f"Invalid field. Choose from: {', '.join(all_updatable_fields)}")
            continue
        value = input(f"Enter the new value for {field}: ").strip()
        updates[field] = value

    if not updates:
        print("No updates provided.")
        return

    driver_updates = {k: v for k, v in updates.items() if k in DRIVER_FIELDS}
    user_updates = {k: v for k, v in updates.items() if k in USER_FIELDS}
    address_updates = {k: v for k, v in updates.items() if k in ADDRESS_FIELDS}

    if driver_updates:
        new_nin = driver_updates.get("NIN")
        with yaspin(text="Updating NIN...", color="cyan") as spinner:
            success = updateDriverNin(cursor, driver_id, new_nin)
            if success:
                spinner.ok("✔")
                print("Driver NIN updated successfully.")
            else:
                spinner.fail("✖ Failed to update driver NIN.")

    if user_updates:
        with yaspin(text="Updating user fields...", color="cyan") as spinner:
            success = updateUser(cursor, user_id, user_updates)
            if success:
                spinner.ok("✔")
                print("User fields updated successfully.")
            else:
                spinner.fail("✖ Failed to update user fields.")

    if address_updates:
        with yaspin(text="Updating address fields...", color="cyan") as spinner:
            success = updateAddress(cursor, address_id, address_updates)
            if success:
                spinner.ok("✔")
                print("Address fields updated successfully.")
            else:
                spinner.fail("✖ Failed to update address fields.")


def update_staff_prompt(cursor: sqlite3.Cursor):
    staff_id = input("Enter the Staff ID to update: ").strip()

    cursor.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,))
    staff = cursor.fetchone()
    if not staff:
        print(f"No staff found with ID {staff_id}.")
        return

    cursor.execute("""
        SELECT user.user_id, address.address_id 
        FROM staff 
        JOIN user ON staff.user_id = user.user_id
        JOIN address ON user.address_id = address.address_id
        WHERE staff.staff_id = ?
    """, (staff_id,))
    user_info = cursor.fetchone()
    if not user_info:
        print("Error: Unable to find associated user or address.")
        return
    user_id, address_id = user_info

    print("Fields you can update:")
    all_updatable_fields = STAFF_FIELDS + USER_FIELDS + ADDRESS_FIELDS
    for field in all_updatable_fields:
        print(f"- {field}")

    updates = {}
    while True:
        field = input("Enter the field to update (or 'done' to finish): ").strip()
        if field.lower() == "done":
            break
        if field not in all_updatable_fields:
            print(f"Invalid field. Choose from: {', '.join(all_updatable_fields)}")
            continue
        value = input(f"Enter the new value for {field}: ").strip()
        updates[field] = value

    if not updates:
        print("No updates provided.")
        return

    staff_updates = {k: v for k, v in updates.items() if k in STAFF_FIELDS}
    user_updates = {k: v for k, v in updates.items() if k in USER_FIELDS}
    address_updates = {k: v for k, v in updates.items() if k in ADDRESS_FIELDS}

    if staff_updates:
        new_role = staff_updates.get("role")
        with yaspin(text="Updating staff role...", color="cyan") as spinner:
            success = updateStaff(cursor, staff_id, new_role)
            if success:
                spinner.ok("✔")
                print("Staff role updated successfully.")
            else:
                spinner.fail("✖ Failed to update staff role.")

    if user_updates:
        with yaspin(text="Updating user fields...", color="cyan") as spinner:
            success = updateUser(cursor, user_id, user_updates)
            if success:
                spinner.ok("✔")
                print("User fields updated successfully.")
            else:
                spinner.fail("✖ Failed to update user fields.")

    if address_updates:
        with yaspin(text="Updating address fields...", color="cyan") as spinner:
            success = updateAddress(cursor, address_id, address_updates)
            if success:
                spinner.ok("✔")
                print("Address fields updated successfully.")
            else:
                spinner.fail("✖ Failed to update address fields.")

# Main Application Loop
def display_menu():
    """
    Display the list of available commands to the user with a fancy design.
    """
    print("\n" + "═" * 40)
    print("💼  🚖  COMMAND MENU  🚖  💼".center(40))
    print("═" * 40)

    sections = [
        {
            "title": "DASHBOARD",
            "commands": [
                "dashboard - View dashboard overview",
            ],
        },
        {
            "title": "OFFICES",
            "commands": [
                "offices - Manage and view office details",
                "offices get - Get office details",
                "offices create - Create a new office",
            ],
        },
        {
            "title": "STAFF",
            "commands": [
                "staff - Manage and view staff details",
                "staff get - Get staff details",
                "staff create - Create a new staff",
                "staff update - Update staff details",
            ],
        },
        {
            "title": "DRIVERS",
            "commands": [
                "drivers - View list of drivers",
                "drivers details - Get driver details",
                "drivers create - Create a new driver",
                "driver update - Update driver details",
            ],
        },
        {
            "title": "TAXIS",
            "commands": [
                "taxis - View list of taxis",
                "taxis get - Get taxi details",
                "taxis create - Create a new taxi",
                "owner taxis - View list of taxis owned by an owner",
            ],
        },
        {
            "title": "OWNERS",
            "commands": [
                "owners - View list of owners",
                "owners get - Get owner details",
                "owners create - Create a new owner",
            ],
        },
        {
            "title": "CLIENTS",
            "commands": [
                "business clients - View list of clients",
                "business clients get - Get client details",
                "business clients create - Create a new client",
                "private clients - View list of private clients",
                "private clients get - Get private client details",
                "private clients create - Create a new private client",
            ],
        },
        {
            "title": "CONTRACTS",
            "commands": [
                "contracts - View list of contracts",
                "contracts get - Get contract details",
                "contracts create - Create a new contract",
            ],
        },
        {
            "title": "JOBS",
            "commands": [
                "job - View list of jobs",
                "job get - Get job details",
                "job create - Create a new job",
                "job finalized - Finalize a job",
                "jobs today - View jobs scheduled for today",
                "jobs driver - View jobs assigned to a driver",
                "job finalize - Finalize a job",
                "job failed - Mark a job as failed",
                "jobs by status - View jobs by status: PENDING, COMPLETED, FAILED",
                "job update - Update a job",
            ],
        },
        {
            "title": "INCOME",
            "commands": [
                "income office - Total income from an office",
                "income driver - Total income from a driver",
                "income date - Total income by date",
            ],
        },
        {
            "title": "SYSTEM",
            "commands": [
                "clear - Clear the screen",
                "menu - Display this menu",
                "quit - Exit the application",
            ],
        },
    ]

    for section in sections:
        print("\n📌 " + section["title"])
        print("─" * len(section["title"]))
        for command in section["commands"]:
            print(f"   ➜ {command}")
    print("\n" + "═" * 40)

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
            "staff update",
            "drivers",
            "drivers get",
            "drivers create",
            "driver update",
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
            "owner taxis",
            "jobs today",
            "jobs driver",
            "job finalize",
            "job failed",
            "jobs by status",
            "income office",
            "income driver",
            "income date",
            "job update",
            "menu",
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
        elif user_input == "owner taxis":
            owner_taxis(cursor)
        elif user_input == "jobs today":
            jobs_today(cursor)
        elif user_input == "jobs driver":
            jobs_driver(cursor)
        elif user_input == "job finalize":
            job_finalize(cursor)
        elif user_input == "job failed":
            job_failed(cursor)
        elif user_input == "jobs by status":
            jobs_by_status(cursor)
        elif user_input == "income office":
            total_income_from_office(cursor)
        elif user_input == "income driver":
            total_income_from_driver(cursor)
        elif user_input == "income date":
            total_income_by_date_at_office(cursor)
        elif user_input == "job update":
            update_job_prompt(cursor)
        elif user_input == "driver update":
            update_driver_prompt(cursor)
        elif user_input == "staff update":
            update_staff_prompt(cursor)
        elif user_input == "menu":
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

