import mysql.connector
from mysql.connector import Error


# Name of the database to be created
db_name = 'alx_book_store'

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created successfully or already exists!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Run the function to create the database
create_database()

