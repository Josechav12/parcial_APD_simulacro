"""1
def par_impar (numero):
    if numero %2 ==0:
        print("el numero es par")
    else:
        print("el numero es impar")

par_impar(5)
"""
"""2
def el_mas_grande(num1,num2,num3):
    if num1> num2 and num1 > num3:
        print(f"el mas grande es el {num1}")
    elif num2 > num3:
        print(f"el mas grande es el {num2} ")
    else:
        print(f"el mas grande es el {num3}")

el_mas_grande(5,1,6)
"""

def resultado_potencia(numero,potencia):
    resultado =  f"el resultado de la potencia es {numero ** potencia}"
    return resultado

print(resultado_potencia(2,2))
