import random
temas : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar"]}

# print(temas)
# print(list(temas))
# #print(temas["Animal"])
# print(temas.get("Animal"))

list_temas = list(temas)
tam_temas = len(list_temas)

rand_tema = random.randint(0, tam_temas - 1)
categoria_escolhida = list_temas[rand_tema]
tam_palavras = len(temas[categoria_escolhida])

rand_palavra = random.randint(0, tam_palavras - 1)
palavra_escolhida = temas[categoria_escolhida][rand_palavra]

def gerar_tracinhos(palavra) -> list:
    tracinhos = ["_"] * len(palavra)
    for i in range(len(palavra)):
        if palavra[i] == " " or palavra[i] == "-":
            tracinhos[i] = palavra[i]
    return tracinhos

tracinhos = gerar_tracinhos(palavra_escolhida)
print(f"CATEGORIA SORTEADA: {categoria_escolhida}")
print(f"PALAVRA SORTEADA: {palavra_escolhida}") 
print(tracinhos)