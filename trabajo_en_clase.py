"""
def invertir_cadena(usuario: str) ->str:
    cadena_invertida =""
    for letra in usuario:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida
    
usuario = input("ingresa una palabra: ")

resultado = invertir_cadena(usuario)
print(resultado)"""

"""
def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input("ingrese una cadena: ")

print(invertir_cadena(cadena))"""


# Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.
# 1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada.
# 2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
# 3. Extraer la nota y almacenarla en una variable llamada nota.
# 4. Extraer la materia y almacenarla en una variable llamada materia. 
# 5.  Mostrar por pantalla la siguiente estructura, usando la concantenación de cadenas: NOMBRE APELLIDO ha sacado un NOTA en MATERIA
"""
# 1. Dar vuelta la cadena
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]

nombre_apellido = cadena_volteada.split(",")[0]

nota = cadena_volteada.split(",")[1]

materia = cadena_volteada.split(",")[2]

resultado = f"{nombre_apellido} ha sacado un {nota} en {materia}"
print(resultado)"""



numero = 5

for i in range(numero):
    # Imprimir la primera parte de los números
    for j in range(1, numero - i + 1):
        print(j, end='')
    
    # Imprimir espacios
    print(' ' * (2 * i - 1), end='')
    
    # Imprimir la segunda parte de los números
    if i != numero - 1:
        for j in range(numero - i, 0, -1):
            print(j, end='')
    
    print()  # Nueva línea