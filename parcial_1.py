# Sistema de Inventario para "Empire Inventory"
inventario = []

# Función para mostrar el menú
def mostrar_menu():
    print("--- Menú Principal ---")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto más caro y más barato")
    print("5. Mostrar productos con precio mayor a 15000")
    print("6. Salir")

# Función para cargar productos en el inventario
def cargar_productos():
    cantidad = int(input("Ingrese la cantidad de productos a cargar: "))
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad de productos: "))
        inventario.append([nombre, precio, cantidad_producto])
        print(f"Producto/s '{nombre}' agregado exitosamente.")

# Función para buscar un producto por nombre
def buscar_producto(nombre_buscado):
    if not inventario:
        print("No hay productos disponibles en el inventario.")
        return
    for producto in inventario:
        if producto[0] == nombre_buscado:
            print(f"Producto encontrado: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
            return producto
    print(f"Producto '{nombre_buscado}' no encontrado.")
    return None

# Función para ordenar el inventario por precio (de menor a mayor)
def ordenar_inventario():
    if not inventario:
        print("No hay productos disponibles en el inventario.")
        return
    for i in range(len(inventario)):
        for j in range(0, len(inventario)-i-1):
            if inventario[j][1] > inventario[j+1][1]:  # Comparar precios
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]  # Intercambiar
    print("Inventario ordenado por precio (de menor a mayor):")
    mostrar_inventario()

# Función para mostrar el producto más caro y más barato
def mostrar_caros_baratos():
    if not inventario:
        print("No hay productos disponibles en el inventario.")
        return
    producto_mas_caro = max(inventario, key=lambda x: x[1])
    producto_mas_barato = min(inventario, key=lambda x: x[1])
    print(f"Producto más caro: {producto_mas_caro[0]}, Precio: {producto_mas_caro[1]}")
    print(f"Producto más barato: {producto_mas_barato[0]}, Precio: {producto_mas_barato[1]}")

# Función para mostrar productos con precio mayor a un umbral dado
def mostrar_productos_caros(umbral_precio):
    if not inventario:
        print("No hay productos disponibles en el inventario.")
        return
    productos_caros = [producto for producto in inventario if producto[1] > umbral_precio]
    if productos_caros:
        print(f"Productos con precio mayor a {umbral_precio}:")
        for producto in productos_caros:
            print(f"{producto[0]} - Precio: {producto[1]}")
    else:
        print(f"No hay productos con precio mayor a {umbral_precio}.")

# Función para mostrar el inventario completo
def mostrar_inventario():
    if not inventario:
        print("No hay productos disponibles en el inventario.")
    else:
        print(f"{'Producto':<15} {'Precio':<10} {'Cantidad':<10}")
        print("-" * 35)
        for producto in inventario:
            print(f"{producto[0]:<15} {producto[1]:<10.2f} {producto[2]:<10}")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cargar_productos()
        elif opcion == '2':
            nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
            buscar_producto(nombre_buscado)
        elif opcion == '3':
            ordenar_inventario()
        elif opcion == '4':
            mostrar_caros_baratos()
        elif opcion == '5':
            umbral = 15000
            mostrar_productos_caros(umbral)
        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
main()
