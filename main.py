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



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    createTables(cursor)
    # createInitialData(cursor)

    # Query 1
    query19(cursor)


if __name__ == "__main__":
    args = sys.argv[1:]
    
    with closing(sqlite3.connect('database.db')) as connection:
        connection.row_factory = sqlite3.Row

        with closing(connection.cursor()) as cursor:
            logging.info("Database connection established")
            logging.info(f'Total changes: {connection.total_changes}')
            logging.info(f'Isolation level: {connection.isolation_level}')
            logging.info(f'Row factory: {connection.row_factory}')
            logging.info(f'Cursor description: {cursor.description}')
            total_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            logging.info(f'Total: {len(total_tables)}')
            # printRecordCounts(cursor)

            if args:
                if args[0] == '--exec':
                    print_table(cursor.execute(args[1]).fetchall(), column_names=[desc[0] for desc in cursor.description])
                else:
                    logging.error("Invalid argument")
            else:
                main(connection, cursor)

            connection.commit()

            # logging.info("\nAfter inserting records:")
            # printRecordCounts(cursor)



