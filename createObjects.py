import sqlite3

def createAddress(cursor: sqlite3.Cursor, street: str, city: str, postcode: str, country: str):
    cursor.execute("""
    INSERT INTO address (street, city, postcode, country)
    VALUES (?, ?, ?, ?)
    """, (street, city, postcode, country))
    return cursor.lastrowid

def createUser(cursor: sqlite3.Cursor, name: str, gender: str, date_of_birth: str, address_id: int = None, phone_number: str = None):
    cursor.execute("""
    INSERT INTO user (address_id, name, gender, date_of_birth, phone_number)
    VALUES (?, ?, ?, ?, ?)
    """, (address_id, name, gender, date_of_birth, phone_number))
    return cursor.lastrowid

def createOffice(cursor: sqlite3.Cursor, address_id: int, phone_number: str = None):
    cursor.execute("""
    INSERT INTO office (phone_number, address_id)
    VALUES (?, ?)
    """, (phone_number, address_id))
    return cursor.lastrowid

def createStaff(cursor: sqlite3.Cursor, user_id: int, office_id: int, role: str = 'STAFF', NIN: str = None):
    cursor.execute("""
    INSERT INTO staff (user_id, office_id, role, NIN)
    VALUES (?, ?, ?, ?)
    """, (user_id, office_id, role, NIN))
    return cursor.lastrowid

def createOwner(cursor: sqlite3.Cursor, office_id: int, user_id: int, NIN: str = None):
    cursor.execute("""
    INSERT INTO owner (office_id, user_id, NIN)
    VALUES (?, ?, ?)
    """, (office_id, user_id, NIN))
    return cursor.lastrowid

def createTaxi(cursor: sqlite3.Cursor, owner_id: int, registration_number: str, capacity: int):
    cursor.execute("""
    INSERT INTO taxi (owner_id, registration_number, capacity)
    VALUES (?, ?, ?)
    """, (owner_id, registration_number, capacity))
    return cursor.lastrowid

def createDriver(cursor: sqlite3.Cursor, user_id: int, join_date: str, owner_id: int = None, taxi_id: int = None, NIN: str = None, licence_no: str = None):
    cursor.execute("""
    INSERT INTO driver (user_id, owner_id, NIN, licence_no, join_date, taxi_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, owner_id, NIN, licence_no, join_date, taxi_id))
    return cursor.lastrowid

def createContract(cursor: sqlite3.Cursor, office_id: int, business_client_id: int, signed_on: str, no_jobs: int = 0, flat_fees: float = None):
    cursor.execute("""
    INSERT INTO contract (office_id, business_client_id, signed_on, no_jobs, flat_fees)
    VALUES (?, ?, ?, ?, ?)
    """, (office_id, business_client_id, signed_on, no_jobs, flat_fees))
    return cursor.lastrowid

def createClient(cursor: sqlite3.Cursor, private_client_id: int = None, business_client_id: int = None):
    cursor.execute("""
    INSERT INTO client (private_client_id, business_client_id)
    VALUES (?, ?)
    """, (private_client_id, business_client_id))
    return cursor.lastrowid

def createBusinessClient(cursor: sqlite3.Cursor, hst_number: str, address_id: int):
    cursor.execute("""
    INSERT INTO business_client (hst_number, address_id)
    VALUES (?, ?)
    """, (hst_number, address_id))
    return cursor.lastrowid

def createPrivateClient(cursor: sqlite3.Cursor, user_id: int, join_date: str):
    cursor.execute("""
    INSERT INTO private_client (user_id, join_date)
    VALUES (?, ?)
    """, (user_id, join_date))
    return cursor.lastrowid

def createJob(cursor: sqlite3.Cursor, driver_id: int, client_id: int, mileage: float, charge: float, pickup_date: str, dropoff_date: str, address_id: int, status: str = 'PENDING', failure_reason: str = None, contract_id: int = None):
    cursor.execute("""
    INSERT INTO job (driver_id, client_id, contract_id, mileage, charge, status, failure_reason, pickup_date, dropoff_date, address_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (driver_id, client_id, contract_id, mileage, charge, status, failure_reason, pickup_date, dropoff_date, address_id))
    return cursor.lastrowid
