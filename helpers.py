import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_table(data, column_names=None):
    """
    Prints the given data (a list of tuples) as a formatted table.

    Args:
        data (list): A list of tuples containing the data.
        column_names (list): A list of column names (optional).
    """
    if not data:
        print("No data available.")
        return

    # Determine the number of columns
    num_columns = len(data[0])

    # If column names are not provided, generate generic names
    if column_names is None:
        column_names = [f"Column {i+1}" for i in range(num_columns)]

    # Calculate the maximum width for each column
    widths = [max(len(str(row[i])) for row in data) for i in range(num_columns)]
    widths = [max(width, len(column_names[i])) for i, width in enumerate(widths)]

    # Print the header row
    header = " | ".join(f"{column_names[i]:<{widths[i]}}" for i in range(num_columns))
    print(header)
    print("-" * (sum(widths) + (3 * (num_columns - 1))))

    # Print the data rows
    for row in data:
        print(" | ".join(f"{str(row[i]):<{widths[i]}}" for i in range(num_columns)))



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