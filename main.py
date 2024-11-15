import sqlite3
from contextlib import closing
from createTables import createTables
from pprint import pprint

def main(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    createTables(cursor)



with closing(sqlite3.connect('database.db')) as connection:
    with closing(connection.cursor()) as cursor:
        print("Database connection established")
        print(f'Total changes: {connection.total_changes}')
        print(f'Isolation level: {connection.isolation_level}')
        print(f'Row factory: {connection.row_factory}')
        print(f'Cursor description: {cursor.description}')
        total_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        print(f'Tables: {total_tables}')


        main(connection, cursor)



