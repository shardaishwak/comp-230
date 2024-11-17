import sqlite3

def createAddressTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS address (
        address_id INTEGER PRIMARY KEY AUTOINCREMENT,
        street VARCHAR(100)  NOT NULL,
        city VARCHAR(50) NOT NULL,
        postcode VARCHAR(10) NOT NULL,
        country VARCHAR(50) NOT NULL
    )
    """)

def createUserTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        address_id INTEGER,
        name VARCHAR(100) NOT NULL,
        gender VARCHAR(20) CHECK( gender IN ('MALE', 'FEMALE', 'OTHER')) NOT NULL DEFAULT 'OTHER',
        date_of_birth DATE NOT NULL,
        phone_number VARCHAR(15),
        FOREIGN KEY (address_id) REFERENCES address(address_id) ON DELETE SET NULL ON UPDATE CASCADE
    )
    """)
    
def createOfficeTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS office (
        office_id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number VARCHAR(15),
        address_id INTEGER NOT NULL,
        FOREIGN KEY (address_id) REFERENCES address(address_id)
    )
    """)

def createStaffTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        office_id INTEGER NOT NULL,
        role VARCHAR(20) CHECK(role IN ('MANAGER', 'STAFF')) NOT NULL DEFAULT 'STAFF',
        NIN VARCHAR(9) UNIQUE,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (office_id) REFERENCES office(office_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
    """)


def createOwnerTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS owner (
        owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
        office_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        NIN VARCHAR(9) UNIQUE,
        FOREIGN KEY (office_id) REFERENCES office(office_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
    """)


def createTaxiTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS taxi (
        taxi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER NOT NULL,
        registration_number VARCHAR(10) UNIQUE,
        capacity INTEGER NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES owner(owner_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
    """)

def createDriverTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS driver (
        driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        owner_id INTEGER,
        NIN VARCHAR(9) UNIQUE,
        licence_no VARCHAR(10) UNIQUE,
        join_date DATE NOT NULL,
        taxi_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (owner_id) REFERENCES owner(owner_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (taxi_id) REFERENCES taxi(taxi_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
    """)

def createContractTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contract (
        contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
        office_id INTEGER NOT NULL,
        business_client_id INTEGER NOT NULL,
        signed_on DATE NOT NULL,
        no_jobs INTEGER DEFAULT 0,
        flat_fees DECIMAL(10, 2),
        FOREIGN KEY (office_id) REFERENCES office(office_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (business_client_id) REFERENCES business_client(business_client_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        UNIQUE (office_id, business_client_id)
    )
    """)

def createClientTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS client (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        private_client_id INTEGER DEFAULT NULL,
        business_client_id INTEGER DEFAULT NULL,
        FOREIGN KEY (private_client_id) REFERENCES private_client(private_client_id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (business_client_id) REFERENCES business_client(business_client_id) ON DELETE SET NULL ON UPDATE CASCADE
    )
    """)

def createBusinessClientTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS business_client (
        business_client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hst_number VARCHAR(15) UNIQUE NOT NULL,
        address_id INTEGER NOT NULL,
        FOREIGN KEY (address_id) REFERENCES address(address_id) ON DELETE SET NULL ON UPDATE CASCADE
    )
    """)

def createPrivateClientTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS private_client (
        private_client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        join_date DATE NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
    """)

def createJobTable(cursor: sqlite3.Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        driver_id INTEGER NOT NULL,
        client_id INTEGER NOT NULL,
        contract_id INTEGER DEFAULT NULL,
        mileage DECIMAL(10, 2) NOT NULL,
        charge DECIMAL(10, 2) NOT NULL,
        status VARCHAR(20) CHECK(status IN ('PENDING', 'COMPLETED', 'FAILED')) NOT NULL DEFAULT 'PENDING',
        failure_reason TEXT DEFAULT NULL,
        pickup_date DATE NOT NULL,
        dropoff_date DATE NOT NULL,
        address_id INTEGER NOT NULL,
        FOREIGN KEY (driver_id) REFERENCES driver(driver_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE NO ACTION ON UPDATE CASCADE,
        FOREIGN KEY (contract_id) REFERENCES contract(contract_id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (address_id) REFERENCES address(address_id) ON DELETE SET NULL ON UPDATE CASCADE
    )
    """)


def createTables(cursor: sqlite3.Cursor):
    createAddressTable(cursor)
    createUserTable(cursor)
    createOfficeTable(cursor)
    createStaffTable(cursor)
    createOwnerTable(cursor)
    createTaxiTable(cursor)
    createDriverTable(cursor)
    createContractTable(cursor)
    createClientTable(cursor)
    createBusinessClientTable(cursor)
    createPrivateClientTable(cursor)
    createJobTable(cursor)
