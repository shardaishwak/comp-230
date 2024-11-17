import sqlite3
from contextlib import closing
from createTables import createTables
from pprint import pprint
from createObjects import *
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def printRecordCounts(cursor: sqlite3.Cursor):
    # Query to get all table names in the database
    cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';
    """)
    tables = cursor.fetchall()

    logging.info("Number of Records in Each Table:")
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"{table_name}: {count}")

def main(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    createTables(cursor)

    # demo data
    address_id1 = createAddress(cursor, "123 Elm St", "Metropolis", "12345", "USA")
    address_id2 = createAddress(cursor, "456 Oak Rd", "Gotham", "54321", "Canada")
    address_id3 = createAddress(cursor, "789 Maple Ave", "Star City", "67890", "UK")
    logging.info(f"Inserted Address IDs: {address_id1}, {address_id2}, {address_id3}")


    user_id1 = createUser(cursor, name="John Doe", gender="MALE", date_of_birth="1990-01-01", address_id=address_id1, phone_number="123-456-7890")
    user_id2 = createUser(cursor, name="Jane Smith", gender="FEMALE", date_of_birth="1985-05-12", address_id=address_id2)
    user_id3 = createUser(cursor, name="Sam Wilson", gender="OTHER", date_of_birth="1995-07-20", phone_number="098-765-4321")
    logging.info(f"Inserted User IDs: {user_id1}, {user_id2}, {user_id3}")

    office_id1 = createOffice(cursor, address_id=address_id1, phone_number="555-1234")
    office_id2 = createOffice(cursor, address_id=address_id2)
    logging.info(f"Inserted Office IDs: {office_id1}, {office_id2}")


    staff_id1 = createStaff(cursor, user_id=user_id1, office_id=office_id1, role="MANAGER", NIN="AB1234567")
    staff_id2 = createStaff(cursor, user_id=user_id2, office_id=office_id2, NIN="CD9876543")
    logging.info(f"Inserted Staff IDs: {staff_id1}, {staff_id2}")

    owner_id1 = createOwner(cursor, office_id=office_id1, user_id=user_id1, NIN="EF6543210")
    owner_id2 = createOwner(cursor, office_id=office_id2, user_id=user_id2)
    logging.info(f"Inserted Owner IDs: {owner_id1}, {owner_id2}")

    taxi_id1 = createTaxi(cursor, owner_id=owner_id1, registration_number="ABC123", capacity=4)
    taxi_id2 = createTaxi(cursor, owner_id=owner_id2, registration_number="XYZ789", capacity=6)
    logging.info(f"Inserted Taxi IDs: {taxi_id1}, {taxi_id2}")

    driver_id1 = createDriver(cursor, user_id=user_id1, join_date="2023-01-01", owner_id=owner_id1, taxi_id=taxi_id1, NIN="GH1234567", licence_no="LIC1234")
    driver_id2 = createDriver(cursor, user_id=user_id2, join_date="2023-02-15", owner_id=owner_id2, taxi_id=taxi_id2, NIN="IJ9876543", licence_no="LIC5678")
    logging.info(f"Inserted Driver IDs: {driver_id1}, {driver_id2}")

    contract_id1 = createContract(cursor, office_id=office_id1, business_client_id=1, signed_on="2023-03-01", no_jobs=5, flat_fees=500.00)
    contract_id2 = createContract(cursor, office_id=office_id2, business_client_id=2, signed_on="2023-04-10", flat_fees=750.00)
    logging.info(f"Inserted Contract IDs: {contract_id1}, {contract_id2}")

    client_id1 = createClient(cursor, private_client_id=1)
    client_id2 = createClient(cursor, business_client_id=1)
    logging.info(f"Inserted Client IDs: {client_id1}, {client_id2}")

    business_client_id1 = createBusinessClient(cursor, hst_number="HST12345", address_id=address_id1)
    business_client_id2 = createBusinessClient(cursor, hst_number="HST67890", address_id=address_id2)
    logging.info(f"Inserted Business Client IDs: {business_client_id1}, {business_client_id2}")

    private_client_id1 = createPrivateClient(cursor, user_id=user_id1, join_date="2023-05-20")
    private_client_id2 = createPrivateClient(cursor, user_id=user_id2, join_date="2023-06-15")
    logging.info(f"Inserted Private Client IDs: {private_client_id1}, {private_client_id2}")

    job_id1 = createJob(cursor, driver_id=driver_id1, client_id=client_id1, mileage=15.5, charge=100.0, pickup_date="2023-07-01", dropoff_date="2023-07-01", address_id=address_id1)
    job_id2 = createJob(cursor, driver_id=driver_id2, client_id=client_id2, mileage=25.0, charge=150.0, pickup_date="2023-07-15", dropoff_date="2023-07-15", address_id=address_id2, failure_reason="Flat tire")
    logging.info(f"Inserted Job IDs: {job_id1}, {job_id2}")


with closing(sqlite3.connect('database.db')) as connection:
    with closing(connection.cursor()) as cursor:
        logging.info("Database connection established")
        logging.info(f'Total changes: {connection.total_changes}')
        logging.info(f'Isolation level: {connection.isolation_level}')
        logging.info(f'Row factory: {connection.row_factory}')
        logging.info(f'Cursor description: {cursor.description}')
        total_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        logging.info(f'Tables: {total_tables}')
        printRecordCounts(cursor)


        main(connection, cursor)

        connection.commit()

        logging.info("\nAfter inserting records:")
        printRecordCounts(cursor)



