class ValidationException(Exception):
    pass

class NegativeBalanceError(ValidationException):
    def __init__(self):
        super().__init__("El saldo de la cuenta no puede ser negativo")

class NegativeAmountError(ValidationException):
    def __init__(self):
        super().__init__("La cantidad de dinero debe ser positiva")

class InsufficientBalanceError(ValidationException):
    def __init__(self):
        super().__init__("No tienes saldo suficiente")

class AccountNotFoundError(ValidationException):
    def __init__(self):
        super().__init__("La cuenta corriente que buscas, no se pudo encontrar")
        
class AccountInactiveError(ValidationException):
    def __init__(self, *args):
        super().__init__("La cuenta se encuentra inactiva en este momento")

class AccountSourceInactiveError(ValidationException):
    def __init__(self, *args):
        super().__init__("La cuenta origen se encuentra inactiva en este momento")

class AccountTargetInactiveError(ValidationException):
    def __init__(self, *args):
        super().__init__("La cuenta destino se encuentra inactiva en este momento")