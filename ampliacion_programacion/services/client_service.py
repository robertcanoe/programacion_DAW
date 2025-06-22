from errors.client_error import *
from clients.client import Client
from clients.client_repository import MySQLClientDAO
from services._db_integrity_import import IntegrityError

def ask_client_data(mysql_client):
    # 1. Pedir y validar el DNI
    for intento in range(3):
        try:
            dni = input("Añade tu DNI (o escribe 'salir' para cancelar): ")
            if dni.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            Client._validate_format_dni(dni)
            # Comprobar si ya existe en la base de datos
            existing = mysql_client.get_client(dni)
            if existing:
                print("❌ Ya existe un cliente registrado con ese DNI. No es posible añadirlo de nuevo.\n")
                return
            break
        except (LetterErrorDNI, FormatErrorDNI) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return
    
    # 2. Pedir el resto de datos solo si el DNI es válido y no existe
    name = input("Añade tu nombre: ")
    lastname = input("Añade tu apellido: ")

    for intento in range(3):
        try:
            phone = input("Añade tu número de teléfono (o escribe 'salir' para cancelar): ")
            if phone.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            Client._validate_phone(phone)
            break
        except ValidationException as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    address = input("Añade tu dirección: ")

    customer = Client(dni, name, lastname, phone, address)
    try:
        mysql_client.add_client(customer)
        print("Cliente añadido correctamente.\n\n")
    except IntegrityError as e:
        if hasattr(e, 'errno') and e.errno == 1062:
            print("❌ Ya existe un cliente registrado con ese DNI. No es posible añadirlo de nuevo.\n")
        else:
            print(f"❌ Error inesperado al añadir el cliente: {e}\n")
    except Exception as e:
        print(f"❌ Error inesperado al añadir el cliente: {e}\n")

def ask_customer_release_client(mysql_client):
    for intento in range(3):
        dni = input("Ingresa el dni del cliente que quieras reactivar (o escribe 'salir' para cancelar): ")
        if dni.strip().lower() == 'salir':
            print("Operación cancelada por el usuario.\n")
            return
        try:
            Client._validate_format_dni(dni)
            mysql_client.release(dni)
            break
        except (LetterErrorDNI, FormatErrorDNI) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

def ask_customer_deregister_client(mysql_client, mysql_account):
    for intento in range(3):
        dni = input("Ingresa el dni del cliente que quieras dar de baja (o escribe 'salir' para cancelar): ")
        if dni.strip().lower() == 'salir':
            print("Operación cancelada por el usuario.\n")
            return
        try:
            Client._validate_format_dni(dni)
            if mysql_account.has_active_accounts(dni):
                print("No se puede dar de baja al cliente porque tiene cuentas corrientes activas.")
                return
            mysql_client.deregister(dni)
            break
        except (LetterErrorDNI, FormatErrorDNI) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

def update_client_data(mysql_client):
    for intento in range(3):
        try:
            dni = input("Añade el DNI del cliente que quieras modificar (o escribe 'salir' para cancelar): ")
            if dni.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return
            Client._validate_format_dni(dni)
            current_customer = mysql_client.get_client(dni)
            if not current_customer:
                print("No se encontró ningún cliente con ese DNI.")
                input("Pulsa ENTER para continuar...")
                continue
            if not current_customer.active:
                print("No se puede modificar un cliente inactivo. Reactívalo antes de modificarlo.")
                input("Pulsa ENTER para continuar...")
                return
            break
        except (LetterErrorDNI, FormatErrorDNI) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        print("Demasiados intentos fallidos. Operación cancelada.\n")
        return

    try:
        name = input("Añade el nuevo nombre (Enter para mantener el actual): ")
        name = name if name.strip() else current_customer.name
        
        lastname = input("Añade el nuevo apellido (Enter para mantener el actual): ")
        lastname = lastname if lastname.strip() else current_customer.lastname

        phone = get_updated_phone(current_customer.phone)
        
        address = input("Añade la nueva dirección (Enter para mantener el actual): ")
        address = address if address.strip() else current_customer.address

        mysql_client.update_client(name, lastname, phone, address, dni)
        print("Cliente actualizado correctamente.")
        input("Pulsa ENTER para continuar...")
    except Exception as e:
        print(f"Error al actualizar el cliente: {e}")
        input("Pulsa ENTER para continuar...")

def get_updated_phone(current_phone):
    for intento in range(3):
        try:
            phone = input("Añade el nuevo número de teléfono (Enter para mantener el actual o escribe 'salir' para cancelar): ")
            if phone.strip().lower() == 'salir':
                print("Operación cancelada por el usuario.\n")
                return current_phone
            if phone.strip():
                Client._validate_phone(phone)
                return phone
            return current_phone
        except ValidationException as e:
            print(f"Error: {e}")
    else:
        print("Demasiados intentos fallidos. Se mantiene el teléfono actual.\n")
        return current_phone

def show_clients(mysql_client):
    cursor = mysql_client.connection.cursor()
    try:
        cursor.execute("""
            SELECT dni, nombre, apellido, telefono, direccion, activo
            FROM customer
            ORDER BY nombre, apellido
        """)
        customers = cursor.fetchall()

        print("================================ LISTADO DE CLIENTES ================================")
        print("-------------------------------------------------------------------------------------")
        print(" DNI       | Nombre               | Teléfono  | Dirección                | Estado  ")
        print("-------------------------------------------------------------------------------------")

        for customer in customers:
            dni, name, lastname, phone, address, active = customer
            status = "Activa" if active else "Inactiva"
            full_name = f"{name} {lastname}"
            print(f" {dni:<9} | {full_name:<20} | {phone:<9} | {address:<24} | {status:<7}")
        print()
    
    except Exception as e:
        print(f"Error al consultar los clientes: {e}")
    finally:
        cursor.close()