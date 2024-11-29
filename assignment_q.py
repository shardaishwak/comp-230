import sqlite3
import logging
from helpers import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query1(cursor: sqlite3.Cursor):
    query = """
        SELECT user.user_id, user.name, user.phone_number FROM user JOIN staff ON user.user_id = staff.user_id WHERE staff.role = 'MANAGER';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])
    


def query2(cursor: sqlite3.Cursor):
    query = """
        SELECT user.name FROM user JOIN driver ON driver.user_id = user.user_id WHERE user.gender = 'FEMALE';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query3(cursor: sqlite3.Cursor):
    query = """
        SELECT staff.office_id, Count(*) as total FROM staff GROUP BY staff.office_id;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query4(cursor: sqlite3.Cursor):
    query = """
        SELECT * FROM taxi JOIN owner ON taxi.owner_id = owner.owner_id JOIN office ON owner.office_id = office.office_id JOIN address ON office.address_id = address.address_id WHERE address.city = 'Glasgow';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query5(cursor: sqlite3.Cursor):
    ## TODO: Create a taxi that has this registration number
    query = """
        SELECT COUNT(*) as total FROM taxi WHERE taxi.registration_number LIKE '%W%';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query6(cursor: sqlite3.Cursor):
    query = """
       SELECT taxi.taxi_id, COUNT(*) as total FROM taxi JOIN driver ON driver.taxi_id = taxi.taxi_id GROUP BY taxi.taxi_id; 
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query7(cursor: sqlite3.Cursor):
    query = """
        SELECT user.name, user.phone_number FROM user JOIN owner ON owner.user_id = user.user_id JOIN taxi ON taxi.owner_id = owner.owner_id GROUP BY user.name HAVING COUNT(taxi.taxi_id) > 1;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])


def query8(cursor: sqlite3.Cursor):
    query = """
        SELECT business_client.business_client_id, address.street, address.city, address.postcode, address.country from address JOIN business_client ON address.address_id = business_client.address_id WHERE address.city = 'Glasgow';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query9(cursor: sqlite3.Cursor):
    query = """
        SELECT contract_id, office_id, contract.business_client_id, signed_on, no_jobs, flat_fees FROM contract JOIN business_client ON contract.business_client_id = business_client.business_client_id JOIN address ON address.address_id = business_client.address_id WHERE address.city = 'Glasgow';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query10(cursor: sqlite3.Cursor):
    query = """
        SELECT address.city , COUNT(*) as total from address JOIN user ON user.address_id = address.address_id JOIN private_client ON private_client.user_id = user.user_id GROUP BY address.city;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query11(cursor: sqlite3.Cursor):
    query = """
        SELECT driver.driver_id, user.name, COUNT(*) as total_jobs 
            FROM driver 
            JOIN job ON job.driver_id = driver.driver_id 
            JOIN user ON user.user_id = driver.user_id
            WHERE job.pickup_date = '2023-07-01' AND driver.driver_id = 1
            GROUP BY driver.driver_id;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query12(cursor: sqlite3.Cursor):
    query = """
        SELECT user.name, (strftime('%Y', 'now') - strftime('%Y', user.date_of_birth)) 
        - (strftime('%m-%d', 'now') < strftime('%m-%d', user.date_of_birth)) AS age
        FROM user
        JOIN driver ON driver.user_id = user.user_id
        WHERE age > 55;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query13(cursor: sqlite3.Cursor):
    
    query = """
        SELECT user.name, user.phone_number FROM user JOIN private_client ON private_client.user_id = user.user_id JOIN client ON client.private_client_id = private_client.private_client_id JOIN job ON job.client_id = client.client_id WHERE job.pickup_date BETWEEN '2000-11-01' AND '2000-11-30';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])
    
def query14(cursor: sqlite3.Cursor):
    query = """
        SELECT user.name, address.street, address.city, address.postcode, address.country FROM user JOIN address ON user.address_id = address.address_id JOIN private_client ON private_client.user_id = user.user_id JOIN client ON client.private_client_id = private_client.private_client_id JOIN job ON job.client_id = client.client_id GROUP BY user.name HAVING COUNT(job.job_id) > 3;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query15(cursor: sqlite3.Cursor):
    query = """
        SELECT AVG(job.mileage) as average_mileage FROM job WHERE job.job_id = 1;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query16(cursor: sqlite3.Cursor):
    query = """
        SELECT taxi.registration_number, COUNT(*) as total_jobs FROM taxi JOIN driver ON driver.taxi_id = taxi.taxi_id JOIN job ON job.driver_id = driver.driver_id GROUP BY taxi.registration_number;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query17(cursor: sqlite3.Cursor):
    query = """
        SELECT driver.driver_id, user.name, COUNT(*) as total_jobs FROm driver JOIN job ON job.driver_id = driver.driver_id JOIN user ON user.user_id = driver.user_id GROUP BY driver.driver_id;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])

def query18(cursor: sqlite3.Cursor):
    query = """
        SELECT SUM(job.charge) as total_charge FROM job WHERE job.pickup_date BETWEEN '2000-11-01' AND '2000-11-30';
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])


def query19(cursor: sqlite3.Cursor):
    query = """
        SELECT COUNT(*) as total_jobs, SUM(job.mileage) as total_miles FROM job WHERE job.contract_id = 1;
    """

    rows = cursor.execute(query).fetchall()
    print_table(rows, column_names=[desc[0] for desc in cursor.description])