# Lista para almacenar los artículos de compra
lista_compras = []

def agregar_articulo():
    """Agrega un nuevo artículo a la lista de compras"""
    producto = input("Nombre del producto: ").strip()
    
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad: "))
        
        if precio < 0 or cantidad < 0:
            print("❌ El precio y la cantidad deben ser positivos.\n")
            return
        
        articulo = {
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad
        }
        lista_compras.append(articulo)
        print(f"✅ Artículo '{producto}' agregado correctamente.\n")
    except ValueError:
        print("❌ Error: Ingresa valores válidos (número para precio y cantidad).\n")

def ver_lista():
    """Muestra todos los artículos de la lista de compras"""
    if not lista_compras:
        print("📋 La lista de compras está vacía.\n")
        return
    
    print("\n📋 LISTA DE COMPRAS")
    print("-" * 50)
    for i, articulo in enumerate(lista_compras, 1):
        for clave, valor in articulo.items():
            if clave == "precio":
                print(f"  {clave}: ${valor:.2f}", end="")
            elif clave == "producto":
                print(f"{i}. {clave}: {valor}")
            else:
                print(f"  {clave}: {valor}")
        print()
    print("-" * 50 + "\n")

def calcular_total():
    """Calcula el costo total de la lista de compras"""
    if not lista_compras:
        print("📋 La lista de compras está vacía.\n")
        return
    
    total = 0
    print("\n💰 CÁLCULO DE TOTAL")
    print("-" * 50)
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        total += subtotal
        print(f"{articulo['producto']}: ${articulo['precio']:.2f} x {articulo['cantidad']} = ${subtotal:.2f}")
    print("-" * 50)
    print(f"TOTAL: ${total:.2f}\n")

def eliminar_articulo():
    """Elimina un artículo de la lista de compras"""
    if not lista_compras:
        print("📋 La lista de compras está vacía.\n")
        return
    
    ver_lista()
    producto_eliminar = input("Nombre del producto a eliminar: ").strip()
    
    for articulo in lista_compras:
        if articulo["producto"].lower() == producto_eliminar.lower():
            lista_compras.remove(articulo)
            print(f"✅ Artículo '{producto_eliminar}' eliminado correctamente.\n")
            return
    
    print(f"❌ No se encontró el producto '{producto_eliminar}' en la lista.\n")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 50)
    print("🛒 GESTOR DE COMPRAS")
    print("=" * 50)
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Calcular total")
    print("4. Eliminar artículo")
    print("5. Salir")
    print("=" * 50)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_articulo()
        elif opcion == "2":
            ver_lista()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            eliminar_articulo()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el Gestor de Compras! Hasta luego.\n")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()