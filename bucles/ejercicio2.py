# Calcula la suma de todos los números pares del 1 al 50 utilizando un bucle for.
suma = 0
for i in range(1,51):
    if i % 2 == 0:
        suma += i
print(suma )