import random

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal", "Mata Atlantica", "Manguezal", "Savana", "Tundra"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar", "Compostagem", "Coleta Seletiva", "Biodiversidade", "Preservacao"],
                'Animal Ameacado': ["Onca-pintada", "Mico-leao-dourado", "Arara-azul", "Tamandua-bandeira", "Lobo-guara", "Ariranha", "Peixe-boi"],
                'Problema Ambiental': ["Desmatamento", "Queimada", "Poluicao", "Aquecimento Global", "Enchente", "Lixo Plastico"]}

VIDAS_MAX : int = 6
vidas : int = VIDAS_MAX
# -------------------------------
# TESTES
# -------------------------------
# print(TEMAS)
# print(list(TEMAS))
# #print(TEMAS["Animal"])
# print(TEMAS.get("Animal"))
# -------------------------------

def escolher_categoria() -> str:
    list_temas = list(TEMAS) # retorna lista com as CHAVES do dict
    tam_temas = len(list_temas) # retorna quantidade de elementos nessa lista de chaves
    rand_tema = random.randint(0, tam_temas - 1) # sorteia um int até o comprimento da lista - 1
    categoria_escolhida = list_temas[rand_tema] # seleciona a sorteada
    # print(f"CATEGORIA SORTEADA: {categoria_escolhida}")    # DEBUG
    return categoria_escolhida


def escolher_palavra(categoria: str) -> str:
    tam_palavras = len(TEMAS[categoria]) # retorna quantidade de elementos na lista dos VALORES da CHAVE escolhida
    rand_palavra = random.randint(0, tam_palavras - 1) # sorteia um int até o comprimento da lista de valores - 1
    palavra_escolhida = TEMAS[categoria][rand_palavra] # seleciona a sorteada
    # print(f"PALAVRA SORTEADA: {palavra_escolhida}")   # DEGUB
    return palavra_escolhida


def gerar_tracinhos(palavra) -> list:
    tracinhos = ["_"] * len(palavra)
    for i in range(len(palavra)):
        if palavra[i] == " " or palavra[i] == "-":
            tracinhos[i] = palavra[i]
    return tracinhos


def mostrar_palavra(categoria: str, tracinhos: list): # printa palavra sem ser em formato de lista
    print(f"CATEGORIA: {categoria}\n")
    print("Palavra: ", end = " ")
    for i in range(len(tracinhos)):
        print(tracinhos[i], end = "")
    print()


def verificar_letra(input_jogador: str, palavra_escolhida: str) -> bool: # retorna se tem ou não a letra
    if input_jogador in palavra_escolhida.lower():
        return True
    else:
        return False


def validar_letra(input_jogador: str) -> bool:
    if input_jogador.isalpha() and len(input_jogador) <= 1:
        return True
    return False


def remover_acento(input_jogador: str) -> str:
    com_acento : str = "áàâãéêíóôõúç"
    sem_acento : str = "aaaaeeiooouc"
    
    if input_jogador in com_acento:
        pos = com_acento.index(input_jogador)
        input_jogador = sem_acento[pos]    
    return input_jogador


def registrar_letra(input_jogador: str, testadas: list) -> None:
    if input_jogador not in testadas:
        testadas.append(input_jogador)


def adicionar_letra(tracinhos: list, palavra_escolhida: str, letra_input: str):
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i].lower() == letra_input:
            tracinhos[i] = palavra_escolhida[i] # retorna letra original para pegar as iniciais maiúsculas


def mostrar_usadas(testadas: list) -> None:
    print("\nLetras já tentadas:", end = " ")
    for i in range(len(testadas)):
        print(testadas[i], end = " - ")


def verificar_vitoria(tracinhos: list) -> bool:
    if "_" not in tracinhos:
        return True
    return False


def verificar_derrota(vidas: int) -> bool:
    if vidas <= 0:
        return True
    return False


# -------------------------------
# LOOP JOGO
# -------------------------------

ganhou : bool = False
perdeu : bool = False

categoria = escolher_categoria()
palavra_escolhida = escolher_palavra(categoria)
tracinhos = gerar_tracinhos(palavra_escolhida)
testadas : list = []

while not ganhou and not perdeu:
    mostrar_palavra(categoria, tracinhos)
    
    input_jogador : str = str(input("Digite uma letra: ").lower())
    while not validar_letra(input_jogador):
        print("Caractere inválido. Por favor digite apenas uma letra.")
        input_jogador : str = str(input("Digite uma letra: ").lower()) 
    
    input_jogador = remover_acento(input_jogador)
        
    print("\n-----------------------------------------")
    if input_jogador in testadas:
        print("\nLetra já verificada anteriormente!")
    else:
        registrar_letra(input_jogador, testadas)
        if verificar_letra(input_jogador, palavra_escolhida):
            adicionar_letra(tracinhos, palavra_escolhida, input_jogador)
        else:
            vidas -= 1
    
    mostrar_usadas(testadas)
    perdeu = verificar_derrota(vidas)
    ganhou = verificar_vitoria(tracinhos)
    print(f"\nVIDAS RESTANTES: {vidas}/{VIDAS_MAX}")

if ganhou:
    print("\nGANHOU")
    print(f"A palavra era: {palavra_escolhida}")
else:
    print("\nPERDEU")
    print(f"A palavra era: {palavra_escolhida}")