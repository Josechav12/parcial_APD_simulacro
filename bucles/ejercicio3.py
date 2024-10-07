# Solicitarle al usuario que ingrese un número y 
# se muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.

multiplicar = int(input("ingrese un numero: "))

for i in range(1,11):
    resultado = multiplicar * i

    print(f"{multiplicar}x{i} = {resultado} ")