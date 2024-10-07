# Solicitarle al usuario que ingrese una palabra y que nuestro
# algoritmo cuente cuántas vocales tiene utilizando un bucle for.

# Solicitar al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Recorrer cada letra de la palabra
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1

# Mostrar el resultado
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")