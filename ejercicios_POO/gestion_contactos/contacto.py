import csv
import os
import re
from typeguard import typechecked

@typechecked
class Contacto:
    def __init__(self, nombre: str, telefono: str, email: str):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data.get('Nombre', '').strip(),
            telefono=data.get('Teléfono', '').strip(),
            email=data.get('Correo electrónico', '').strip()
        )
    
    def to_dict(self):
        return {
            'Nombre': self.nombre,
            'Teléfono': self.telefono,
            'Correo electrónico': self.email
        }
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value.strip()
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @telefono.setter
    def telefono(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("El teléfono no puede estar vacío")
        if not re.match(r'^\d{9}$', value):
            raise ValueError("El teléfono debe tener exactamente 9 dígitos")
        self._telefono = value
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("El correo electrónico no puede estar vacío")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValueError("El correo electrónico no tiene un formato válido")
        self._email = value

@typechecked
class GestorContactos:
    ARCHIVO = 'contactos.csv'
    CAMPOS = ['Nombre', 'Teléfono', 'Correo electrónico']
    
    def __init__(self):
        self.contactos = []
        self.cargar_contactos()
    
    def cargar_contactos(self):
        """Carga los contactos desde el archivo CSV si existe."""
        self.contactos.clear()
        if not os.path.exists(self.ARCHIVO):
            return
            
        try:
            with open(self.ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        self.contactos.append(Contacto.from_dict(fila))
                    except ValueError as e:
                        print(f"Error en el formato del contacto: {e}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    
    def guardar_contactos(self):
        """Guarda los contactos en el archivo CSV."""
        try:
            with open(self.ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
                escritor.writeheader()
                for contacto in self.contactos:
                    escritor.writerow(contacto.to_dict())
        except Exception as e:
            print(f"Error al guardar los contactos: {e}")
    
    def crear_archivo(self):
        """Crea el archivo CSV si no existe."""
        if os.path.exists(self.ARCHIVO):
            print("\n    El archivo ya existe.")
            input("\n    Presione Enter para continuar...")
            return
        
        try:
            with open(self.ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
                escritor.writeheader()
            print("\n    " + "=" * 30)
            print(f"    Archivo {self.ARCHIVO} creado correctamente.")
            print("    " + "=" * 30)
        except Exception as e:
            print(f"\n    Error al crear el archivo: {e}")
        
        input("\n    Presione Enter para continuar...")
