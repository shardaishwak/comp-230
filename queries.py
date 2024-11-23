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
    SELECT taxi.taxi_id, taxi.registration_number, taxi.capacity, user.name as ownerName FROM taxi JOIN owner ON taxi.owner_id = owner.owner_id JOIN user ON owner.user_id = user.user_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getTaxiDetails(cursor: sqlite3.Cursor, taxi_id: int) -> dict:
    query = """
    SELECT taxi.taxi_id, taxi.registration_number, taxi.capacity, user.name as ownerName FROM taxi JOIN owner ON taxi.owner_id = owner.owner_id JOIN user ON owner.user_id = user.user_id
    WHERE taxi_id = ?;
    """
    cursor.execute(query, (taxi_id,))
    return cursor.fetchone()

# Contracts
def getTotalContracts(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM contract;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getContracts(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT contract.contract_id, contract.signed_on, contract.no_jobs, contract.flat_fees, office.office_id, business_client.business_client_id FROM contract JOIN office ON contract.office_id = office.office_id JOIN business_client ON contract.business_client_id = business_client.business_client_id
    """
    cursor.execute(query)
    return cursor.fetchall()

def getContractDetails(cursor: sqlite3.Cursor, contract_id: int) -> dict:
    query = """
    SELECT contract.contract_id, contract.signed_on, contract.no_jobs, contract.flat_fees, office.office_id, business_client.business_client_id FROM contract JOIN office ON contract.office_id = office.office_id JOIN business_client ON contract.business_client_id = business_client.business_client_id
    WHERE contract_id = ?;
    """
    cursor.execute(query, (contract_id,))
    return cursor.fetchone()


# Clients
def getTotalClients(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM client;
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getBusinessClients(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT business_client_id, hst_number, address.street, address.city, address.postcode, address.country
      FROM business_client 
        JOIN address ON business_client.address_id = address.address_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getBusinessClientDetails(cursor: sqlite3.Cursor, business_client_id: int) -> dict:
    query = """
    SELECT business_client_id, hst_number, address.street, address.city, address.postcode, address.country
      FROM business_client 
        JOIN address ON business_client.address_id = address.address_id
      WHERE business_client_id = ?;
    """
    cursor.execute(query, (business_client_id,))
    return cursor.fetchone()

def getPrivateClients(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT * FROM private_client;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getPrivateClientDetails(cursor: sqlite3.Cursor, private_client_id: int) -> dict:
    query = """
    SELECT * FROM private_client WHERE private_client_id = ?;
    """
    cursor.execute(query, (private_client_id,))
    return cursor.fetchone()



# Active Jobs
def getTotalActiveJobs(cursor: sqlite3.Cursor) -> int:
    query = """
    SELECT COUNT(*) FROM job WHERE status = 'PENDING';
    """
    cursor.execute(query)
    return cursor.fetchone()[0]

def getJobs(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT job.job_id, job.client_id, job.contract_id, job.mileage, job.charge, job.status, job.pickup_date, job.dropoff_date, driverUser.name as driverName, address.street, address.city, address.postcode, address.country
    FROM job 
    JOIN address ON address.address_id = job.address_id
    JOIN driver ON driver.driver_id = job.driver_id
    JOIN user driverUser ON driverUser.user_id = driver.user_id;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getJobDetails(cursor: sqlite3.Cursor, job_id: int) -> dict:
    query = """
    SELECT job.job_id, job.client_id, job.contract_id, job.mileage, job.charge, job.status, job.pickup_date, job.dropoff_date, driverUser.name as driverName, address.street, address.city, address.postcode, address.country
    FROM job 
    JOIN address ON address.address_id = job.address_id
    JOIN driver ON driver.driver_id = job.driver_id
    JOIN user driverUser ON driverUser.user_id = driver.user_id
    WHERE job_id = ?;
    """
    cursor.execute(query, (job_id,))
    return cursor.fetchone()

# Recent Activity
def getRecentActivity(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT job.*, address.street, address.city, address.postcode, address.country FROM job JOIN address ON address.address_id = job.address_id ORDER BY job_id DESC LIMIT 5;
    """
    cursor.execute(query)
    return cursor.fetchall()


# Get today jobs
def getTodayJobs(cursor: sqlite3.Cursor) -> list:
    query = """
    SELECT job.*, address.street, address.city, address.postcode, address.country FROM job JOIN address ON address.address_id = job.address_id WHERE pickup_date = date('now') ORDER BY job_id DESC;
    """
    cursor.execute(query)
    return cursor.fetchall()

def getOwnerTaxis(cursor: sqlite3.Cursor, owner_id: int) -> list:
    query = """
    SELECT taxi.taxi_id, taxi.registration_number, taxi.capacity FROM taxi WHERE owner_id = ?;
    """
    cursor.execute(query, (owner_id,))
    return cursor.fetchall()

def getDriverJobs(cursor: sqlite3.Cursor, driver_id: int) -> list:
    query = """
    SELECT job.job_id, job.client_id, job.contract_id, job.mileage, job.charge, job.status, job.pickup_date, job.dropoff_date, address.street, address.city, address.postcode, address.country
    FROM job 
    JOIN address ON address.address_id = job.address_id
    WHERE driver_id = ?;
    """
    cursor.execute(query, (driver_id,))
    return cursor.fetchall()


def finalizeJob(cursor: sqlite3.Cursor, job_id: int, mileage: int, charge: int) -> None:
    query = """
    UPDATE job SET status = 'COMPLETED', mileage = ?, charge = ? WHERE job_id = ?;
    """
    cursor.execute(query, (mileage, charge, job_id))

def finalizeJobFailed(cursor: sqlite3.Cursor, job_id: int, failure_reason) -> None:
    query = """
    UPDATE job SET status = 'FAILED', failure_reason = ? WHERE job_id = ?;
    """
    cursor.execute(query, (failure_reason, job_id))

def getJobsByStatus(cursor: sqlite3.Cursor, status: str) -> list:
    query = """
    SELECT job.job_id, job.client_id, job.contract_id, job.mileage, job.charge, job.status, job.pickup_date, job.dropoff_date, driverUser.name as driverName, address.street, address.city, address.postcode, address.country
    FROM job 
    JOIN address ON address.address_id = job.address_id
    JOIN driver ON driver.driver_id = job.driver_id
    JOIN user driverUser ON driverUser.user_id = driver.user_id
    WHERE job.status = ?;
    """
    cursor.execute(query, (status,))
    return cursor.fetchall()

def getTotalIncomeByOffice(cursor: sqlite3.Cursor, office_id: int) -> int:
    query = """
    SELECT SUM(charge) FROM job WHERE office_id = ? AND status = 'COMPLETED';
    """
    cursor.execute(query, (office_id,))
    return cursor.fetchone()[0]

def getTotalIncomeByDriver(cursor: sqlite3.Cursor, driver_id: int) -> int:
    query = """
    SELECT SUM(charge) FROM job WHERE driver_id = ? AND status = 'COMPLETED';
    """
    cursor.execute(query, (driver_id,))
    return cursor.fetchone()[0]

def getTotalIncomeByDateAtOffice(cursor: sqlite3.Cursor, office_id: int, date: str) -> int:
    query = """
    SELECT SUM(charge) FROM job WHERE office_id = ? AND status = 'COMPLETED' AND pickup_date = ?;
    """
    cursor.execute(query, (office_id, date))
    return cursor.fetchone()[0]