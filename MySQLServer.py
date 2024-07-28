import mysql.connector
from mysql.connector import errorcode

# Database name
db_name = 'alx_book_store'

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    else:
        print(f"Database '{db_name}' created successfully or already exists!")

