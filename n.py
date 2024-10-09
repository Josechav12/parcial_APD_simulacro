def busqueda_secuencial_matriz(elemento, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                return f'Elemento encontrado en la posición ({i}, {j})'
    return "Elemento no encontrado"

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento_a_buscar = 10
resultado = busqueda_secuencial_matriz(elemento_a_buscar, matriz)
print(resultado)
