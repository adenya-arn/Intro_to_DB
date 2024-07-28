import mysql.connector
from mysql.connector import errorcode


# Database name
db_name = 'alx_book_store'

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{db_name}' already exists.")
        else:
            print(f"Failed creating database: {err}")
    else:
        print(f"Database '{db_name}' created successfully!")

