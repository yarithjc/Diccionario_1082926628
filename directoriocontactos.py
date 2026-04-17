# Diccionario para almacenar los contactos
directorio_contactos = {}

def agregar_contacto():
    """Agrega un nuevo contacto al directorio"""
    nombre = input("Nombre del contacto: ").strip()
    
    if nombre in directorio_contactos:
        print(f"❌ El contacto '{nombre}' ya existe.\n")
        return
    
    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()
    ciudad = input("Ciudad: ").strip()
    
    directorio_contactos[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad
    }
    print(f"✅ Contacto '{nombre}' agregado correctamente.\n")

def ver_todos_contactos():
    """Muestra todos los contactos del directorio"""
    if not directorio_contactos:
        print("📋 El directorio de contactos está vacío.\n")
        return
    
    print("\n" + "=" * 60)
    print("📞 DIRECTORIO DE CONTACTOS")
    print("=" * 60)
    
    for nombre, datos in directorio_contactos.items():
        print(f"\n👤 Nombre: {nombre}")
        for campo, valor in datos.items():
            print(f"   • {campo.capitalize()}: {valor}")
    
    print("\n" + "=" * 60 + "\n")

def buscar_por_nombre():
    """Busca un contacto por nombre"""
    nombre = input("Nombre del contacto a buscar: ").strip()
    
    contacto = directorio_contactos.get(nombre)
    
    if contacto is None:
        print(f"❌ No se encontró el contacto '{nombre}' en el directorio.\n")
        return
    
    print(f"\n✅ Contacto encontrado:")
    print(f"   👤 Nombre: {nombre}")
    for campo, valor in contacto.items():
        print(f"   • {campo.capitalize()}: {valor}")
    print()

def actualizar_telefono():
    """Actualiza el teléfono de un contacto"""
    nombre = input("Nombre del contacto: ").strip()
    
    contacto = directorio_contactos.get(nombre)
    
    if contacto is None:
        print(f"❌ No se encontró el contacto '{nombre}' en el directorio.\n")
        return
    
    nuevo_telefono = input("Nuevo teléfono: ").strip()
    directorio_contactos[nombre]["teléfono"] = nuevo_telefono
    print(f"✅ Teléfono de '{nombre}' actualizado correctamente.\n")

def eliminar_contacto():
    """Elimina un contacto del directorio"""
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    contacto = directorio_contactos.pop(nombre, None)
    
    if contacto is None:
        print(f"❌ No se encontró el contacto '{nombre}' en el directorio.\n")
        return
    
    print(f"✅ Contacto '{nombre}' eliminado correctamente.\n")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 60)
    print("📞 GESTOR DE DIRECTORIO DE CONTACTOS")
    print("=" * 60)
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar por nombre")
    print("4. Actualizar teléfono")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("=" * 60)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_todos_contactos()
        elif opcion == "3":
            buscar_por_nombre()
        elif opcion == "4":
            actualizar_telefono()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el Directorio de Contactos! Hasta luego.\n")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()