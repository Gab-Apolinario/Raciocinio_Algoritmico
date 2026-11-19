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
    for i in range(tam_tab):
        tab[i] = [0] * tam_tab
    return tab


def mostrar_matriz(tab: list, tam_tab: int):
    for linha in range(tam_tab):
        for coluna in range(tam_tab):
            if tab[linha][coluna] == -1: #bomba
                print("*", end = " ")
            else:    
                print(tab[linha][coluna], end = " ")
        print()


def sortear_matriz(tab: list, qntd_bombas: int, tam_tab: int):
    bombas = 0
    while bombas < qntd_bombas:
        linha = randint(0, tam_tab - 1)
        coluna = randint(0, tam_tab - 1)
        if tab[linha][coluna] == 0: #casa livre
            tab[linha][coluna] = -1 #vira bomba
        bombas += 1
    return tab


tam_tab = escolher_tamanho()
tab = criar_matriz_tab(tam_tab)
qntd_bombas = quantidade_bombas(tam_tab)
mostrar_matriz(tab, tam_tab)
sortear_matriz(tab, qntd_bombas, tam_tab)
print()
print()
mostrar_matriz(tab, tam_tab)