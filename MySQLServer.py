import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost:3306', 
            user='root',  
            password='simo@51344/c'
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensure the connection is closed
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()