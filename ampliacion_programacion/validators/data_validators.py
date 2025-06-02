import re
from datetime import datetime
from exceptions.validation_exceptions import (
    DNIValidationError,
    PhoneValidationError,
    EmptyFieldError,
    InvalidAmountError,
    InvalidDateError
)

class DataValidator:
    @staticmethod
    def validate_dni(dni: str) -> str:
        """
        valida un DNI español.
        - Debe tener 9 caracteres
        - 8 números seguidos de una letra
        - La letra debe ser correcta según el algoritmo del DNI
        """
        if not dni:
            raise EmptyFieldError("DNI")

        # Limpiamos el DNI de espacios y lo ponemos en mayúsculas
        dni = dni.strip().upper()
        
        # Patrón del DNI: 8 números y una letra
        patron_dni = re.compile(r'^[0-9]{8}[A-Z]$')
        if not patron_dni.match(dni):
            raise DNIValidationError("El formato del DNI debe ser 8 números seguidos de una letra")

        # Letras válidas del DNI
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        
        numero = dni[:-1]
        letra = dni[-1]
        
        if not numero.isdigit():
            raise DNIValidationError("Los primeros 8 caracteres del DNI deben ser números")
            
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if letra != letras[int(numero) % 23]:
            raise DNIValidationError("La letra del DNI no es válida")
    
    @staticmethod
    def validate_phone(phone: str) -> None:
        if not phone:
            raise EmptyFieldError("Teléfono")
            
        if not phone.isdigit():
            raise PhoneValidationError("El teléfono debe contener solo números")
            
        if len(phone) != 9:
            raise PhoneValidationError("El teléfono debe tener 9 dígitos")
            
        if not phone.startswith(("6", "7", "9")):
            raise PhoneValidationError("El teléfono debe empezar por 6, 7 o 9")
    
    @staticmethod
    def validate_amount(amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("El importe debe ser mayor que 0")
            
        # Convertir a Decimal para manejar decimales con precisión
        try:
            amount_decimal = Decimal(str(amount))
            if amount_decimal.as_tuple().exponent < -2:
                raise InvalidAmountError("El importe no puede tener más de 2 decimales")
        except:
            raise InvalidAmountError("Importe inválido")
    
    @staticmethod
    def validate_required_field(value: str, field_name: str) -> None:
        if not value or str(value).strip() == "":
            raise EmptyFieldError(field_name)
    
    @staticmethod
    def validate_account_number(account: str) -> None:
        if not account:
            raise EmptyFieldError("Número de cuenta")
            
        if not str(account).isdigit():
            raise InvalidAmountError("El número de cuenta debe contener solo números")
            
        if int(account) <= 0:
            raise InvalidAmountError("El número de cuenta debe ser positivo")

    @staticmethod
    def validate_date(date_str: str, format: str = "%d/%m/%Y") -> datetime:
        """
        Valida una fecha en el formato especificado.
        Por defecto usa el formato dd/mm/yyyy
        """
        if not date_str:
            raise EmptyFieldError("Fecha")

        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            raise InvalidDateError(f"La fecha debe estar en formato {format}")
        if not value or not value.strip():
            raise EmptyFieldError(field_name)
        return value.strip()

    @staticmethod
    def validate_account_number(account_number: str) -> str:
        """
        Valida un número de cuenta.
        Por ahora solo validamos que sea un número positivo,
        pero aquí se podría implementar la validación de IBAN si se necesita
        """
        try:
            num = int(account_number)
            if num <= 0:
                raise ValueError
            return account_number
        except ValueError:
            raise InvalidAmountError("El número de cuenta debe ser un número positivo")
