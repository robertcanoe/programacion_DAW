from __future__ import annotations
from clients.client_dao import ClientDAO
from clients.client import Client
from mysql.connector import Error
from typeguard import typechecked
from db.db_config import connect, create_database_if_not_exists

@typechecked
class MySQLClientDAO(ClientDAO):
    def is_customer_active(self, dni: str) -> bool:
        query = "SELECT activo FROM customer WHERE dni = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (dni,))
            result = cursor.fetchone()
            if result is None:
                raise Exception("Cliente no encontrado")
            return bool(result[0])
        finally:
            cursor.close()


    def __init__(self):
        create_database_if_not_exists()
        self.connection = connect()
        self._create_table()

    def _execute_query(self, query: str, parameters: tuple = ()):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            self.connection.commit()
        except Error as e:
            raise
        finally:
            if cursor:
                cursor.close()

    def _create_table(self):
        create_table_customer = """
        CREATE TABLE IF NOT EXISTS customer(
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        telefono VARCHAR(20),
        direccion VARCHAR(150),
        activo BOOL
        )
        """
        self._execute_query(create_table_customer)

    def add_client(self, client: Client):
        insert_client = """
        INSERT INTO customer (dni, nombre, apellido, telefono, direccion, activo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self._execute_query(insert_client, (client._dni, client.name, client.lastname, client.phone, 
                                         client.address, client.active))

    def update_client(self, name: str, lastname: str, phone: str, address: str, dni: str):
        update_customers = """
        UPDATE customer SET nombre = %s, apellido = %s, telefono = %s, direccion = %s
        WHERE dni = %s
        """
        self._execute_query(update_customers, (name, lastname, phone, 
                                         address, dni))

    def get_client(self, dni: str):
        select_client = "SELECT * FROM customer WHERE dni = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(select_client, (dni,))
            result = cursor.fetchone()  
            if result:
                return Client(result[0], result[1], result[2], result[3], result[4], bool(result[5]))
            return None
        finally:
            cursor.close()

    def release(self, dni: str):
        release_customer = """
        UPDATE customer SET activo = True WHERE dni = %s
        """
        self._execute_query(release_customer, (dni,))

    def deregister(self, dni: str):
        deregister_customer = """
        UPDATE customer SET activo = False WHERE dni = %s
        """
        self._execute_query(deregister_customer, (dni,))

    def is_client_active(self, dni: str):
        client_query = "SELECT activo FROM customer WHERE dni = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(client_query, (dni,))
            result = cursor.fetchone()
            if result is None:
                raise Exception(f"No se encontró cliente con DNI {dni}")
            return bool(result[0])
        except Exception as e:
            print(f"Error al verificar estado del cliente: {e}")
            raise
        finally:
            cursor.close()

    def close_connection(self):
           if self.connection and self.connection.is_connected():
               self.connection.close()