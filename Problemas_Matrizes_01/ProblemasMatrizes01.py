def mostra_matriz(m: list) -> None:
    print(f"Matriz Função:")
    for i in range(len(m)): # loop linhas -> len(m) devolve total de linhas
        for j in range(len(m[i])): # loop colunas -> len(m[i]) devolve total de colunas naquela linha
            print(m[i][j], end = " ")
        print()

m1 = [[1, 2, 3], [4, 5, 6]] # matriz 2x3, 6 elementos
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz 3x3, 9 elementos
print(f"Print Puro: {m1}")
print()
mostra_matriz(m1)
mostra_matriz(m2)