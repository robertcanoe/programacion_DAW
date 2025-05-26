from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    id: int = None
    nombre: str = ""
    email: str = ""
    fecha_registro: datetime = None
    activo: bool = True
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None,
            'activo': self.activo
        }
