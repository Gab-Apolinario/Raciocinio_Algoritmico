import random
# EX.1: Escreva um programa que imprima todas as possibilidades de que no lançamento de dois dados tenhamos o valor 7 
# como resultado da soma dos valores (empregando um laço duplo, cada um simulando um dos dados). Depois, fazendo o 
# sorteiro randômico de dois dados, mostre os sorteios até alcançar uma soma igual a 7.

def soma_dados() -> None:
    print("Parte 1 - Soma:")
    for i in range(1, 7):
        for j in range(1, 7):
            if (i + j) == 7:
                print(f"Dado Um: {i} | Dado Dois: {j} | Soma = {i + j}") 
                
#soma_dados()

def sorteio_dados() -> None:
    print("Parte 2 - Sorteio:")
    soma_dados : int = 0
    while soma_dados != 7:
        dado_um = random.randint(1, 6)
        dado_dois = random.randint(1, 6)
        soma_dados = dado_um + dado_dois
        print(f"Dado Um: {dado_um} | Dado Dois: {dado_dois} | Soma = {soma_dados}") 

#sorteio_dados()

# EX.2: Elabore um algoritmo que imprima: 
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9

def desenho_dois() -> None:
    for i in range(1, 10): #conta linhas de 1 a 9
        for j in range(1, 10):
            print(j, end = " ")
        print()

#desenho_dois()

# EX.3: Elabore um algoritmo que imprima: 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

def desenho_tres() -> None:
    for i in range(1, 10): #conta linhas de 1 a 9
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

#desenho_tres()

# EX.4: Elabore um algoritmo que imprima: 
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def desenho_quatro() -> None:
    for i in range(1, 10):
        for j in range(9, i - 1, -1):
            print(j, end = " ")
        print()
        
#desenho_quatro()

# EX.5: Elabore um algoritmo que imprima: 
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 0
# 2 3 4 5 6 7 8 9 0 1
# 3 4 5 6 7 8 9 0 1 2
# 4 5 6 7 8 9 0 1 2 3
# 5 6 7 8 9 0 1 2 3 4
# 6 7 8 9 0 1 2 3 4 5
# 7 8 9 0 1 2 3 4 5 6
# 8 9 0 1 2 3 4 5 6 7
# 9 0 1 2 3 4 5 6 7 8

def desenho_cinco() -> None:
    for i in range(0, 10):
        for j in range(0, 10):
            print((i + j) % 10, end = " ")
        print()
        
#desenho_cinco()

# EX.6: Elabore um algoritmo que imprima: 
# x
# 2 x
# 3 3 x
# 4 4 4 x
# 5 5 5 5 x
# 6 6 6 6 6 x

def desenho_seis() -> None:
    for i in range(1, 7):
        for j in range(0, i - 1):
            print(i, end = " ")
        print("x")

#desenho_seis()

# EX.7: Elabore um algoritmo que imprima:
# x 2 3 4 5 6
#   x 3 4 5 6
#     x 4 5 6
#       x 5 6
#         x 6
#           x

def desenho_sete() -> None:
    for i in range(1, 7):
        for j in range(1, 7):
            if j < i:
                print(" ", end = " ")
            elif j == i:
                print("x", end = " ")
            else:
                print(j, end = " ")
        print()
        
#desenho_sete()

# EX.8: Elabore um algoritmo que imprima:
# 1          6
#   2      5
#     3  4
#     3  4
#   2      5
# 1          6

def desenho_oito() -> None:
    for i in range(1, 7):
        for j in range(1, 7):
            if j == i:
                print(j, end = " ")
            else:
                print(" ", end = " ")
        print()
#desenho_oito()

# EX.9: Elabore um algoritmo que imprima:
# - 1 - 3 - 5 - 7
# 0 - 2 - 4 - 6 -
# - 1 - 3 - 5 - 7
# 0 - 2 - 4 - 6 -
# - 1 - 3 - 5 - 7
# 0 - 2 - 4 - 6 -
# - 1 - 3 - 5 - 7

def desenho_nove() -> None:    
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 != 0:
                    print(j, end = " - ")
            elif j % 2 == 0:
                print(j, end = " ")
            else:
                print("-", end = " ")
        print()
        
desenho_nove()

# EX.10: Elabore um algoritmo que imprima:
# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

def desenho_dez() -> None:
    for i in range(0, 9):
        for j in range(9, 0, -1):
            if j > i:
                print((j - i) % 10, end = " ")
            else:
                print(" ", end = " ")
        print()

#desenho_dez()

# EX.11: Elabore um algoritmo que imprima:
# 1

# 1
# 1 2

# 1
# 1 2
# 1 2 3

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# assim por diante, até

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

def desenho_onze() -> None:
    for i in range(1, 10):
        for j in range(1, 10):
            if j <= i:
                print(j, end = " ")
        print()

desenho_onze()