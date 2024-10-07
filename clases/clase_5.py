"""invertir palabras
def invertir_cadena(usuario: str) ->str:
    cadena_invertida =""
    for letra in usuario:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida
    
usuario = input("ingresa una palabra: ")

resultado = invertir_cadena(usuario)
print(resultado)
"""

# Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion) 
# y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos 
# (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
#  y terminar el programa. Si todos los datos fueron bien ingresados, 
    #segunda parte
# el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas, 
# los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades.
# Determinar mediante funciones si una persona puede o no jubilarse.
edad_minima = 1
edad_maxima = 99

femenino = "f"
masculino = "m"
no_binario = "x"

def validar_edad(edad:int) -> int:
    while edad < edad_minima or edad > edad_maxima:
        edad = int(input("error, ingrese un valor correcto: "))
    return edad

def validad_genero(genero:str) -> str:
    while genero != masculino and genero != femenino and genero != no_binario:
        genero = int(input("error, ingrese un valor valido(F, M o X): "))
    return genero


promedio= (60 +65)/2 
def jubilarse(edad:int, genero: str):
    mensaje = "puede jubilarse"
    if genero == femenino and edad >= 60:
        return mensaje
    elif genero == masculino and edad >= 65:
        return mensaje
    elif genero == no_binario and edad >= promedio:
        return mensaje
    else:
        return "no podes jubilarte, segui laburando"

edad = int(input("ingrese su edad: "))
# validar_edad(edad)
edad = validar_edad(edad)

genero = input("ingrese su genero: ")
# validad_genero(genero)
genero = validad_genero(genero)

resultado = jubilarse(edad, genero)
print(resultado)