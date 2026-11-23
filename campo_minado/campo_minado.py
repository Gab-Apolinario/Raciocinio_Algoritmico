from random import randint
BOMBA : int = -1
FECHADA : int = -10
ABERTA : int = 1
BANDEIRA : int = 100

#pergunta o tamanho do tabuleiro e repete até a resposta ser válida
def escolher_tamanho():
    tam_tab = int(input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): "))
    while tam_tab not in [9, 16, 30]:
        print("Digite um tamanho válido!")
        tam_tab = int(input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): "))
    return tam_tab


#devolve quantas bombas o modo escolhido tem
def quantidade_bombas(tam_tab: int) -> int:
    qntd_bombas = 99
    if tam_tab == 9:
        qntd_bombas = 10
    elif tam_tab == 16:
        qntd_bombas = 40
    print(f"QUANTIDADE DE BOMBAS: {qntd_bombas}")
    return qntd_bombas


#cria uma matriz do tamanho do modo, com todas as casas iguais a "valor"
#serve para as duas: tab (valor 0) e estado (valor FECHADA)
def criar_matriz(tam_tab: int, valor: int):
    matriz = [valor] * tam_tab
    tam_col: int = tam_tab #incia por conta do tabuleiro 30x16
    if tam_tab == 30:
        tam_col = 16
        
    for i in range(tam_tab):
        matriz[i] = [valor] * tam_col #cria colunas no tamanho certo
    return matriz


def mostrar_matriz(tab: list, estado: list):
    #tab = conteúdo real das casas | estado = quais estão fechadas/abertas
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
            if estado[linha][coluna] == FECHADA: #casa fechada
                print("■", end = " ")
            elif estado[linha][coluna] == BANDEIRA:
                print("#", end = " ")
            else: #casa aberta
                if tab[linha][coluna] == BOMBA:
                    print("*", end = " ")
                else:
                    print(tab[linha][coluna], end = " ")
        print()


#coloca as bombas em casas aleatórias de tab
def sortear_bombas(tab: list, qntd_bombas: int, tam_tab: int):
    bombas = 0
    while bombas < qntd_bombas:
        linha = randint(0, tam_tab - 1)
        coluna = randint(0, len(tab[linha]) - 1)
        if tab[linha][coluna] == 0: #casa livre
            tab[linha][coluna] = BOMBA #vira bomba
            bombas += 1 #soma somente quando altera casa para bomba


#para cada bomba, soma 1 em cada casa vizinha que não é bomba
def calcular_dicas(tab: list):
    for linha in range(len(tab)): #percorre linhas
        for coluna in range(len(tab[linha])): #percorre colunas
            if tab[linha][coluna] == BOMBA: #se a casa for bomba
                for lin in range(-1, 2, 1):
                    for col in range(-1, 2, 1):
                        viz_lin = linha + lin #casa vizinha
                        viz_col = coluna + col #casa vizinha
                        if 0 <= viz_lin < len(tab) and 0 <= viz_col < len(tab[linha]): #ver se a casa existe. linha é >= 0 e < totalCasas. Coluna >= 0 e < totalColunas
                            if tab[viz_lin][viz_col] != BOMBA: #se NÃO é bomba, acrescenta
                                tab[viz_lin][viz_col] += 1


def converter_input(casa: str, tab: list) -> tuple:
    casa = casa.lower().strip()
    #se for < 2, se for > 3 e se a parte depois da letra NÃO FOR só digito -> retorna None
    if len(casa) < 2 or len(casa) > 3 or not casa[1:].isdigit():
        return None
    
    col = ord(casa[0]) - ord('a')
    lin = int(casa[1:]) - 1

    if 0 <= lin < len(tab) and 0 <= col < len(tab[lin]):
        return lin, col

    return None


#uma matriz com as bombas e dicas já sorteadas que o jogador não vê.
#usada para comparação com os inputs do jogador (tab -> gabarito).
#outra matriz toda fechada (no inicio) e que salva as casas abertas pelo jogador. (estado)
# tam_tab = escolher_tamanho()
# gabarito = criar_matriz(tam_tab, 0) #gabarito -> começa tudo 0 (livre)
# estado = criar_matriz(tam_tab, FECHADA) #começa tudo fechado
# estado_teste = criar_matriz(tam_tab, ABERTA)
# qntd_bombas = quantidade_bombas(tam_tab)
# sortear_bombas(gabarito, qntd_bombas, tam_tab)
# calcular_dicas(gabarito)
# print("GABARITO")
# mostrar_matriz(gabarito, estado_teste)
# print()
# mostrar_matriz(gabarito, estado)