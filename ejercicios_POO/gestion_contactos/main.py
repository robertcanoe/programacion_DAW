import os
import re
from contacto import Contacto, GestorContactos

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('clear' if os.name == 'posix' else 'cls')

def crear_separador(longitud):
    """Crea un separador del ancho especificado."""
    return "═" * max(30, longitud + 2)

def crear_marco_superior(ancho):
    """Crea el marco superior del menú."""
    return f"╔{'═' * (ancho - 2)}╗"

def crear_marco_medio(ancho):
    """Crea una línea de separación en el menú."""
    return f"╠{'═' * (ancho - 2)}╣"

def crear_marco_inferior(ancho):
    """Crea el marco inferior del menú."""
    return f"╚{'═' * (ancho - 2)}╝"

def crear_linea(texto, ancho):
    """Crea una línea de texto centrada."""
    return f"║{texto.center(ancho - 2)}║"

def crear_linea_izquierda(texto, ancho):
    """Crea una línea de texto alineada a la izquierda."""
    return f"║ {texto.ljust(ancho - 3)}║"



def mostrar_menu():
    """Muestra el menú principal."""
    limpiar_pantalla()
    opciones = [
        "1. Crear archivo de contactos",
        "2. Mostrar todos los contactos",
        "3. Añadir nuevo contacto",
        "4. Buscar contacto por nombre",
        "5. Eliminar contacto",
        "6. Salir"
    ]
    
    # Calcular el ancho necesario
    ancho = max(len(opcion) for opcion in opciones) + 6
    
    print(f"\n    {crear_marco_superior(ancho)}")
    print(f"    {crear_linea('GESTIÓN DE CONTACTOS', ancho)}")
    print(f"    {crear_marco_medio(ancho)}")
    
    for opcion in opciones:
        print(f"    {crear_linea_izquierda(opcion, ancho)}")
    
    print(f"    {crear_marco_inferior(ancho)}")

def mostrar_contactos(gestor):
    """Muestra todos los contactos."""
    limpiar_pantalla()
    titulo = "LISTA DE CONTACTOS"
    ancho = max(50, len(titulo) + 20)
    
    print(f"\n    {crear_marco_superior(ancho)}")
    print(f"    {crear_linea(titulo, ancho)}")
    print(f"    {crear_marco_medio(ancho)}")
    
    if not gestor.contactos:
        print(f"    {crear_linea('No hay contactos para mostrar', ancho)}")
        print(f"    {crear_marco_inferior(ancho)}\n")
        input("    Presione Enter para continuar...")
        return
        
    for i, contacto in enumerate(gestor.contactos, 1):
        print(f"    {crear_linea(f'Contacto {i}', ancho)}")
        print(f"    {crear_linea_izquierda(f'Nombre: {contacto.nombre}', ancho)}")
        print(f"    {crear_linea_izquierda(f'Teléfono: {contacto.telefono}', ancho)}")
        print(f"    {crear_linea_izquierda(f'Email: {contacto.email}', ancho)}")
        if i < len(gestor.contactos):
            print(f"    {crear_marco_medio(ancho)}")
    
    print(f"    {crear_marco_inferior(ancho)}\n")
    input("    Presione Enter para continuar...")

def agregar_contacto(gestor):
    """Añade un nuevo contacto."""
    try:
        limpiar_pantalla()
        titulo = "AÑADIR NUEVO CONTACTO"
        ancho = 50
        
        print(f"\n    {crear_marco_superior(ancho)}")
        print(f"    {crear_linea(titulo, ancho)}")
        print(f"    {crear_marco_medio(ancho)}")
        
        # Validar nombre
        while True:
            try:
                nombre = input("    Nombre: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío")
                if any(c.nombre.lower() == nombre.lower() for c in gestor.contactos):
                    raise ValueError("Ya existe un contacto con ese nombre")
                break
            except ValueError as e:
                print(f"    Error: {e}")
                print("    " + "─" * 30)
        
        # Validar teléfono
        while True:
            try:
                telefono = input("    Teléfono: ").strip()
                if not telefono:
                    raise ValueError("El teléfono no puede estar vacío")
                if not telefono.isdigit() or len(telefono) != 9:
                    raise ValueError("El teléfono debe tener exactamente 9 dígitos")
                break
            except ValueError as e:
                print(f"    Error: {e}")
                print("    " + "─" * 30)
        
        # Validar email
        while True:
            try:
                email = input("    Correo electrónico: ").strip()
                if not email:
                    raise ValueError("El correo electrónico no puede estar vacío")
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    raise ValueError("El correo electrónico no tiene un formato válido")
                break
            except ValueError as e:
                print(f"    Error: {e}")
                print("    " + "─" * 30)
        
        # Crear y guardar el contacto
        nuevo_contacto = Contacto(nombre=nombre, telefono=telefono, email=email)
        gestor.contactos.append(nuevo_contacto)
        gestor.guardar_contactos()
        
        mensaje = "¡Contacto agregado correctamente!"
        ancho_mensaje = len(mensaje) + 4
        print(f"    {crear_marco_superior(ancho_mensaje)}")
        print(f"    {crear_linea(mensaje, ancho_mensaje)}")
        print(f"    {crear_marco_inferior(ancho_mensaje)}")
        
    except Exception as e:
        print(f"\n    Error inesperado: {e}")
    
    input("\n    Presione Enter para continuar...")

def buscar_contacto(gestor):
    """Busca un contacto por nombre."""
    limpiar_pantalla()
    titulo = "BUSCAR CONTACTO"
    ancho = 50
    
    print(f"\n    {crear_marco_superior(ancho)}")
    print(f"    {crear_linea(titulo, ancho)}")
    print(f"    {crear_marco_medio(ancho)}")
    
    if not gestor.contactos:
        print("    ║  No hay contactos para buscar  ║")
        print("    ╚══════════════════════════════╝\n")
        input("    Presione Enter para continuar...")
        return
        
    nombre = input("    \n    Ingrese el nombre del contacto a buscar: ").strip().lower()
    encontrados = [c for c in gestor.contactos if nombre in c.nombre.lower()]
    
    limpiar_pantalla()
    print("\n    ╔══════════════════════════════╗")
    print("    ║     RESULTADOS DE BÚSQUEDA    ║")
    print("    ╠══════════════════════════════╣")
    
    if not encontrados:
        print("    ║  No se encontraron contactos  ║")
        print("    ║  con ese nombre.              ║")
    else:
        for i, contacto in enumerate(encontrados, 1):
            print(f"    ║  Contacto {i}:" + " " * 16 + "║")
            print(f"    ║  Nombre: {contacto.nombre.ljust(20)} ║")
            print(f"    ║  Teléfono: {contacto.telefono.ljust(17)} ║")
            print(f"    ║  Email: {contacto.email.ljust(21)} ║")
            if i < len(encontrados):
                print("    ╟──────────────────────────────╢")
    
    print("    ╚══════════════════════════════╝\n")
    input("    Presione Enter para continuar...")

def eliminar_contacto(gestor):
    """Elimina un contacto por nombre."""
    limpiar_pantalla()
    titulo = "ELIMINAR CONTACTO"
    ancho = 50
    
    print(f"\n    {crear_marco_superior(ancho)}")
    print(f"    {crear_linea(titulo, ancho)}")
    print(f"    {crear_marco_medio(ancho)}")
    
    if not gestor.contactos:
        print("    ║  No hay contactos para       ║")
        print("    ║  eliminar.                   ║")
        print("    ╚══════════════════════════════╝\n")
        input("    Presione Enter para continuar...")
        return
        
    nombre = input("    \n    Ingrese el nombre del contacto a eliminar: ").strip()
    
    for i, contacto in enumerate(gestor.contactos):
        if contacto.nombre.lower() == nombre.lower():
            print("    " + "=" * 30)
            confirmacion = input(f"    ¿Está seguro de eliminar a {contacto.nombre}? (s/n): ").lower()
            if confirmacion == 's':
                del gestor.contactos[i]
                gestor.guardar_contactos()
                mensaje = "Contacto eliminado correctamente."
                ancho_mensaje = len(mensaje) + 4
                print(f"    {crear_marco_superior(ancho_mensaje)}")
                print(f"    {crear_linea(mensaje, ancho_mensaje)}")
                print(f"    {crear_marco_inferior(ancho_mensaje)}")
            else:
                mensaje = "Operación cancelada."
                ancho_mensaje = len(mensaje) + 4
                print(f"    {crear_marco_superior(ancho_mensaje)}")
                print(f"    {crear_linea(mensaje, ancho_mensaje)}")
                print(f"    {crear_marco_inferior(ancho_mensaje)}")
            input("\n    Presione Enter para continuar...")
            return
            
    print("\n    No se encontró ningún contacto con ese nombre.")
    input("\n    Presione Enter para continuar...")

def main():
    """Función principal del programa."""
    gestor = GestorContactos()
    
    while True:
        mostrar_menu()
        try:
            opcion = input("\n    Seleccione una opción: ")
            
            if opcion == '1':
                gestor.crear_archivo()
            elif opcion == '2':
                mostrar_contactos(gestor)
            elif opcion == '3':
                agregar_contacto(gestor)
            elif opcion == '4':
                buscar_contacto(gestor)
            elif opcion == '5':
                eliminar_contacto(gestor)
            elif opcion == '6':
                print("\n    ¡Hasta luego!")
                break
            else:
                print("\n    Opción no válida. Por favor, intente de nuevo.")
                input("    Presione Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
