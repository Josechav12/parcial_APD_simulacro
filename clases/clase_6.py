"""forma iterativa
def contar_hasta_cero(numero):
    for i in range(numero, -1, -1):
        print(i)

    contar_hasta_cero
"""
"""forma recursiva
def contar_recursivamente(numero):
    if numero < 0:
        return
    print(numero)
    contar_recursivamente(numero -1)

contar_recursivamente
"""
"""5! = 5*4*3*2*1 = 120
def factorial_iterativo(numero):
    if numero < 0:
        return "El factorial no se puede realizar"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
        
print(factorial_iterativo(5))


def factorial_recursivo(numero):
    if numero ==0:
        return 1
    else:
        return numero * factorial_recursivo(numero -1)
    
print(factorial_recursivo(4))
def fibonacci_iter(numero):
    a = 0
    b = 1
    for _ in range(numero):
        resultado = a+b
        a = b
        b = resultado
        print(resultado)
    return resultado

resultado = fibonacci_iter(6)
print(resultado)

def fibonacci_recur(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    else:
        resultado = fibonacci_recur(numero - 1) + fibonacci_recur(numero -2)
        return resultado

resultado = fibonacci_recur
print(resultado)
"""
def recursiva (numero):
    if numero == 1:
        return 1
    else:
        return recursiva(numero - 1) + numero

print(recursiva(5))