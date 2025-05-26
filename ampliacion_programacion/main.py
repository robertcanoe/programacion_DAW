from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Listar todos los usuarios")
    print("2. Buscar usuario por ID")
    print("3. Agregar nuevo usuario")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("0. Salir")

def listar_usuarios(dao):
    print("\n--- LISTA DE USUARIOS ---")
    usuarios = dao.get_all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}, Activo: {'Sí' if usuario.activo else 'No'}")

def buscar_usuario(dao):
    try:
        usuario_id = int(input("\nIngrese el ID del usuario a buscar: "))
        usuario = dao.get_by_id(usuario_id)
        if usuario:
            print(f"\nUsuario encontrado:")
            print(f"ID: {usuario.id}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Email: {usuario.email}")
            print(f"Fecha de registro: {usuario.fecha_registro}")
            print(f"Activo: {'Sí' if usuario.activo else 'No'}")
        else:
            print("No se encontró ningún usuario con ese ID.")
    except ValueError:
        print("Por favor, ingrese un ID válido (número entero).")

def agregar_usuario(dao):
    print("\n--- AGREGAR NUEVO USUARIO ---")
    nombre = input("Nombre: ")
    email = input("Email: ")
    activo = input("¿Usuario activo? (s/n): ").lower() == 's'
    
    nuevo_usuario = Usuario(nombre=nombre, email=email, activo=activo)
    usuario_creado = dao.create(nuevo_usuario)
    
    if usuario_creado:
        print(f"\nUsuario creado exitosamente con ID: {usuario_creado.id}")
    else:
        print("Error al crear el usuario.")

def actualizar_usuario(dao):
    try:
        usuario_id = int(input("\nIngrese el ID del usuario a actualizar: "))
        usuario = dao.get_by_id(usuario_id)
        
        if not usuario:
            print("No se encontró ningún usuario con ese ID.")
            return
            
        print("\nDeje en blanco los campos que no desea modificar.")
        nuevo_nombre = input(f"Nuevo nombre [{usuario.nombre}]: ") or usuario.nombre
        nuevo_email = input(f"Nuevo email [{usuario.email}]: ") or usuario.email
        nuevo_estado = input(f"¿Usuario activo? (s/n) [{'s' if usuario.activo else 'n'}]: ").lower()
        nuevo_estado = usuario.activo if nuevo_estado == '' else nuevo_estado == 's'
        
        usuario.nombre = nuevo_nombre
        usuario.email = nuevo_email
        usuario.activo = nuevo_estado
        
        if dao.update(usuario):
            print("Usuario actualizado exitosamente.")
        else:
            print("Error al actualizar el usuario.")
    except ValueError:
        print("Por favor, ingrese un ID válido (número entero).")

def eliminar_usuario(dao):
    try:
        usuario_id = int(input("\nIngrese el ID del usuario a eliminar: "))
        confirmacion = input(f"¿Está seguro de que desea eliminar al usuario con ID {usuario_id}? (s/n): ").lower()
        
        if confirmacion == 's':
            if dao.delete(usuario_id):
                print("Usuario eliminado exitosamente.")
            else:
                print("No se pudo eliminar el usuario. Verifique el ID e intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un ID válido (número entero).")

def main():
    # Crear una instancia del DAO
    dao = UsuarioDAO()
    
    try:
        while True:
            mostrar_menu()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == '1':
                listar_usuarios(dao)
            elif opcion == '2':
                buscar_usuario(dao)
            elif opcion == '3':
                agregar_usuario(dao)
            elif opcion == '4':
                actualizar_usuario(dao)
            elif opcion == '5':
                eliminar_usuario(dao)
            elif opcion == '0':
                print("\n¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
    finally:
        dao.close()

if __name__ == "__main__":
    main()