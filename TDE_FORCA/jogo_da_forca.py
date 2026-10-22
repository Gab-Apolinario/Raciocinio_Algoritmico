import random

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar"]}

vidas : int = 6

# -------------------------------
# TESTES
# -------------------------------
# print(TEMAS)
# print(list(TEMAS))
# #print(TEMAS["Animal"])
# print(TEMAS.get("Animal"))
# -------------------------------

list_temas = list(TEMAS) #retorna lista com as CHAVES do dict
tam_temas = len(list_temas) #retorna quantidade de elementos nessa lista de chaves

rand_tema = random.randint(0, tam_temas - 1) #sorteia um int até o comprimento da lista - 1
categoria_escolhida = list_temas[rand_tema] #seleciona a sorteada
tam_palavras = len(TEMAS[categoria_escolhida]) #retorna quantidade de elementos na lista dos VALORES da CHAVE escolhida

rand_palavra = random.randint(0, tam_palavras - 1) #sorteia um int até o comprimento da lista de valores - 1
palavra_escolhida = TEMAS[categoria_escolhida][rand_palavra] #seleciona a sorteada

def gerar_tracinhos(palavra) -> list:
    tracinhos = ["_"] * len(palavra)
    for i in range(len(palavra)):
        if palavra[i] == " " or palavra[i] == "-":
            tracinhos[i] = palavra[i]
    return tracinhos


def mostrar_palavra(tracinhos: list): #printa palavra sem ser em formato de lista
    for i in range(len(tracinhos)):
        print(tracinhos[i], end = "")
    print()


def verificar_letra(input_jogador: str, palavra_escolhida: str) -> bool: #retorna se tem ou não a letra
    if input_jogador.lower() in palavra_escolhida.lower():
        print("tem letra") #teste, não aparece no jogo principal pois é chamado num if
        return True
    else:
        print("não tem letra") #teste, não aparece no jogo principal pois é chamado num if
        return False


def adicionar_letra(tracinhos: list, palavra_escolhida: str, letra_input: str):
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i].lower() == letra_input.lower():
            tracinhos[i] = palavra_escolhida[i] #retorna letra original para pegar as iniciais maiúsculas


tracinhos = gerar_tracinhos(palavra_escolhida)
print(f"CATEGORIA SORTEADA: {categoria_escolhida}")
print(f"PALAVRA SORTEADA: {palavra_escolhida}")
mostrar_palavra(tracinhos)
input_jogador : str = str(input("Digite uma letra: "))

if verificar_letra(input_jogador, palavra_escolhida):
    adicionar_letra(tracinhos, palavra_escolhida, input_jogador)
else:
    vidas -= 1
    print(f"Vidas Restantes: {vidas}")
mostrar_palavra(tracinhos)