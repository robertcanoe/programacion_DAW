from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

@dataclass
class Cliente:
    dni: str
    nombre: str
    telefono: str
    direccion: str

@dataclass
class Cuenta:
    numero: int
    dni_cliente: str
    activa: bool = True
    saldo: Decimal = Decimal('0.00')

@dataclass
class Movimiento:
    id: Optional[int]
    cuenta_numero: int
    fecha: datetime
    concepto: str
    importe: Decimal
    cuenta_transferencia: Optional[int]
