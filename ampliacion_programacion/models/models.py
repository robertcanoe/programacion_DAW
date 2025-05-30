from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Cliente:
    dni: str
    nombre: str
    telefono: str
    direccion: str

@dataclass
class Cuenta:
    numero: Optional[int]
    dni_cliente: str
    activa: bool = True

@dataclass
class Movimiento:
    numero_cuenta: int
    importe: float
    fecha_hora: datetime
    tipo: str
    numero_cuenta_transferencia: Optional[int]
    concepto: str
    id: Optional[int] = None
