import random

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal", "Mata Atlantica", "Manguezal", "Savana", "Tundra"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar", "Compostagem", "Coleta Seletiva", "Biodiversidade", "Preservacao"],
                'Animal Ameacado': ["Onca-pintada", "Mico-leao-dourado", "Arara-azul", "Tamandua-bandeira", "Lobo-guara", "Ariranha", "Peixe-boi"],
                'Problema Ambiental': ["Desmatamento", "Queimada", "Poluicao", "Aquecimento Global", "Enchente", "Lixo Plastico"]}

vidas : int = 6

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


def mostrar_palavra(tracinhos: list): # printa palavra sem ser em formato de lista
    print(f"CATEGORIA: {categoria}")
    print()
    print("Palavra: ", end = " ")
    for i in range(len(tracinhos)):
        print(tracinhos[i], end = "")
    print()


def verificar_letra(input_jogador: str, palavra_escolhida: str) -> bool: # retorna se tem ou não a letra
    if input_jogador.lower() in palavra_escolhida.lower():
        return True
    else:
        return False


def adicionar_letra(tracinhos: list, palavra_escolhida: str, letra_input: str):
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i].lower() == letra_input.lower():
            tracinhos[i] = palavra_escolhida[i] # retorna letra original para pegar as iniciais maiúsculas


# -------------------------------
# LOOP JOGO
# -------------------------------

ganhou : bool = False
perdeu : bool = False

categoria = escolher_categoria()
palavra_escolhida = escolher_palavra(categoria)
tracinhos = gerar_tracinhos(palavra_escolhida)
while not ganhou and not perdeu:
    mostrar_palavra(tracinhos)
    input_jogador : str = str(input("Digite uma letra: "))    

    # Verificação de Estado
    if verificar_letra(input_jogador, palavra_escolhida):
        adicionar_letra(tracinhos, palavra_escolhida, input_jogador)
    else:
        vidas -= 1
        if vidas <= 0:
            perdeu = True
        else:
            print(f"\nVidas Restantes: {vidas}\n")
    
    if "_" not in tracinhos:
        ganhou = True

if ganhou:
    print("\nGANHOU")
    print(f"A palavra era: {palavra_escolhida}")
else:
    print("\nPERDEU")
    print(f"A palavra era: {palavra_escolhida}")