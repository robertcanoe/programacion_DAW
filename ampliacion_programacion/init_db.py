import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def create_database():
    try:
        # Conectar al servidor MySQL sin seleccionar una base de datos
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        cursor = connection.cursor()
        
        # Crear la base de datos
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
        
        # Seleccionar la base de datos
        cursor.execute(f"USE {os.getenv('DB_NAME')}")
        
        # Crear tabla clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                dni VARCHAR(9) PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                telefono VARCHAR(15) NOT NULL,
                direccion VARCHAR(200) NOT NULL
            )
        """)
        
        # Crear tabla cuentas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cuentas (
                numero INT AUTO_INCREMENT PRIMARY KEY,
                dni_cliente VARCHAR(9) NOT NULL,
                activa BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (dni_cliente) REFERENCES clientes(dni)
            )
        """)
        
        # Crear tabla movimientos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimientos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                numero_cuenta INT NOT NULL,
                importe DECIMAL(10,2) NOT NULL,
                fecha_hora DATETIME NOT NULL,
                tipo ENUM('ingreso', 'salida', 'transferencia_enviada', 'transferencia_recibida') NOT NULL,
                numero_cuenta_transferencia INT,
                concepto VARCHAR(200) NOT NULL,
                FOREIGN KEY (numero_cuenta) REFERENCES cuentas(numero),
                FOREIGN KEY (numero_cuenta_transferencia) REFERENCES cuentas(numero)
            )
        """)
        
        connection.commit()
        print("Base de datos y tablas creadas correctamente")
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
