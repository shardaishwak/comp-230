import sqlite3
from contextlib import closing
from createTables import createTables
from pprint import pprint
from createObjects import *
import logging
from scripts import *
from helpers import *
import sys
from assignment_q import *
import os

def populate_data(cursor):
    
    address_ids = {}
    
    address_ids['Glasgow1'] = createAddress(cursor, '123 Glasgow Street', 'Glasgow', 'G1 1AA', 'Scotland')
    address_ids['Glasgow2'] = createAddress(cursor, '456 Glasgow Road', 'Glasgow', 'G1 2BB', 'Scotland')
    
    address_ids['Edinburgh1'] = createAddress(cursor, '789 Edinburgh Street', 'Edinburgh', 'EH1 1AA', 'Scotland')
    address_ids['London1'] = createAddress(cursor, '101 London Road', 'London', 'SW1A 1AA', 'England')
    address_ids['Manchester1'] = createAddress(cursor, '202 Manchester Ave', 'Manchester', 'M1 1AA', 'England')
    address_ids['Liverpool1'] = createAddress(cursor, '303 Liverpool Lane', 'Liverpool', 'L1 1AA', 'England')

    
    user_ids = {}
    
    user_ids['manager1'] = createUser(cursor, 'John Doe', 'MALE', '1960-05-15', address_ids['Glasgow1'], '07123456789')
    user_ids['manager2'] = createUser(cursor, 'Jane Manager', 'FEMALE', '1970-07-20', address_ids['Edinburgh1'], '07234567890')
    user_ids['manager3'] = createUser(cursor, 'Mike Manager', 'MALE', '1965-03-30', address_ids['London1'], '07345678901')
    
    user_ids['staff1'] = createUser(cursor, 'Sarah Staff', 'FEMALE', '1985-08-20', address_ids['Glasgow2'], '07456789012')
    user_ids['staff2'] = createUser(cursor, 'Tom Staff', 'MALE', '1990-09-25', address_ids['Edinburgh1'], '07567890123')
    
    user_ids['driver1'] = createUser(cursor, 'Alice Johnson', 'FEMALE', '1980-03-10', address_ids['Manchester1'], '07678901234')
    user_ids['driver2'] = createUser(cursor, 'Emily Driver', 'FEMALE', '1995-12-05', address_ids['Liverpool1'], '07789012345')
    user_ids['driver3'] = createUser(cursor, 'Emma Driver', 'FEMALE', '1982-05-15', address_ids['Glasgow1'], '07890123456')
    
    user_ids['driver4'] = createUser(cursor, 'Bob Brown', 'MALE', '1975-06-22', address_ids['Edinburgh1'], '07901234567')
    user_ids['driver5'] = createUser(cursor, 'Charlie Driver', 'MALE', '1990-10-10', address_ids['Manchester1'], '07012345678')
    
    user_ids['driver_old1'] = createUser(cursor, 'Henry Oldman', 'MALE', '1940-04-04', address_ids['Glasgow2'], '07123456780')
    user_ids['driver_old2'] = createUser(cursor, 'Olivia Senior', 'FEMALE', '1950-06-06', address_ids['Edinburgh1'], '07234567891')
    
    user_ids['owner1'] = createUser(cursor, 'Owner One', 'MALE', '1965-07-22', address_ids['Glasgow1'], '07345678902')
    user_ids['owner2'] = createUser(cursor, 'Owner Two', 'MALE', '1970-08-15', address_ids['Edinburgh1'], '07456789013')
    user_ids['owner3'] = createUser(cursor, 'Owner Three', 'FEMALE', '1980-09-09', address_ids['London1'], '07567890124')
    
    user_ids['private_client1'] = createUser(cursor, 'Eve White', 'FEMALE', '1990-01-01', address_ids['London1'], '07678901235')
    user_ids['private_client2'] = createUser(cursor, 'Frank Green', 'MALE', '1988-02-02', address_ids['Edinburgh1'], '07789012346')
    user_ids['private_client3'] = createUser(cursor, 'Grace Pink', 'FEMALE', '1982-03-03', address_ids['Glasgow2'], '07890123457')
    user_ids['private_client4'] = createUser(cursor, 'Hannah Blue', 'FEMALE', '1985-04-04', address_ids['Manchester1'], '07901234568')
    user_ids['private_client5'] = createUser(cursor, 'Ian Orange', 'MALE', '1987-05-05', address_ids['Liverpool1'], '07012345679')

    
    office_ids = {}
    office_ids['Glasgow'] = createOffice(cursor, address_ids['Glasgow1'], '07123456789')
    office_ids['Edinburgh'] = createOffice(cursor, address_ids['Edinburgh1'], '07234567890')
    office_ids['London'] = createOffice(cursor, address_ids['London1'], '07345678901')

    
    staff_ids = {}
    staff_ids['manager1'] = createStaff(cursor, user_ids['manager1'], office_ids['Glasgow'], 'MANAGER', 'NIN001')
    staff_ids['manager2'] = createStaff(cursor, user_ids['manager2'], office_ids['Edinburgh'], 'MANAGER', 'NIN002')
    staff_ids['manager3'] = createStaff(cursor, user_ids['manager3'], office_ids['London'], 'MANAGER', 'NIN003')
    staff_ids['staff1'] = createStaff(cursor, user_ids['staff1'], office_ids['Glasgow'], 'STAFF', 'NIN004')
    staff_ids['staff2'] = createStaff(cursor, user_ids['staff2'], office_ids['Edinburgh'], 'STAFF', 'NIN005')

    
    owner_ids = {}
    owner_ids['owner1'] = createOwner(cursor, office_ids['Glasgow'], user_ids['owner1'], 'NIN101')
    owner_ids['owner2'] = createOwner(cursor, office_ids['Edinburgh'], user_ids['owner2'], 'NIN102')
    owner_ids['owner3'] = createOwner(cursor, office_ids['London'], user_ids['owner3'], 'NIN103')

    
    taxi_ids = {}
    
    taxi_ids['taxi1'] = createTaxi(cursor, owner_ids['owner1'], 'GLA123W', 4)  
    taxi_ids['taxi2'] = createTaxi(cursor, owner_ids['owner1'], 'GLA456W', 4)  
    taxi_ids['taxi3'] = createTaxi(cursor, owner_ids['owner1'], 'GLA789', 4)
    
    taxi_ids['taxi4'] = createTaxi(cursor, owner_ids['owner2'], 'EDI123W', 4)  
    taxi_ids['taxi5'] = createTaxi(cursor, owner_ids['owner2'], 'EDI456', 4)
    
    taxi_ids['taxi6'] = createTaxi(cursor, owner_ids['owner3'], 'LON123W', 4)  
    taxi_ids['taxi7'] = createTaxi(cursor, owner_ids['owner3'], 'LON456', 4)
    taxi_ids['taxi8'] = createTaxi(cursor, owner_ids['owner3'], 'LON789', 4)
    

    
    driver_ids = {}
    driver_ids['driver1'] = createDriver(cursor, user_ids['driver1'], '2015-01-01', None, taxi_ids['taxi1'], 'NIN201', 'LIC001')
    driver_ids['driver2'] = createDriver(cursor, user_ids['driver2'], '2016-01-01', None, taxi_ids['taxi2'], 'NIN202', 'LIC002')
    driver_ids['driver3'] = createDriver(cursor, user_ids['driver3'], '2017-01-01', None, taxi_ids['taxi3'], 'NIN203', 'LIC003')
    driver_ids['driver4'] = createDriver(cursor, user_ids['driver4'], '2018-01-01', None, taxi_ids['taxi4'], 'NIN204', 'LIC004')
    driver_ids['driver5'] = createDriver(cursor, user_ids['driver5'], '2019-01-01', None, taxi_ids['taxi5'], 'NIN205', 'LIC005')
    driver_ids['driver_old1'] = createDriver(cursor, user_ids['driver_old1'], '2010-01-01', None, taxi_ids['taxi6'], 'NIN206', 'LIC006')
    driver_ids['driver_old2'] = createDriver(cursor, user_ids['driver_old2'], '2010-01-01', None, taxi_ids['taxi7'], 'NIN207', 'LIC007')

    
    business_client_ids = {}
    business_client_ids['business1'] = createBusinessClient(cursor, 'HST001', address_ids['Glasgow1'])
    business_client_ids['business2'] = createBusinessClient(cursor, 'HST002', address_ids['Glasgow2'])
    business_client_ids['business3'] = createBusinessClient(cursor, 'HST003', address_ids['Edinburgh1'])
    business_client_ids['business4'] = createBusinessClient(cursor, 'HST004', address_ids['London1'])

    
    contract_ids = {}
    contract_ids['contract1'] = createContract(cursor, office_ids['Glasgow'], business_client_ids['business1'], '2023-01-01', 0, 1000.0)
    contract_ids['contract2'] = createContract(cursor, office_ids['Glasgow'], business_client_ids['business2'], '2023-02-01', 0, 1500.0)
    contract_ids['contract3'] = createContract(cursor, office_ids['Edinburgh'], business_client_ids['business3'], '2023-03-01', 0, 2000.0)

    
    client_ids = {}
    
    private_client_ids = {}
    private_client_ids['private1'] = createPrivateClient(cursor, user_ids['private_client1'], '2022-01-01')
    private_client_ids['private2'] = createPrivateClient(cursor, user_ids['private_client2'], '2022-02-01')
    private_client_ids['private3'] = createPrivateClient(cursor, user_ids['private_client3'], '2022-03-01')
    private_client_ids['private4'] = createPrivateClient(cursor, user_ids['private_client4'], '2022-04-01')
    private_client_ids['private5'] = createPrivateClient(cursor, user_ids['private_client5'], '2022-05-01')

    for key in private_client_ids:
        client_ids[key] = createClient(cursor, private_client_ids[key], None)

    
    for key in business_client_ids:
        client_ids[key] = createClient(cursor, None, business_client_ids[key])

    
    
    createJob(cursor, driver_ids['driver1'], client_ids['private1'], 10.0, 50.0, '2023-07-01', '2023-07-01', address_ids['London1'])
    createJob(cursor, driver_ids['driver1'], client_ids['private2'], 15.0, 75.0, '2023-07-01', '2023-07-01', address_ids['London1'])
    createJob(cursor, driver_ids['driver1'], client_ids['private3'], 20.0, 100.0, '2023-07-01', '2023-07-01', address_ids['London1'])

    
    createJob(cursor, driver_ids['driver2'], client_ids['private1'], 12.0, 60.0, '2000-11-10', '2000-11-10', address_ids['Edinburgh1'])
    createJob(cursor, driver_ids['driver2'], client_ids['private2'], 8.0, 40.0, '2000-11-15', '2000-11-15', address_ids['Edinburgh1'])
    createJob(cursor, driver_ids['driver3'], client_ids['private3'], 6.0, 30.0, '2000-11-20', '2000-11-20', address_ids['Edinburgh1'])
    createJob(cursor, driver_ids['driver4'], client_ids['private4'], 10.0, 50.0, '2000-11-25', '2000-11-25', address_ids['Edinburgh1'])

    
    
    createJob(cursor, driver_ids['driver1'], client_ids['private3'], 10.0, 50.0, '2023-08-01', '2023-08-01', address_ids['Glasgow1'])
    createJob(cursor, driver_ids['driver1'], client_ids['private3'], 12.0, 60.0, '2023-08-05', '2023-08-05', address_ids['Glasgow1'])
    createJob(cursor, driver_ids['driver1'], client_ids['private3'], 14.0, 70.0, '2023-08-10', '2023-08-10', address_ids['Glasgow1'])
    createJob(cursor, driver_ids['driver1'], client_ids['private3'], 16.0, 80.0, '2023-08-15', '2023-08-15', address_ids['Glasgow1'])
    
    createJob(cursor, driver_ids['driver2'], client_ids['private4'], 11.0, 55.0, '2023-08-02', '2023-08-02', address_ids['Manchester1'])
    createJob(cursor, driver_ids['driver2'], client_ids['private4'], 13.0, 65.0, '2023-08-06', '2023-08-06', address_ids['Manchester1'])
    createJob(cursor, driver_ids['driver2'], client_ids['private4'], 15.0, 75.0, '2023-08-11', '2023-08-11', address_ids['Manchester1'])
    createJob(cursor, driver_ids['driver2'], client_ids['private4'], 17.0, 85.0, '2023-08-16', '2023-08-16', address_ids['Manchester1'])

    
    
    

    
    
    createJob(cursor, driver_ids['driver3'], client_ids['private5'], 18.0, 90.0, '2023-09-01', '2023-09-01', address_ids['Liverpool1'])
    createJob(cursor, driver_ids['driver4'], client_ids['private1'], 20.0, 100.0, '2023-09-02', '2023-09-02', address_ids['Manchester1'])
    createJob(cursor, driver_ids['driver5'], client_ids['private2'], 22.0, 110.0, '2023-09-03', '2023-09-03', address_ids['London1'])
    createJob(cursor, driver_ids['driver5'], client_ids['private3'], 24.0, 120.0, '2023-09-04', '2023-09-04', address_ids['London1'])
    createJob(cursor, driver_ids['driver5'], client_ids['private4'], 26.0, 130.0, '2023-09-05', '2023-09-05', address_ids['London1'])

    
    

    
    createJob(cursor, driver_ids['driver1'], client_ids['business1'], 30.0, 150.0, '2023-09-01', '2023-09-01', address_ids['Glasgow1'], contract_id=contract_ids['contract1'])
    createJob(cursor, driver_ids['driver2'], client_ids['business1'], 25.0, 125.0, '2023-09-05', '2023-09-05', address_ids['Glasgow1'], contract_id=contract_ids['contract1'])
    createJob(cursor, driver_ids['driver3'], client_ids['business1'], 35.0, 175.0, '2023-09-10', '2023-09-10', address_ids['Glasgow1'], contract_id=contract_ids['contract1'])



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    createTables(cursor)
    

    populate_data(cursor)

    query1(cursor)
    query2(cursor)
    query3(cursor)
    query4(cursor)
    query5(cursor)
    query6(cursor)
    query7(cursor)
    query8(cursor)
    query9(cursor)
    query10(cursor)
    query11(cursor)
    query12(cursor)
    query13(cursor)
    query14(cursor)
    query15(cursor)
    query16(cursor)
    query17(cursor)
    query18(cursor)
    query19(cursor)
    



if __name__ == "__main__":
    args = sys.argv[1:]
    
    with closing(sqlite3.connect('database2.db')) as connection:
        connection.row_factory = sqlite3.Row

        with closing(connection.cursor()) as cursor:
            logging.info("Database connection established")
            logging.info(f'Total changes: {connection.total_changes}')
            logging.info(f'Isolation level: {connection.isolation_level}')
            logging.info(f'Row factory: {connection.row_factory}')
            logging.info(f'Cursor description: {cursor.description}')
            total_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            logging.info(f'Total: {len(total_tables)}')
            

            if args:
                if args[0] == '--exec':
                    print_table(cursor.execute(args[1]).fetchall(), column_names=[desc[0] for desc in cursor.description])
                else:
                    logging.error("Invalid argument")
            else:
                main(connection, cursor)

            connection.commit()

            
            os.remove('database2.db')

            
            



