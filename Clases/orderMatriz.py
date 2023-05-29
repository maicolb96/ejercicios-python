def ordenar_matriz(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas - 1):
            for k in range(filas):
                if matriz[k][j] > matriz[k][j + 1]:
                    matriz[k][j], matriz[k][j + 1] = matriz[k][j + 1], matriz[k][j]

    return matriz

# Ejemplo de uso
matriz = [[3, 2, 1],
          [6, 5, 4],
          [9, 8, 7]]

print("Matriz original:")
print(matriz)

matriz_ordenada = ordenar_matriz(matriz)
print("Matriz ordenada:")
print(matriz_ordenada)
