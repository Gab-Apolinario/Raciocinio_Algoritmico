import random

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar"]}

VIDAS : int = 6

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


def verificar_letra(letra_input: str) -> bool: #retorna se tem ou não a letra
    if input_jogador.lower() in palavra_escolhida:
        print("tem letra")
        return True
    else:
        print("não tem letra")
        return False


tracinhos = gerar_tracinhos(palavra_escolhida)
print(f"CATEGORIA SORTEADA: {categoria_escolhida}")
print(f"PALAVRA SORTEADA: {palavra_escolhida}")
mostrar_palavra(tracinhos)
print("teste")
input_jogador : str = str(input("Digite uma letra: "))
verificar_letra(input_jogador)