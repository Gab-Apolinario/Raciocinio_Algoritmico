from random import randint

def escolher_tamanho():
    tam_tab = int(input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): "))
    while tam_tab not in [9, 16, 30]:
        print("Digite um tamanho válido!")
        tam_tab = int(input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): "))
    return tam_tab


def quantidade_bombas(tam_tab: int) -> int:
    qntd_bombas = 99
    if tam_tab == 9:
        qntd_bombas = 10
    elif tam_tab == 16:
        qntd_bombas = 40
    print(f"QUANTIDADE DE BOMBAS: {qntd_bombas}")
    return qntd_bombas


def criar_matriz_tab(tam_tab: int):
    tab = [0] * tam_tab
    tam_col: int = tam_tab #inciia por conta do tabuleiro 30x16
    if tam_tab == 30:
        tam_col = 16
        
    for i in range(tam_tab):
        tab[i] = [0] * tam_col #cria colunas no tamanho certo
    return tab


def mostrar_matriz(tab: list):
    linhas = len(tab)
    colunas = len(tab[0])
    ## LINHA VISUAL COLUNA
    
    print(" " * 5, end = "") #adiciona espaços para alinhar letras na matriz
    for i in range(colunas):
        print(chr(ord('A') + i), end = " ") #pega chr do int e adiciona i para mostras as letras seguintes
    print()
    
    for linha in range(linhas):
        print(f"{linha + 1: 3}", end = "  ") #COLUNA VISUAL com espaçamento fixo
        for coluna in range(colunas):
            if tab[linha][coluna] == -1: #bomba
                print("*", end = " ")
            else:    
                print(tab[linha][coluna], end = " ")
        print()


def sortear_matriz(tab: list, qntd_bombas: int, tam_tab: int):
    bombas = 0
    while bombas < qntd_bombas:
        linha = randint(0, tam_tab - 1)
        coluna = randint(0, len(tab[linha]) - 1)
        if tab[linha][coluna] == 0: #casa livre
            tab[linha][coluna] = -1 #vira bomba
            bombas += 1 #soma somente quando altera casa para bomba
    return tab


def calcular_dicas(tab: list):
    for linha in range(len(tab)): #percorre linhas
        for coluna in range(len(tab[linha])): #percorre colunas
            if tab[linha][coluna] == -1: #se a casa for bomba
                for lin in range(-1, 2, 1):
                    for col in range(-1, 2, 1):
                        viz_lin = linha + lin #casa vizinha
                        viz_col = coluna + col #casa vizinha
                        if 0 <= viz_lin < len(tab) and 0 <= viz_col < len(tab[linha]): #ver se a casa existe. linha é >= 0 e < totalCasas. Coluna >= 0 e < totalColunas
                            if tab[viz_lin][viz_col] != -1: #se NÃO é bomba, acrescenta
                                tab[viz_lin][viz_col] += 1
    return tab


tam_tab = escolher_tamanho()
tab = criar_matriz_tab(tam_tab)
qntd_bombas = quantidade_bombas(tam_tab)
mostrar_matriz(tab)
sortear_matriz(tab, qntd_bombas, tam_tab)
print()
print()
mostrar_matriz(tab)
calcular_dicas(tab)
print()
mostrar_matriz(tab)