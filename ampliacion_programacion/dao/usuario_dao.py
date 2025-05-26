import mysql.connector
from mysql.connector import Error
from datetime import datetime
from models.usuario import Usuario
from database.config import db_config

class UsuarioDAO:
    def __init__(self):
        self.connection = None
        self._create_database_if_not_exists()
        self.connect()
        self._create_table()

    def connect(self):
        """Establece la conexión a la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=db_config.host,
                user=db_config.user,
                password=db_config.password,
                database=db_config.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def _create_database_if_not_exists(self):
        """Crea la base de datos si no existe"""
        try:
            # Primero nos conectamos sin especificar la base de datos
            temp_conn = mysql.connector.connect(
                host=db_config.host,
                user=db_config.user,
                password=db_config.password
            )
            cursor = temp_conn.cursor()
            
            # Creamos la base de datos si no existe
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config.database}")
            temp_conn.commit()
            cursor.close()
            temp_conn.close()
            print(f"Base de datos '{db_config.database}' verificada/creada correctamente")
        except Error as e:
            print(f"Error al crear la base de datos: {e}")
    
    def _create_table(self):
        """Crea la tabla de usuarios si no existe"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
            activo BOOLEAN DEFAULT TRUE
        )
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def create(self, usuario):
        """Crea un nuevo usuario en la base de datos"""
        query = """
        INSERT INTO usuarios (nombre, email, activo)
        VALUES (%s, %s, %s)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario.nombre, usuario.email, usuario.activo))
            self.connection.commit()
            usuario.id = cursor.lastrowid
            return usuario
        except Error as e:
            print(f"Error al crear usuario: {e}")
            return None

    def get_all(self):
        """Obtiene todos los usuarios de la base de datos"""
        query = "SELECT id, nombre, email, fecha_registro, activo FROM usuarios"
        usuarios = []
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor.fetchall():
                usuario = Usuario(
                    id=row['id'],
                    nombre=row['nombre'],
                    email=row['email'],
                    fecha_registro=row['fecha_registro'],
                    activo=bool(row['activo'])
                )
                usuarios.append(usuario)
            return usuarios
        except Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def get_by_id(self, usuario_id):
        """Obtiene un usuario por su ID"""
        query = "SELECT id, nombre, email, fecha_registro, activo FROM usuarios WHERE id = %s"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (usuario_id,))
            row = cursor.fetchone()
            if row:
                return Usuario(
                    id=row['id'],
                    nombre=row['nombre'],
                    email=row['email'],
                    fecha_registro=row['fecha_registro'],
                    activo=bool(row['activo'])
                )
            return None
        except Error as e:
            print(f"Error al obtener usuario: {e}")
            return None

    def update(self, usuario):
        """Actualiza un usuario existente"""
        query = """
        UPDATE usuarios
        SET nombre = %s, email = %s, activo = %s
        WHERE id = %s
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario.nombre, usuario.email, usuario.activo, usuario.id))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    def delete(self, usuario_id):
        """Elimina un usuario por su ID"""
        query = "DELETE FROM usuarios WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")
