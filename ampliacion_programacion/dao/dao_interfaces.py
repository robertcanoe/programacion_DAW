from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from models.models import Cliente, Cuenta, Movimiento

class ClienteDAO(ABC):
    @abstractmethod
    def crear(self, cliente: Cliente) -> bool:
        pass

    @abstractmethod
    def modificar(self, cliente: Cliente) -> bool:
        pass

    @abstractmethod
    def eliminar(self, dni: str) -> bool:
        pass

    @abstractmethod
    def obtener_por_dni(self, dni: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    def tiene_cuentas(self, dni: str) -> bool:
        pass

class CuentaDAO(ABC):
    @abstractmethod
    def crear(self, cuenta: Cuenta) -> int:
        pass

    @abstractmethod
    def modificar_estado(self, numero: int, activa: bool) -> bool:
        pass

    @abstractmethod
    def obtener_por_numero(self, numero: int) -> Optional[Cuenta]:
        pass

    @abstractmethod
    def obtener_por_cliente(self, dni: str) -> List[Cuenta]:
        pass

class MovimientoDAO(ABC):
    @abstractmethod
    def crear(self, movimiento: Movimiento) -> bool:
        pass

    @abstractmethod
    def obtener_por_cuenta(self, numero_cuenta: int) -> List[Movimiento]:
        pass

    @abstractmethod
    def obtener_por_cuenta_y_fechas(self, numero_cuenta: int, fecha_inicio: datetime, fecha_fin: datetime) -> List[Movimiento]:
        pass

    @abstractmethod
    def obtener_saldo(self, numero_cuenta: int) -> float:
        pass
