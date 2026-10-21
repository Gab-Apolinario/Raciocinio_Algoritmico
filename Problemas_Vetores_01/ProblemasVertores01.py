# EX.1: Desenvolva uma função chamada ler_vetor que recebe a quantidade de elementos de um vetor, cria, lê 
# e retorna este vetor. No programa principal, came a função e mostre o vetor lido.
tamanho_vetor : int = int(input("Digite o tamanho desejado do seu vetor: "))
def ler_vetor(elementos: int) -> list:
    vetor : list = [0] * elementos
    print(f"\nVocê deve digitar {elementos} números:")
    
    for i in range(elementos):
        vetor[i] = int(input(f"   >> Digite o {i + 1}o. valor: "))

    return vetor


v = ler_vetor(tamanho_vetor)
print(f"\nVetor Criado: {v}\n")

# EX.2: Adicione ao script anterior uma função chamada calcular_soma que recebe um vetor de números inteiros 
# e devolve a soma de seus valores. Adicione o uso deste função ao programa principal.

def calcular_soma(vetor: list) -> int:
    soma : int = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma


soma = calcular_soma(v)
print(f"A soma do vetor {v} é {soma}")

# EX.3: Adicione ao script anterior uma função chamada calcular_media que recebe um vetor de números inteiros 
# e devolve a média de seus valores. Esta função deve usar a função calcular_soma já elaborada acima. Adicione o uso
# dessa função no programa principal.

def calcular_media(vetor : list) -> float:
    media : float = calcular_soma(vetor) / len(vetor)
    return media


media = calcular_media(v)
print(f"A média do vetor {v} é {media}")

# EX.4: Adicione ao script anterior uma função chamada calcular_menor que recebe um vetor de números inteiros 
# e devolve o valor do seu menor número. Adicione o uso dessa função ao programa principal.

def calcular_menor(vetor: list) -> int:
    menor = vetor[0]
    for i in range(1, len(vetor)): #começa em 1 pq o [0] já foi usado antes
        if vetor[i] < menor:
            menor = vetor[i]
    return menor


menor_valor = calcular_menor(v)
print(f"O menor valor do vetor {v} é {menor_valor}")

# EX.5: Adicione ao script anterior uma função chamada calcular_maior que recebe um vetor de números inteiros 
# e devolve o valor do seu maior número. Adicione o uso dessa função ao programa principal.

def calcular_maior(vetor: list) -> int:
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior


maior_valor = calcular_maior(v)
print(f"O maior valor do vetor {v} é {maior_valor}")

# #X.6: Adicione ao script anterior uma função chamada existe_numero que recebe um vetor de números inteiros e um número
# a ser pesquisado. A função devolve true ou false se este número existe ou não no vetor. Adicione o uso desta função
# ao programa principal.

def existe_numero(vetor: list, pesquisar: int) -> bool:
    for i in range(len(vetor)):
        if vetor[i] == pesquisar:
            return True
    return False


pesquisar : int = int(input("\nQual número você quer pesquisar no vetor: "))
existe_num = existe_numero(v, pesquisar)
print(f"O número {pesquisar} está no vetor: {existe_num}")

# EX.7: Adicione ao script anterior uma função chamada posicao_numero que recebe um vetor de números inteiros e um número
# a ser pesquisado. A função devolve a posição da primeira ocorrência deste número no vetor (se não encontrar retorna '-1').
# Adicione o uso desta função ao programa principal dentro de um bloco if que testou se ele existe 
# usando a função existe_numero.

def posicao_numero(vetor: list, pesquisar: int) -> None:
    for i in range(len(vetor)):
        if vetor[i] == pesquisar:
            return vetor[i]


if existe_num:
    pos_num = posicao_numero(v, pesquisar)
    print(f"O número {pesquisar} está na posição {pos_num}")

# EX.8: Adicione ao script anterior uma função chamada multiplicar_numero que recebe um vetor de números inteiros e um
# valor inteiro para multiplicar num. A função devolve um novo vetor, com cada valor do vetor original multiplicado
# pelo num(multiplicação por escalar). Adicione o uso da função ao programa principal.

def multiplicar_numero(vetor: list, num : int) -> None:
    vetor_multiplicado = [0] * len(vetor)
    for i in range(len(vetor)):
        vetor_multiplicado[i] = vetor[i] * num
    return vetor_multiplicado


multiplicador : int = int(input("\nDigite um número inteiro para multiplicar cada valor do vetor: "))
mul_num = multiplicar_numero(v, multiplicador)
print(f"Vetor multiplicado pelo número {multiplicador}: {mul_num}")

# EX.9: Adicione ao script anterior uma função chamada vetor_ao_quadrado que recebe um vetor de números inteiros
# e devolve um novo vetor, com cada valor do vetor original elevado ao quadrado. Adicione o uuso desta função ao programa principal.
import math
def vetor_ao_quadrado(vetor: list) -> list:
    vetor_sqrt : list = [0] * len(vetor)
    for i in range(len(vetor)):
        vetor_sqrt[i] = math.pow(vetor[i], 2)
    return vetor_sqrt


vetor_quadrado = vetor_ao_quadrado(v)
print(f"Vetor ao quadrado: {vetor_quadrado}")

# EX.10: Adicione ao script anterior uma função chamada contar_sinais que recebe um vetor de números inteiros
# e devolve uma TUPLA contendo a quantidade de números negativos, a quantidade de zeros e a quantidade de números
# positivos. Adicione o uso desta função ao programa principal.

def contar_sinais(vetor: list) -> tuple:
    negativo = 0
    nulo = 0
    positivo = 0
    
    for i in range(len(vetor)):
        if vetor[i] < 0:
            negativo += 1
        elif vetor[i] > 0:
            positivo += 1
        else:
            nulo += 1
            
    return negativo, nulo, positivo


sinais = contar_sinais(v)
print(f"\nTupla com (negativos, nulos, positivos): {sinais}")
print(f"Negativos: {sinais[0]} | Nulos: {sinais[1]} | Positivos: {sinais[2]}")

# EX.11: Adicione ao script anterior uma função chamada contar_paridade que recebe um vetor de números inteiros e devolve
# uma tupla contendo a quantidade de números ímpares e quantidade de números pares. Adicione o uso desta função ao
# programa principal.

def contar_paridade(vetor: list) -> tuple:
    pares : int = 0
    pares_list = []
    impares : int = 0
    impares_list = []
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            pares += 1
            pares_list.append(vetor[i])
        else:
            impares += 1
            impares_list.append(vetor[i])
    return impares, pares #impares_list, pares_list (retorna os valores em formato de lista)


paridades : tuple = contar_paridade(v)
print(f"As quantidade de ímpares e pares do vetor são: {paridades}")

# EX.12.: Adicione ao script anterior uma função chamada contar_media que recebe um vetor de números inteiros e devolve
# uma tupla contendo a quantidade de números menores, iguais ou superiores a média aritmética do conjunto (calculada usando
# a função calcular_media). Adicione o uso desta função ao programa principal.

def contar_media(vetor: list) -> tuple:
    menores_media : int = 0
    iguais_media : int = 0
    maiores_media : int = 0
    media = calcular_media(vetor)
    for i in range(len(vetor)):
        if vetor[i] < media:
            menores_media += 1
        elif vetor[i] > media:
            maiores_media += 1
        else:
            iguais_media += 1
    return menores_media, iguais_media, maiores_media


tupla_media = contar_media(v)
print(f"Contagem dos valores menores, iguais e maiores que a média do vetor: {tupla_media}")