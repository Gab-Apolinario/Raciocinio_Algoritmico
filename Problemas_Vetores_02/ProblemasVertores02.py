# EX.1: Crie duas listas com o mesmo tamanho: uma com os nomes de 5 itens de um jogo de aventura (ex.: "espada", "escudo", "poção", "mapa", 
# "tocha" que estão à venda e outra com os respectivos preços. Mostre o catálogo no formato Espada - 50 moedas. Depois, leia a quantidade 
# de moedas do jogador e mostre apenas os itens que ele consegue comprar.

def mostrar_catalogo(itens: list, precos: list) -> None:
    print("\nCatálogo da Loja".upper())
    for i in range(len(itens)):
        print(f"Item: {itens[i]} - {precos[i]} moedas")


def mostrar_compravel(moedas: int, itens: list, precos: list) -> None:
    print("\nItens compráveis".upper())
    for i in range(len(itens)):
        if moedas >= precos[i]:
            print(f"Item: {itens[i]} - {precos[i]} moedas")
        else:
            print(f"Não é possível comprar o item {itens[i]}!")


lista_itens = ["Espada", "Escudo", "Poção", "Mapa", "Tocha"]
lista_precos = [100, 120, 10, 40, 15]
mostrar_catalogo(lista_itens, lista_precos)
moedas = int(input("\nDigite quantas moedas você possui: "))
mostrar_compravel(moedas, lista_itens, lista_precos)


# EX.3: Leia 8 itens coletados por um jogador (um por vez) e guarde-os numa lista. Depois, peça o nome de um item e informe:
# - se o jogador possui esse item (usando in)
# - quantas unidades dele foram coletadas (usando count)

def itens_coletados() -> None:
    lista_itens : list = []
    while len(lista_itens) < 8:
        item_coletado : str = str(input("Digite o item coletado: "))
        lista_itens.append(item_coletado)

    print("Itens Coletados:")
    for item in lista_itens:
        print(f"  -> {item}")

    item = input("Qual item quer procurar? ")
    if item in lista_itens:
        qntd = lista_itens.count(item) #conta quantidade do item
        print(f"Você coletou {qntd} do item {item}")
    else:
        print(f"Infelizmente, você não coletou o item {item}")


#itens_coletados()

# EX.5: Um aventureiro carrega no máximo 50 kg. Leia o nome e o peso de itens, um a um, e guarde em duas listas paralelas. Quando um item 
# novo ultrapassar o limite, recuse-o e encerre a leitura. Crie a função analisar_mochila(nomes, pesos), que devolve uma tupla com o 
# peso total e o nome do item mais pesado. Mostre o inventário final.

capacidade_max = 50
soma_peso = 0
nomes_itens = []
pesos_itens = []

while sum(pesos_itens) < 50:
    nomes_itens.append(str(input("Digite o nome do item: ")))
    pesos_itens.append(str(input("Digite o peso do item: ")))

def item_mais_pesado(pesos):
    for i in range(len(pesos_itens)):
        
        
def analisar_mochila(nomes: list, pesos: list) -> tuple:
    
    return sum(pesos_itens), item_mais_pesado