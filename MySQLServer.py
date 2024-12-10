import mysql.connector
from mysql.connector

from dotenv import load_dotenv
import os


load_dotenv()

def create_database():
    try:
        mysql_root_password = os.getenv('MY_SQL_ROOT_PASSWD')
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=mysql_root_password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully")
            
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    
    finally:
        
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
    