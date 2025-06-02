class ValidationError(Exception):
    """Clase base para excepciones de validación"""
    pass

class DNIValidationError(ValidationError):
    """Excepción para errores de validación de DNI"""
    def __init__(self, message="DNI no válido"):
        self.message = message
        super().__init__(self.message)

class PhoneValidationError(ValidationError):
    """Excepción para errores de validación de teléfono"""
    def __init__(self, message="Número de teléfono no válido"):
        self.message = message
        super().__init__(self.message)

class EmptyFieldError(ValidationError):
    """Excepción para campos vacíos"""
    def __init__(self, field_name):
        self.message = f"El campo {field_name} no puede estar vacío"
        super().__init__(self.message)

class InvalidAmountError(ValidationError):
    """Excepción para cantidades monetarias inválidas"""
    def __init__(self, message="La cantidad debe ser un número positivo"):
        self.message = message
        super().__init__(self.message)

class InvalidDateError(ValidationError):
    """Excepción para fechas inválidas"""
    def __init__(self, message="Fecha no válida"):
        self.message = message
        super().__init__(self.message)
