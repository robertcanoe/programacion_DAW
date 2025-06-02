from datetime import datetime
from typing import List, Optional, Tuple
from decimal import Decimal

from models.models import Cliente, Cuenta, Movimiento
from dao.dao_impl import ClienteDAOImpl, CuentaDAOImpl, MovimientoDAOImpl
from validators.data_validators import DataValidator
from exceptions.validation_exceptions import ValidationError

class BancoService:
    def __init__(self):
        self.cliente_dao = ClienteDAOImpl()
        self.cuenta_dao = CuentaDAOImpl()
        self.movimiento_dao = MovimientoDAOImpl()

    # Servicios de Cliente
    def crear_cliente(self, dni: str, nombre: str, telefono: str, direccion: str) -> bool:
        try:
            # Validamos todos los campos
            dni_validado = DataValidator.validate_dni(dni)
            nombre_validado = DataValidator.validate_required_field(nombre, "Nombre")
            telefono_validado = DataValidator.validate_phone(telefono)
            direccion_validada = DataValidator.validate_required_field(direccion, "Dirección")
            
            cliente = Cliente(
                dni=dni_validado,
                nombre=nombre_validado,
                telefono=telefono_validado,
                direccion=direccion_validada
            )
            return self.cliente_dao.crear(cliente)
        except ValidationError as e:
            print(f"Error de validación: {e}")
            return False

    def modificar_cliente(self, dni: str, nombre: str, telefono: str, direccion: str) -> bool:
        try:
            # Validamos todos los campos
            dni_validado = DataValidator.validate_dni(dni)
            nombre_validado = DataValidator.validate_required_field(nombre, "Nombre")
            telefono_validado = DataValidator.validate_phone(telefono)
            direccion_validada = DataValidator.validate_required_field(direccion, "Dirección")
            
            cliente = Cliente(
                dni=dni_validado,
                nombre=nombre_validado,
                telefono=telefono_validado,
                direccion=direccion_validada
            )
            return self.cliente_dao.modificar(cliente)
        except ValidationError as e:
            print(f"Error de validación: {e}")
            return False

    def eliminar_cliente(self, dni: str) -> Tuple[bool, str]:
        if self.cliente_dao.tiene_cuentas(dni):
            return False, "No se puede eliminar el cliente porque tiene cuentas activas"
        return self.cliente_dao.eliminar(dni), "Cliente eliminado correctamente"

    def obtener_cliente(self, dni: str) -> Optional[Cliente]:
        return self.cliente_dao.obtener_por_dni(dni)

    # Servicios de Cuenta
    def crear_cuenta(self, dni_cliente: str) -> Tuple[bool, str, Optional[int]]:
        if not self.cliente_dao.obtener_por_dni(dni_cliente):
            return False, "Cliente no encontrado", None
        
        cuenta = Cuenta(numero=None, dni_cliente=dni_cliente)
        numero_cuenta = self.cuenta_dao.crear(cuenta)
        if numero_cuenta:
            return True, "Cuenta creada correctamente", numero_cuenta
        return False, "Error al crear la cuenta", None

    def dar_baja_cuenta(self, numero_cuenta: int) -> Tuple[bool, str]:
        cuenta = self.cuenta_dao.obtener_por_numero(numero_cuenta)
        if not cuenta:
            return False, "Cuenta no encontrada"
        if not cuenta.activa:
            return False, "La cuenta ya está dada de baja"
        
        if self.cuenta_dao.modificar_estado(numero_cuenta, False):
            return True, "Cuenta dada de baja correctamente"
        return False, "Error al dar de baja la cuenta"

    def realizar_ingreso(self, numero_cuenta: int, importe: float, concepto: str) -> Tuple[bool, str]:
        try:
            importe_validado = DataValidator.validate_amount(importe)
            concepto_validado = DataValidator.validate_required_field(concepto, "Concepto")
            DataValidator.validate_account_number(str(numero_cuenta))
            
            cuenta = self.cuenta_dao.obtener_por_numero(numero_cuenta)
            if not cuenta:
                return False, "Cuenta no encontrada"
            if not cuenta.activa:
                return False, "La cuenta está dada de baja"

            movimiento = Movimiento(
                numero_cuenta=numero_cuenta,
                importe=importe_validado,
                fecha_hora=datetime.now(),
                tipo="ingreso",
                numero_cuenta_transferencia=None,
                concepto=concepto_validado
            )
            
            if self.movimiento_dao.crear(movimiento):
                return True, "Ingreso realizado correctamente"
            return False, "Error al realizar el ingreso"
        except ValidationError as e:
            return False, str(e)

    def realizar_salida(self, numero_cuenta: int, importe: float, concepto: str) -> Tuple[bool, str]:
        try:
            importe_validado = DataValidator.validate_amount(importe)
            concepto_validado = DataValidator.validate_required_field(concepto, "Concepto")
            DataValidator.validate_account_number(str(numero_cuenta))
            
            cuenta = self.cuenta_dao.obtener_por_numero(numero_cuenta)
            if not cuenta:
                return False, "Cuenta no encontrada"
            if not cuenta.activa:
                return False, "La cuenta está dada de baja"

            saldo = self.movimiento_dao.obtener_saldo(numero_cuenta)
            if saldo < importe_validado:
                return False, "Saldo insuficiente"

            movimiento = Movimiento(
                numero_cuenta=numero_cuenta,
                importe=importe_validado,
                fecha_hora=datetime.now(),
                tipo="salida",
                numero_cuenta_transferencia=None,
                concepto=concepto_validado
            )
            
            if self.movimiento_dao.crear(movimiento):
                return True, "Salida realizada correctamente"
            return False, "Error al realizar la salida"
        except ValidationError as e:
            return False, str(e)

    def realizar_transferencia(self, cuenta_origen: int, cuenta_destino: int, importe: float, concepto: str) -> Tuple[bool, str]:
        try:
            importe_validado = DataValidator.validate_amount(importe)
            concepto_validado = DataValidator.validate_required_field(concepto, "Concepto")
            DataValidator.validate_account_number(str(cuenta_origen))
            DataValidator.validate_account_number(str(cuenta_destino))
            
            cuenta_orig = self.cuenta_dao.obtener_por_numero(cuenta_origen)
            cuenta_dest = self.cuenta_dao.obtener_por_numero(cuenta_destino)

            if not cuenta_orig or not cuenta_dest:
                return False, "Alguna de las cuentas no existe"
            if not cuenta_orig.activa or not cuenta_dest.activa:
                return False, "Alguna de las cuentas está dada de baja"

            saldo = self.movimiento_dao.obtener_saldo(cuenta_origen)
            if saldo < importe_validado:
                return False, "Saldo insuficiente en la cuenta de origen"

            # Crear movimiento de salida
            mov_salida = Movimiento(
                numero_cuenta=cuenta_origen,
                importe=importe_validado,
                fecha_hora=datetime.now(),
                tipo="transferencia_enviada",
                numero_cuenta_transferencia=cuenta_destino,
                concepto=concepto_validado
            )

            # Crear movimiento de entrada
            mov_entrada = Movimiento(
                numero_cuenta=cuenta_destino,
                importe=importe_validado,
                fecha_hora=datetime.now(),
                tipo="transferencia_recibida",
                numero_cuenta_transferencia=cuenta_origen,
                concepto=concepto_validado
            )

            if self.movimiento_dao.crear(mov_salida) and self.movimiento_dao.crear(mov_entrada):
                return True, "Transferencia realizada correctamente"
            return False, "Error al realizar la transferencia"
        except ValidationError as e:
            return False, str(e)

    def obtener_movimientos(self, numero_cuenta: int, fecha_inicio: Optional[datetime] = None, fecha_fin: Optional[datetime] = None) -> List[Movimiento]:
        if fecha_inicio and fecha_fin:
            return self.movimiento_dao.obtener_por_cuenta_y_fechas(numero_cuenta, fecha_inicio, fecha_fin)
        return self.movimiento_dao.obtener_por_cuenta(numero_cuenta)

    def obtener_saldo(self, numero_cuenta: int) -> float:
        return self.movimiento_dao.obtener_saldo(numero_cuenta)

    def obtener_cuentas(self) -> List[Cuenta]:
        """Obtiene todas las cuentas registradas"""
        return self.cuenta_dao.get_all()
