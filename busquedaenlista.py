# Lista de números a trabajar
numeros = [12, 45, 78, 23, 56, 89, 34, 67]

def buscar_numero(numero):
    """
    Devuelve el índice del número en la lista, o -1 si no existe.
    Usa .index() con manejo de excepciones.
    """
    try:
        indice = numeros.index(numero)
        return indice
    except ValueError:
        return -1

def numeros_mayores(umbral):
    """
    Devuelve una nueva lista con todos los números mayores que el umbral.
    Usa comprensión de listas para mayor eficiencia.
    """
    resultado = [num for num in numeros if num > umbral]
    return resultado

def promedio_lista(lista):
    """
    Calcula y devuelve el promedio de todos los elementos.
    Usa sum() y len() para simplificar el cálculo.
    """
    if len(lista) == 0:
        return 0
    promedio = sum(lista) / len(lista)
    return promedio

def ordenar_lista(lista):
    """
    Ordena los números de menor a mayor y devuelve la lista ordenada.
    Usa sorted() para no modificar la lista original.
    """
    lista_ordenada = sorted(lista)
    return lista_ordenada

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 60)
    print("🔍 BÚSQUEDA Y OPERACIONES EN LISTA")
    print("=" * 60)
    print(f"\n📊 Lista actual: {numeros}")
    print("\n" + "-" * 60)
    print("1. Buscar un número")
    print("2. Obtener números mayores que un umbral")
    print("3. Calcular promedio")
    print("4. Ordenar lista")
    print("5. Salir")
    print("-" * 60)

def opcion_buscar():
    """Opción 1: Buscar número"""
    try:
        numero = int(input("\nIngresa el número a buscar: "))
        indice = buscar_numero(numero)
        
        if indice == -1:
            print(f"❌ El número {numero} no se encuentra en la lista.\n")
        else:
            print(f"✅ El número {numero} se encuentra en el índice: {indice}\n")
    except ValueError:
        print("❌ Por favor, ingresa un número válido.\n")

def opcion_mayores():
    """Opción 2: Números mayores que un umbral"""
    try:
        umbral = int(input("\nIngresa el umbral: "))
        resultado = numeros_mayores(umbral)
        
        if resultado:
            print(f"\n✅ Números mayores que {umbral}:")
            print(f"   {resultado}\n")
        else:
            print(f"❌ No hay números mayores que {umbral}.\n")
    except ValueError:
        print("❌ Por favor, ingresa un número válido.\n")

def opcion_promedio():
    """Opción 3: Calcular promedio"""
    promedio = promedio_lista(numeros)
    print(f"\n✅ Promedio de la lista:")
    print(f"   {promedio:.2f}\n")

def opcion_ordenar():
    """Opción 4: Ordenar lista"""
    lista_ordenada = ordenar_lista(numeros)
    print(f"\n✅ Lista ordenada de menor a mayor:")
    print(f"   {lista_ordenada}\n")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            opcion_buscar()
        elif opcion == "2":
            opcion_mayores()
        elif opcion == "3":
            opcion_promedio()
        elif opcion == "4":
            opcion_ordenar()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el programa! Hasta luego.\n")
            break
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()