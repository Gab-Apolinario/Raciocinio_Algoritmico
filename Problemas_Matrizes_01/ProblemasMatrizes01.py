# EXEMPLO SALA
# def mostra_matriz(m: list) -> None:
#     print(f"Matriz Função:")
#     for i in range(len(m)): # loop linhas -> len(m) devolve total de linhas
#         for j in range(len(m[i])): # loop colunas -> len(m[i]) devolve total de colunas naquela linha
#             print(m[i][j], end = " ")
#         print()

# m1 = [[1, 2, 3], [4, 5, 6]] # matriz 2x3, 6 elementos
# m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz 3x3, 9 elementos
# print(f"Print Puro: {m1}")
# print()
# mostra_matriz(m1)
# mostra_matriz(m2)

# EX.1: Desenvolva uma função chamada ler_matriz que recebe a dimensão de uma matriz(linha e coluna), cria, lê (com números inteiros)
# e retorna esta matriz. No programa principal, chame a função e mostre a matriz lida.

def ler_matriz(linhas: int, colunas: int) -> list:
    print(f"Você vai digitar uma matriz {linhas}x{colunas}:")
    m : list = ["0"] * linhas # criando linhas -> valor não importa
    
    for i in range(linhas):
        m[i] = ["x"] * colunas # criando colunas -> valor não importa
        for j in range(colunas):
            m[i][j] = input(f"   -> Posição linha {i}, coluna {j}: ")
    return m


mat = ler_matriz(3, 3)

# EX.2: Adicione ao script anterior uma função chamada mostrar_matriz que recebe uma matriz e imprime seu conteúdo em formato
# matricial. No programa principal, chame a função para mostrar a matriz lida pelo uso da função anterior.

def mostrar_matriz(matriz: list) -> list:
    print(f"\nMatriz -> {matriz} em formato de tabela:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end = " ")
        print()
    return matriz


mostrar_matriz(mat)

# EX.3: Adicione ao script anterior uma cfunção chamada mostrar_linha() que recebe uma matriz e o índice de uma linha.
# Ela então imprrime apenas o conteúdo da linha em particular (na horizontal). No programa principal, chame a função.

# EX.11: Adicione ao script anterior uma função chamada posicao_numero() que recebe uma matriz de números inteiros e um número inteiro
# a ser pesquisado. A função então devolve a posição da priemira ocorrência deste número na matriz através de uma tupla contendo linha e coluna
# da posição na qual se encontra o número (se não encontrar retorna -1, -1). Adicione o uso desta função ao programa principal.

def posicao_numero(matriz: list, pesquisar: int) -> tuple:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == pesquisar:
                print("chegou")
                return i, j
    return -1, -1

pesquisar = int(input("Número para pesquisar na matriz: "))
n = posicao_numero(mat, pesquisar)
print(n)