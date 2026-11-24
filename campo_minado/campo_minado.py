from random import randint
import time
DEBUG : bool = True
TAMANHOS : list = [0, 9, 16, 30] #posição = opção do menu (a posição 0, "sair", não é usada)
BOMBA : int = -1
FECHADA : int = -10
ABERTA : int = 1
BANDEIRA : int = 100
SEGURA : int = 2 #abriu uma casa sem bomba
EXPLODIU : int = -2 #abriu uma bomba
INVALIDA : int = 20 #casa já aberta ou com bandeira, nada muda
ABRIR : int = 1000
COLOCAR_BANDEIRA : int = 2000
RETIRAR_BANDEIRA : int = 3000

#pergunta o tamanho do tabuleiro e repete até a resposta ser válida
# def escolher_tamanho():
#     tam_tab = input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): ").strip()
#     while not tam_tab.isdecimal() or int(tam_tab) not in [9, 16, 30]: #valida se todos os dígitos são numeros e se está dentro dos permitidos
#         print("Digite um tamanho válido!")
#         tam_tab = input("Digite o tamanho do tabuleiro que quer jogar (9, 16 ou 30): ").strip()
#     return int(tam_tab)


#devolve quantas bombas o modo escolhido tem
def quantidade_bombas(tam_tab: int) -> int:
    qntd_bombas = 99
    if tam_tab == 9:
        qntd_bombas = 10
    elif tam_tab == 16:
        qntd_bombas = 40
    print(f"\nQUANTIDADE DE BOMBAS: {qntd_bombas}\n")
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
                elif tab[linha][coluna] == 0:
                    print(" ", end = " ")
                else:
                    print(tab[linha][coluna], end = " ")
        print()


def mostrar_bombas(tab: list):
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
            if tab[linha][coluna] == BOMBA:
                    print("*", end = " ")
            else:
                print("■", end = " ")
        print()


#coloca as bombas em casas aleatórias de tab
def sortear_bombas(tab: list, qntd_bombas: int, tam_tab: int, casa_escolhida: tuple):
    bombas = 0
    while bombas < qntd_bombas:
        linha_escolhida = casa_escolhida[0]
        coluna_escolhida = casa_escolhida[1]
        linha = randint(0, tam_tab - 1)
        coluna = randint(0, len(tab[linha]) - 1)
        if tab[linha][coluna] == 0 and (linha,coluna) != (casa_escolhida): #casa livre E diferente da primeira jogada
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
    #se for < 2, se for > 3 e se a parte depois da letra NÃO FOR só digito -> retorna None
    if len(casa) < 2 or len(casa) > 3 or not casa[1:].isdecimal():
        return None
    
    col = ord(casa[0]) - ord('a')
    lin = int(casa[1:]) - 1

    if 0 <= lin < len(tab) and 0 <= col < len(tab[lin]):
        return lin, col

    return None


def abrir_casa(casa_escolhida: tuple, gabarito: list, estado: list):
    linha = casa_escolhida[0]
    coluna = casa_escolhida[1]
    
    if estado[linha][coluna] != FECHADA: #está ABERTA ou BANDEIRA
        return INVALIDA
     
    estado[linha][coluna] = ABERTA #abre a casa
    if gabarito[linha][coluna] == BOMBA:
        return EXPLODIU
    return SEGURA


def abrir_vazias(casa_escolhida: tuple, gabarito: list, estado: list):
    linha = casa_escolhida[0]
    coluna = casa_escolhida[1]
    casa_aberta = abrir_casa(casa_escolhida, gabarito, estado)
    if casa_aberta == SEGURA and gabarito[linha][coluna] == 0:
        for lin in range(-1, 2, 1):
            for col in range(-1, 2, 1):
                viz_lin = linha + lin #casa vizinha
                viz_col = coluna + col #casa vizinha
                casa_vizinha = viz_lin, viz_col
                if 0 <= viz_lin < len(gabarito) and 0 <= viz_col < len(gabarito[linha]): #ver se a casa existe. linha é >= 0 e < totalCasas. Coluna >= 0 e < totalColunas
                    abrir_vazias(casa_vizinha, gabarito, estado)
    return casa_aberta


def pedir_casa(gabarito: list, estado: list) -> tuple:
    casa = str(input("\nDigite a casa que quer selecionar (exemplo: A1): ")).lower().strip()
    casa_escolhida = converter_input(casa, gabarito)
    while casa_escolhida == None:
        print("Digite uma casa válida!")
        casa = str(input("\nDigite a casa que quer selecionar (exemplo: A1): ")).lower().strip()
        casa_escolhida = converter_input(casa, gabarito)

    linha = casa_escolhida[0]
    coluna = casa_escolhida[1]
    if estado[linha][coluna] == FECHADA:
        resposta = input("\nQuer <A>brir a casa ou <M>arcar? ").lower().strip()
        while resposta not in ['a', 'm']:
            print("Digite 'a'(abrir casa) ou 'm'(marcar casa)!")
            resposta = input("\nQuer <A>brir a casa ou <M>arcar? ").lower().strip()

        if resposta == 'a':
            return casa_escolhida, ABRIR
        else:
            return casa_escolhida, COLOCAR_BANDEIRA

    elif estado[linha][coluna] == BANDEIRA:
        resposta = input("Casa com bandeira, deseja retirar? [s/n]").lower().strip()
        while resposta not in ['s', 'n']:
            print("Digite 's' ou 'n'!")
            resposta = input("Casa com bandeira, deseja retirar? [s/n]").lower().strip()

        if resposta == 's':
            return casa_escolhida, RETIRAR_BANDEIRA
        else:
            print("Selecione uma nova casa!")
            return pedir_casa(gabarito, estado)
    else: #casa já aberta
        print("Selecione uma nova casa!")
        return pedir_casa(gabarito, estado)
        

def colocar_bandeira(casa_escolhida: tuple, estado: list):
    linha = casa_escolhida[0]
    coluna = casa_escolhida[1]
    estado[linha][coluna] = BANDEIRA


def retirar_bandeira(casa_escolhida: tuple, estado: list):
    linha = casa_escolhida[0]
    coluna = casa_escolhida[1]
    estado[linha][coluna] = FECHADA


def vitoria_abrindo_tudo(gabarito: list, estado: list) -> bool:
    for linha in range(len(gabarito)):
        for coluna in range(len(gabarito[linha])):
            if gabarito[linha][coluna] != BOMBA and estado[linha][coluna] != ABERTA:
                return False
    return True


def vitoria_marcando_bombas(gabarito: list, estado: list) -> bool:
    for linha in range(len(gabarito)):
        for coluna in range(len(gabarito[linha])):
            if (gabarito[linha][coluna] != BOMBA) != (estado[linha][coluna] != BANDEIRA):
                return False
    return True


def checar_vitoria(gabarito: list, estado: list) -> bool:
    return vitoria_abrindo_tudo(gabarito, estado) or vitoria_marcando_bombas(gabarito, estado)


#transforma segundos (float) do time.time() em texto "X min e Y s"
def formatar_tempo(segundos: float) -> str:
    total = int(segundos) #descarta as frações
    minutos = total // 60 #minutos inteiros
    seg = total % 60 #segundos que sobraram
    return f"{minutos} min e {seg} s"


def menu() -> int:
    print("===============================\n")
    print("BEM VINDO AO JOGO CAMPO MINADO\n")
    print("===============================\n")
    time.sleep(1)
    print("Escolha a dificuldade que quer jogar!\n")
    print("OPÇÕES:")
    print("   1. Principiante  (9x9, 10 bombas)")
    print("   2. Intermediário (16x16, 40 bombas)")
    print("   3. Especialista  (30x16, 99 bombas)")
    print("   0. SAIR")
    
    resposta = input("\nDigite sua opção (número): ").strip()
    while not resposta.isdecimal() or int(resposta) not in [0, 1, 2, 3]: 
        print("\nDigite uma opção válida!")
        resposta = input("\nDigite sua opção (número): ").strip()
    return int(resposta)

def jogar(tam_tab: int):
    #uma matriz com as bombas e dicas já sorteadas que o jogador não vê.
    #usada para comparação com os inputs do jogador (tab -> gabarito).
    #outra matriz toda fechada (no inicio) e que salva as casas abertas pelo jogador. (estado)
    ganhou : bool = False
    perdeu : bool = False
    primeira_jogada : bool = True
    jogadas : int = 0
    tempo_jogado = 0
    gabarito = criar_matriz(tam_tab, 0) #gabarito -> começa tudo 0 (livre)
    estado = criar_matriz(tam_tab, FECHADA) #começa tudo fechado
    qntd_bombas = quantidade_bombas(tam_tab)

    print("======= TABULEIRO =======")
    mostrar_matriz(gabarito, estado)
    tempo_inicial = time.time()

    # LOOP JOGO
    while not ganhou and not perdeu:
        casa_escolhida, marcacao = pedir_casa(gabarito, estado)
        if primeira_jogada:
            sortear_bombas(gabarito, qntd_bombas, tam_tab, casa_escolhida)
            calcular_dicas(gabarito)
            primeira_jogada = False

        if DEBUG:
                estado_teste = criar_matriz(tam_tab, ABERTA) #TESTE
                print("======= GABARITO =======")
                mostrar_matriz(gabarito, estado_teste)
                print()

        if marcacao == ABRIR:
            resultado = abrir_vazias(casa_escolhida, gabarito, estado)

            if resultado == SEGURA:
                ganhou = checar_vitoria(gabarito, estado)
                jogadas += 1
                print()
                mostrar_matriz(gabarito, estado)
            elif resultado == EXPLODIU:
                perdeu = True

        elif marcacao == COLOCAR_BANDEIRA:
            colocar_bandeira(casa_escolhida, estado)
            ganhou = checar_vitoria(gabarito, estado)
            mostrar_matriz(gabarito, estado)
            jogadas += 1
        elif marcacao == RETIRAR_BANDEIRA:
            retirar_bandeira(casa_escolhida, estado)
            ganhou = checar_vitoria(gabarito, estado)
            mostrar_matriz(gabarito, estado)
            jogadas += 1

    if perdeu:
        tempo_final = time.time()
        tempo_jogado = tempo_final - tempo_inicial
        print()
        mostrar_bombas(gabarito)
        print("\nVOCÊ EXPLODIU!\n")
        print(f"Você realizou {jogadas} jogadas.\n")
        print(f"Você perdeu em {formatar_tempo(tempo_jogado)}.\n")

    if ganhou:
        tempo_final = time.time()
        tempo_jogado = tempo_final - tempo_inicial
        mostrar_matriz(gabarito, estado)
        if vitoria_abrindo_tudo(gabarito, estado):
            print("\nPARABÉNS, VOCÊ GANHOU ABRINDO TODAS AS CASAS VAZIAS!")
            print(f"Você ganhou em {jogadas} jogadas.\n")
            print(f"Você ganhou em {formatar_tempo(tempo_jogado)}.\n")
        else:
            print("\nPARABÉNS, VOCÊ GANHOU MARCANDO TODAS AS BOMBAS!")
            print(f"Você ganhou em {jogadas} jogadas.\n")
            print(f"Você ganhou em {formatar_tempo(tempo_jogado)}.\n")


opcao = menu()
while opcao != 0:
    jogar(TAMANHOS[opcao])
    time.sleep(3)
    opcao = menu()
print("\nFIM DE JOGO!\n")