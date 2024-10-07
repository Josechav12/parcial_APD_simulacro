# vector = [12,34,"hola",65]
# for i in range(len(vector)):
#     print(vector[i])

# matriz = [
#     [12,34,65,54],
#     [54,34,34,45],
#     [523,45,34,34]
# ]
#mostrarme toda la matriz:
# for i in range(len(matriz)):
#     print(matriz[i])

#muestra la ultima fila:
# for i in range(len(matriz)):
# print(matriz[-1])

#camnbia un numero dela matriz:
# matriz[1][2] = 77
# for i in range(len(matriz)):
#     print(matriz[i])
#muestra los numeros con espacio
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j],end=" ")
#     print("")


def buscar_valor(matriz,valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i,j)

matriz = [
    [12,34,65,54],
    [54,34,9,45],
    [523,45,34,34]]

print(buscar_valor(matriz,9))

