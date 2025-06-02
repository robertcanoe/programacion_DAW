import os
from typing import Optional
from dotenv import load_dotenv
from mysql.connector import connect, Error

class DatabaseConnection:
    _instance = None
    connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        load_dotenv()
        try:
            self.connection = connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
            self.connection.autocommit = True
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def get_cursor(self):
        try:
            if not self.connection or not self.connection.is_connected():
                self._connect()
            return self.connection.cursor()
        except Error as e:
            print(f"Error al obtener el cursor: {e}")
            raise

    def commit(self):
        if self.connection:
            self.connection.commit()

    def rollback(self):
        if self.connection:
            self.connection.rollback()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
