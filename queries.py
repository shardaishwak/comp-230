import sqlite3

def getTotalOffices(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM office;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getOffices(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT office.office_id, office.phone_number, address.street, address.city, address.postcode, address.country FROM office JOIN address ON office.address_id = address.address_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getOfficeDetails(cursor: sqlite3.Cursor, office_id: int) -> dict:
    query = """
    SELECT office.*, address.street, address.city, address.postcode, address.country FROM office JOIN address ON office.address_id = address.address_id WHERE office_id = ?;
    """
    cursor.execute(query, (office_id,))
    return cursor.fetchone()

# user
def getUserDetails(cursor: sqlite3.Cursor, user_id: int) -> dict:
    query = """
    SELECT user.*, address.street, address.city, address.postcode, address.country FROM user JOIN address ON user.address_id = address.address_id WHERE user_id = ?;
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchone()


# staff
def getTotalStaff(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM staff;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getStaffs(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT staff.*, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country FROM staff JOIN user ON staff.user_id = user.user_id JOIN office ON staff.office_id = office.office_id JOIN address ON office.address_id = address.address_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getStaffDetails(cursor: sqlite3.Cursor, staff_id: int) -> dict:
    query = """
    SELECT staff.*, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country FROM staff JOIN user ON staff.user_id = user.user_id JOIN office ON staff.office_id = office.office_id JOIN address ON office.address_id = address.address_id WHERE staff_id = ?;
    """
    cursor.execute(query, (staff_id,))
    return cursor.fetchone()


# Drivers
def getTotalDrivers(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM driver;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getDrivers(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT driver.driver_id, driver.NIN, driver.licence_no, driver.join_date, driver.taxi_id, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country
        FROM driver 
        JOIN user ON driver.user_id = user.user_id 
        JOIN address ON user.address_id = address.address_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getDriverDetails(cursor: sqlite3.Cursor, driver_id: int) -> dict:
    query = """
    SELECT driver.driver_id, driver.NIN, driver.licence_no, driver.join_date, driver.taxi_id, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country
        FROM driver
        JOIN user ON driver.user_id = user.user_id
        JOIN address ON user.address_id = address.address_id
        WHERE driver_id = ?;
    """
    cursor.execute(query, (driver_id,))
    return cursor.fetchone()


# owners
def getTotalOwners(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM owner;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getOwners(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT owner.owner_id, office.office_id, owner.NIN, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country
        FROM owner 
        JOIN office ON office.office_id = owner.office_id 
        JOIN user ON user.user_id = owner.user_id 
        JOIN address ON address.address_id = user.address_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getOwnerDetails(cursor: sqlite3.Cursor, owner_id: int) -> dict:
    query = """
    SELECT owner.owner_id, office.office_id, owner.NIN, user.name, user.gender, user.date_of_birth, user.phone_number, address.street, address.city, address.postcode, address.country
        FROM owner
        JOIN office ON office.office_id = owner.office_id
        JOIN user ON user.user_id = owner.user_id
        JOIN address ON address.address_id = user.address_id
        WHERE owner_id = ?;
    """
    cursor.execute(query, (owner_id,))
    return cursor.fetchone()


# Taxis
def getTotalTaxis(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM taxi;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getTaxis(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT * FROM taxi;
    """
    cursor.execute(query)
    return cursor.fetchall()

# Contracts
def getTotalContracts(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM contract;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

# Clients
def getTotalClients(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM client;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

# Active Jobs
def getTotalActiveJobs(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM job WHERE status = 'PENDING';
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

# Recent Activity
def getRecentActivity(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT job.*, address.street, address.city, address.postcode, address.country FROM job JOIN address ON address.address_id = job.address_id ORDER BY job_id DESC LIMIT 5;
    """
    cursor.execute(query)
    return cursor.fetchall()