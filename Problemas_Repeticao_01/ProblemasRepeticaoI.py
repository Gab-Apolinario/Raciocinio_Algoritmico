import math

# EX.1: Imprima os números de 1 até 99, com incremento de 2.
# Exemplo: 1, 3, 5.....97, 99

#WHILE
def impares_while() -> None:
    num = 1 #inicialização da variável de controle
    print("Usando While: ")
    while num <= 99: #condição de continuidade do loop
        print(num, end = " - ")
        num += 2 #incremento do contador
        
# impares_while()

#FOR
# for i in range(INICIO, CONDICAO, PASSO)
# INICIO é primeiro valor da variável de controle
# CONDICAO é um limite ACIMA do valor
# PASSO é o pulo, o incremento da variável a cada iteração

def impares_for() -> None:
    print("\n\nUsando For: ")
    for i in range(1, 100, 2): 
        print(i , end = "  ")
        
# impares_for()

# EX.2: Imprima os números de 50 até 0 com decremento de 5.  
# Exemplo: 50, 45, 40.....5, 0

def decrescente_while() -> None:
    num = 50
    print("Usando While:")
    while (num >= 0):
        print(num, end = " ")
        num -= 5
    
#decrescente_while()

def decrescente_for() -> None:
    print("\n\nUsando For: ")
    for i in range(50, -1, -5):
        print(i, end = " ")

#decrescente_for()
       
# EX.3: Imprima os números de -100 até 100, com incremento de 10.  
# Exemplo: -100, -90, -80.....90, 100

def crescente_while() -> None:
    num = -100
    print("Usando While:")
    while (num <= 100):
        print(num, end = " ")
        num += 10
        
# crescente_while()

def crescente_for() -> None:
    print("\n\nUsando For: ")
    for i in range(-100, 101, 10):
        print(i, end = " ")

# crescente_for()

# EX.4: Imprima os números múltiplos de 4 existentes no intervalo aberto ]1, 100[

def multiplos_quatro_while() -> None:
    num = 4
    print("Usando While:")
    while (num < 100):
        print(num, end = " ")
        num += 4

#multiplos_quatro_while()

def multiplos_quatro_for() -> None:
    print("\n\nUsando For: ")
    for i in range(4, 100, 4):
        print(i, end = " ")
        
#multiplos_quatro_for()

# Ex.5: Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário. Intervalo fechado [1, n]

def num_impares_while(n: int) -> None:
    num = 1
    print("Usando While:")
    print(f"Ímpares de 1 até {n}: ")
    while (num <= n):
        resto_impar = num % 2
        if resto_impar != 0:
            print(num, end = " ")
        num += 1
        
#n : int = int(input("Digite um número máximo (inteiro): "))
#num_impares_while(n)

def num_impares_for(n: int) -> None:
    print("\n\nUsando For:")
    print(f"Ímpares de 1 até {n}: ")
    for i in range(1, n + 1, 1):
        if (i % 2) != 0:
            print(i, end = " ")
            
#n : int = int(input("Digite um número máximo (inteiro): "))
#num_impares_for(n)
    
# EX.6: Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas.  
# A conversão entre estas duas unidades é dada por:  polegada = centímetro × 2,54

def polegada_centimetros_while() -> None:
    print("Usando While:")
    num = 1
    while (num <= 20):
        cm = num * 2.54
        print(f"{num} polegadas = {cm} centímetros")
        num += 1
        
# polegada_centimetros_while()

def polegada_centimetros_for() -> None:
    print("\n\nUsando For:")
    for i in range(1, 21, 1):
        cm = i * 2.54
        print(f"{i} polegadas = {cm} centímetros")

# polegada_centimetros_for()
    
# EX.7: Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela de conversão
# de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 kilômetros.

def conversao_milhas_while() -> None:
    print("Usando While: ")
    km = 20 
    while (km <= 160):
        milhas = (km * 1000) / 1609.34 #transforma kms em metros e depois em milhas
        print(f" Kilometros: {km} | Milhas: {milhas:.2f}")
        km += 10
        
#conversao_milhas_while()

def conversao_milhas_for() -> None:
    print("\nUsando For: ")
    for km in range(20, 161, 10):
        milhas = (km * 1000) / 1609.34 #transforma kms em metros e depois em milhas
        print(f" Kilometros: {km} | Milhas: {milhas:.2f}")
        
#conversao_milhas_for()

# EX.8: Elabore um algoritmo que leia um conjunto de 10 números inteiros.
# Mostre então qual o valor da soma e da média aritmética do conjunto.

def soma_media_while() -> None:
    print("Usando While:")
    num = 0
    soma = 0
    while (num < 10):
        soma += int(input("Digite um inteiro: "))
        num += 1
    
    media = soma / num
    print(f"Soma dos valores: {soma} | Média dos valores: {media:.2f}")
    
#soma_media_while()

def soma_media_for() -> None:
    print("\n\nUsando For:")
    soma = 0
    valor_media = 0
    for i in range(0, 10, 1):
        soma += int(input("Digite um inteiro: "))
        valor_media += 1
    media = soma / valor_media
    print(f"Soma dos valores: {soma} | Média dos valores: {media:.2f}")

#soma_media_for()

# EX.9:  Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os valores inteiros de li e lf devem 
# ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto: ]li, lf[
    
def multiplos_tres_while(li: int, lf: int) -> None:
    if li > lf:
        print("Valor inválido!")
    else:
        print("Usando While: ")
        num = li + 1
        while (num < lf):
            multiplo_tres = num % 3
            if multiplo_tres == 0:
                print(num, end = " ")
                
            num += 1

#li : int = int(input("Digite um número inteiro: "))
#lf : int = int(input("Digite um número inteiro maior que o anteior: "))
#multiplos_tres_while(li, lf)

def multiplos_tres_for(li: int, lf: int) -> None:
    if li > lf:
        print("Valor inválido!")
    else:
        print("\n\nUsando For:")
        for i in range(li + 1, lf, 1):
            multiplo_tres = i % 3
            if multiplo_tres == 0:
                print(i, end = " ")
                
#li : int = int(input("Digite um número inteiro: "))
#lf : int = int(input("Digite um número inteiro maior que o anteior: "))
#multiplos_tres_for(li, lf)

# EX.10: Faça um algoritmo que mostre o resultado da função de Babbage f(x) = x² + x + 41 
# (polinômio que gera apenas números primos), variando x de 0 até 20.

def funcao_babbage_while() -> None:
    print("Usando While:")
    num = 0
    while (num <= 20):
        babbage = pow(num, 2) + num + 41
        print(f"f({num}) = {babbage}", end = " | ")
        num += 1

#funcao_babbage_while()

def funcao_babbage_for() -> None:
    print("\n\nUsando For:")
    for i in range(0, 21, 1):
        babbage = pow(i, 2) + i + 41
        print(f"f({i}) = {babbage}", end = " | ")
        
#funcao_babbage_for()

# EX.11: Considerando que a conversão de graus Celsius (°C) para graus Fahrenheit (°F)
# é dada pela seguinte fórmula: °F = °C × 1,8 + 32
# Elabore um algoritmo que leia uma temperatura (T) em graus Celsius e mostre as conversões de 
# temperatura para graus Fahrenheit em uma escala que vai de T-10 até T+10, de 1 em 1 grau.  

def celsius_fahrenheit_while(temp_celsius : float) -> None:
    print("Usando While:")
    num = temp_celsius - 10
    while (num <= temp_celsius + 10):
        fahr = num * 1.8 + 32
        print(f"Temperatura em Celsius: {num} | Fahrenheit: {fahr:.2f}")
        num += 1
#temp_celsius : float = float(input("Digite uma temperatura em celsius: "))
#celsius_fahrenheit_while(temp_celsius)

def celsius_fahrenheit_for(temp_celsius : float) -> None:
    print("\n\nUsando For:")
    for i in range(int(temp_celsius - 10), int(temp_celsius + 11), 1):
        fahr = i * 1.8 + 32
        print(f"Temperatura em Celsius: {i} | Fahrenheit: {fahr:.2f}")

#celsius_fahrenheit_for(temp_celsius)

# EX.12: 

def funcao_harmonica_while(n: int) -> None:
    print("Usando While:")
    k = 1
    harm = 0
    while (k <= n):
        harm += 1 / k
        k += 1
    print(f"{harm:.2f}")
        
#n : int = int(input("Digite um número inteiro: "))
#funcao_harmonica_while(n)

def funcao_harmonica_for(n: int) -> None:
    print("\n\nUsando For:")
    harm = 0
    for i in range(1, n + 1, 1):
        harm += 1 / i
    print(f"{harm:.2f}")

#funcao_harmonica_for(n)

# EX.13: Elabore um algoritmo que calcule o valor da série S abaixo,
# sendo que o valor inteiro de n é fornecido pelo usuário.
# s = 1/sqrt(3) + 2/sqrt(4) + 3/sqrt(5) + ... + n/sqrt(n + 2)

def serie_s_while(n: int) -> None:
    print("Usando While:")
    num = 1
    s = 0
    while(num <= n):
        s += num/math.sqrt(num + 2)
        num += 1    
    print(f"{s:.2f}")
    
#n : int = int(input("Digite um número inteiro: "))
#serie_s_while(n)

def serie_s_for(n: int) -> None:
    print("\nUsando For:")
    s = 0
    for i in range(1, n + 1, 1):
        s += i/math.sqrt(i + 2)
    print(f"{s:.2f}")

#serie_s_for(n)