import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),
                    database=os.getenv('DB_NAME')
                )
            except Error as e:
                print(f"Error connecting to MySQL Database: {e}")
                raise
        return self.connection

    def get_cursor(self):
        return self.connect().cursor(dictionary=True)

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
