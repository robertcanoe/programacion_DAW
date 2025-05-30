from typing import List, Optional
from datetime import datetime
from config.db_config import DatabaseConnection
from models.models import Cliente, Cuenta, Movimiento
from dao.dao_interfaces import ClienteDAO, CuentaDAO, MovimientoDAO

class ClienteDAOImpl(ClienteDAO):
    def __init__(self):
        self.db = DatabaseConnection()

    def crear(self, cliente: Cliente) -> bool:
        try:
            cursor = self.db.get_cursor()
            sql = "INSERT INTO clientes (dni, nombre, telefono, direccion) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cliente.dni, cliente.nombre, cliente.telefono, cliente.direccion))
            self.db.connect().commit()
            return True
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            return False

    def modificar(self, cliente: Cliente) -> bool:
        try:
            cursor = self.db.get_cursor()
            sql = "UPDATE clientes SET nombre = %s, telefono = %s, direccion = %s WHERE dni = %s"
            cursor.execute(sql, (cliente.nombre, cliente.telefono, cliente.direccion, cliente.dni))
            self.db.connect().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al modificar cliente: {e}")
            return False

    def eliminar(self, dni: str) -> bool:
        if self.tiene_cuentas(dni):
            return False
        try:
            cursor = self.db.get_cursor()
            sql = "DELETE FROM clientes WHERE dni = %s"
            cursor.execute(sql, (dni,))
            self.db.connect().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False

    def obtener_por_dni(self, dni: str) -> Optional[Cliente]:
        try:
            cursor = self.db.get_cursor()
            sql = "SELECT * FROM clientes WHERE dni = %s"
            cursor.execute(sql, (dni,))
            result = cursor.fetchone()
            if result:
                return Cliente(**result)
            return None
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
            return None

    def tiene_cuentas(self, dni: str) -> bool:
        try:
            cursor = self.db.get_cursor()
            sql = "SELECT COUNT(*) as count FROM cuentas WHERE dni_cliente = %s"
            cursor.execute(sql, (dni,))
            result = cursor.fetchone()
            return result['count'] > 0
        except Exception as e:
            print(f"Error al verificar cuentas del cliente: {e}")
            return False

class CuentaDAOImpl(CuentaDAO):
    def __init__(self):
        self.db = DatabaseConnection()

    def crear(self, cuenta: Cuenta) -> int:
        try:
            cursor = self.db.get_cursor()
            sql = "INSERT INTO cuentas (dni_cliente, activa) VALUES (%s, %s)"
            cursor.execute(sql, (cuenta.dni_cliente, cuenta.activa))
            self.db.connect().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear cuenta: {e}")
            return 0

    def modificar_estado(self, numero: int, activa: bool) -> bool:
        try:
            cursor = self.db.get_cursor()
            sql = "UPDATE cuentas SET activa = %s WHERE numero = %s"
            cursor.execute(sql, (activa, numero))
            self.db.connect().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al modificar estado de cuenta: {e}")
            return False

    def obtener_por_numero(self, numero: int) -> Optional[Cuenta]:
        try:
            cursor = self.db.get_cursor()
            sql = "SELECT * FROM cuentas WHERE numero = %s"
            cursor.execute(sql, (numero,))
            result = cursor.fetchone()
            if result:
                return Cuenta(**result)
            return None
        except Exception as e:
            print(f"Error al obtener cuenta: {e}")
            return None

    def obtener_por_cliente(self, dni: str) -> List[Cuenta]:
        try:
            cursor = self.db.get_cursor()
            sql = "SELECT * FROM cuentas WHERE dni_cliente = %s"
            cursor.execute(sql, (dni,))
            return [Cuenta(**row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener cuentas del cliente: {e}")
            return []

class MovimientoDAOImpl(MovimientoDAO):
    def __init__(self):
        self.db = DatabaseConnection()

    def crear(self, movimiento: Movimiento) -> bool:
        try:
            cursor = self.db.get_cursor()
            sql = """INSERT INTO movimientos 
                    (numero_cuenta, importe, fecha_hora, tipo, numero_cuenta_transferencia, concepto)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                movimiento.numero_cuenta,
                movimiento.importe,
                movimiento.fecha_hora,
                movimiento.tipo,
                movimiento.numero_cuenta_transferencia,
                movimiento.concepto
            ))
            self.db.connect().commit()
            return True
        except Exception as e:
            print(f"Error al crear movimiento: {e}")
            return False

    def obtener_por_cuenta(self, numero_cuenta: int) -> List[Movimiento]:
        try:
            cursor = self.db.get_cursor()
            sql = "SELECT * FROM movimientos WHERE numero_cuenta = %s ORDER BY fecha_hora DESC"
            cursor.execute(sql, (numero_cuenta,))
            return [Movimiento(**row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener movimientos: {e}")
            return []

    def obtener_por_cuenta_y_fechas(self, numero_cuenta: int, fecha_inicio: datetime, fecha_fin: datetime) -> List[Movimiento]:
        try:
            cursor = self.db.get_cursor()
            sql = """SELECT * FROM movimientos 
                    WHERE numero_cuenta = %s 
                    AND fecha_hora BETWEEN %s AND %s 
                    ORDER BY fecha_hora DESC"""
            cursor.execute(sql, (numero_cuenta, fecha_inicio, fecha_fin))
            return [Movimiento(**row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener movimientos por fecha: {e}")
            return []

    def obtener_saldo(self, numero_cuenta: int) -> float:
        try:
            cursor = self.db.get_cursor()
            sql = """SELECT COALESCE(SUM(
                    CASE 
                        WHEN tipo IN ('ingreso', 'transferencia_recibida') THEN importe
                        WHEN tipo IN ('salida', 'transferencia_enviada') THEN -importe
                    END), 0) as saldo
                    FROM movimientos 
                    WHERE numero_cuenta = %s"""
            cursor.execute(sql, (numero_cuenta,))
            result = cursor.fetchone()
            return float(result['saldo'])
        except Exception as e:
            print(f"Error al obtener saldo: {e}")
            return 0.0
