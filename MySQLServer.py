import mysql.connector
from mysql.connector import Error

# Database name
db_name = 'alx_book_store'

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
    print(f"Database '{db_name}' created successfully or already exists.")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()

