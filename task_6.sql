import mysql.connector
from mysql.connector import Error


# Name of the database to be created
db_name = 'alx_book_store'

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
"""    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database '{db_name}' created successfully or already exists.")
    
except Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
