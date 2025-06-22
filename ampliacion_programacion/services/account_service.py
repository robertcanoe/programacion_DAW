from errors.account_error import *
from errors.client_error import *
from accounts.account import Account
from transactions.transaction_repository import MySQLTransactionDAO
from transactions.transaction import Transaction

def create_current_account(mysql_account):
    dni = input("Añade el DNI del cliente al que quieras crear una cuenta: ")
    
    for intento in range(3):
        try:
            balance_input = input("Añade la cantidad de saldo que quieres en la cuenta (Pulsa ENTER si no quieres añadir nada o escribe 'salir' para cancelar): ")
            if balance_input.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            amount = float(balance_input) if balance_input else 0.0
            if amount < 0:
                raise NegativeAmountError()
            break
        except NegativeAmountError as e:
            print(f"{e}")
        except ValueError:
            print("Introduce un número válido.")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    try:
        current_account = Account(dni, amount)
        mysql_account.create_account(current_account)
    except NegativeAmountError as e:
        print(f"Error: {e}")

def open_current_account(mysql_account, mysql_customer):
    for intento in range(3):
        try:
            entrada = input("Escribe el número de la cuenta que quieras reabrir (o escribe 'salir' para cancelar): ")
            if entrada.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            number_account = int(entrada)
            dni = mysql_account.get_dni_by_account(number_account)
            if not dni:
                raise DNINotFoundError()
            if not mysql_customer.is_customer_active(dni):
                raise CustomerInactiveError()
            mysql_account.open_account(number_account)
            print("Cuenta reabierta correctamente.")
            break
        except DNINotFoundError as e:
            print(f"Error: {e}")
            return
        except CustomerInactiveError as e:
            print(f"Error: {e}")
            return
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

def close_current_account(mysql_account):
    for intento in range(3):
        try:
            entrada = input("Escribe el número de la cuenta que quieras cerrar (o escribe 'salir' para cancelar): ")
            if entrada.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            number_account = int(entrada)
            break
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return
    mysql_account.close_account(number_account)

def consult_balance(mysql_account):
    for intento in range(3):
        try:
            entrada = input("Escribe el número de la cuenta que quieras ver su saldo (o escribe 'salir' para cancelar): ")
            if entrada.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            number_account = int(entrada)
            break
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return
    balance = mysql_account.get_balance(number_account)
    print(f"El saldo de la cuenta {number_account:010} es: {balance} €\n")

def deposit_money(mysql_account):
    for intento in range(3):
        try:
            entrada = input("Escribe el número de la cuenta donde quieras depositar dinero (o escribe 'salir' para cancelar): ")
            if entrada.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            number_account = int(entrada)
            if not mysql_account.is_account_active(number_account):
                raise AccountInactiveError()
            balance = float(input("¿Qué cantidad quieres depositar? (o escribe 'salir' para cancelar): "))
            description = input("Escribe el concepto del deposito (Pulsa ENTER si no quieres añadir concepto): ")
            break
        except AccountInactiveError as e:
            print(f"Error: {e}")
            return
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    deposit = Transaction(number_account, balance, "ingreso", None, description)
    mysql_account.deposit(number_account, balance)
    movement = MySQLTransactionDAO()
    movement.create_movement(deposit)

def withdraw_money(mysql_account):
    for intento in range(3):
        try:
            entrada = input("Escribe el número de la cuenta donde quieras retirar dinero (o escribe 'salir' para cancelar): ")
            if entrada.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            number_account = int(entrada)
            if not mysql_account.is_account_active(number_account):
                raise AccountInactiveError()
            balance = float(input("¿Qué cantidad quieres retirar? (o escribe 'salir' para cancelar): "))
            description = input("Escribe el concepto de la salida (Pulsa ENTER si no quieres añadir concepto): ")
            break
        except AccountInactiveError as e:
            print(f"Error: {e}")
            return
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    withdraw = Transaction(number_account, balance, "salida", None, description)
    mysql_account.withdraw(number_account, balance)
    movement = MySQLTransactionDAO()
    movement.create_movement(withdraw)

def transfer_money(mysql_account):
    for intento in range(3):
        try:
            entrada_origen = input("Escribe el número de la cuenta que realizará la transferencia (o escribe 'salir' para cancelar): ")
            if entrada_origen.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            source_account = int(entrada_origen)
            entrada_destino = input("Escribe el número de la cuenta receptora (o escribe 'salir' para cancelar): ")
            if entrada_destino.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            target_account = int(entrada_destino)
            if not mysql_account.is_account_active(source_account):
                raise AccountSourceInactiveError()
            if not mysql_account.is_account_active(target_account):
                raise AccountTargetInactiveError()
            balance = float(input("¿Qué cantidad quieres transferir? (o escribe 'salir' para cancelar): "))
            description = input("Escribe el concepto de la transferencia (Pulsa ENTER si no quieres añadir concepto): ")
            break
        except AccountSourceInactiveError as e:
            print(f"Error: {e}")
            return
        except AccountTargetInactiveError as e:
            print(f"Error: {e}")
            return
        except ValueError:
            print("Introduce un número válido.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    source_transfer = Transaction(source_account, balance, "transferencia enviada", target_account, description)
    target_transfer = Transaction(target_account, balance, "transferencia recibida", source_account, description)
    mysql_account.transfer_to(source_account, target_account, balance)
    movement = MySQLTransactionDAO()
    movement.create_movement(source_transfer)
    movement.create_movement(target_transfer)

def show_all_accounts(mysql_account):
    cursor = mysql_account.connection.cursor()
    try:
        cursor.execute("""
            SELECT c.numero_cuenta, c.dni, cu.nombre, cu.apellido, c.saldo, c.activa 
            FROM current_account c
            JOIN customer cu ON c.dni = cu.dni
            ORDER BY c.numero_cuenta
        """)
        accounts = cursor.fetchall()
        
        print("\n================= LISTADO DE CUENTAS CORRIENTES ==================")
        print("--------------------------------------------------------------------")
        print(" Nº Cuenta  | DNI       | Nombre               | Saldo     | Estado")
        print("--------------------------------------------------------------------")
        
        for account in accounts:
            number, dni, name, lastname, balance, active = account
            status = "Activa" if active else "Inactiva"
            full_name = f"{name} {lastname}"
            print(f" {number:010} | {dni:<9} | {full_name:<20} | {balance:>8.2f}€ | {status:<8}")
        print()
            
    except Exception as e:
        print(f"Error al consultar las cuentas: {e}")
    finally:
        cursor.close()