import random
import math

# EX.1: Um jogador começa no nível 1 e ganha 3 pontos de habilidade a cada partida, enquanto um NPC rival começa no 
# nível 5 e ganha 1 ponto por partida. Escreva um algoritmo que calcule quantas partidas serão necessárias até o jogador 
# ultrapassar o NPC.

def partidas_ate_ultrapassar() -> None:
    nivel_jogador : int = 1
    nivel_npc : int = 5
    partidas_jogadas : int = 0
    print("Jogo iniciado!")
    print(f"Partidas Jogadas: {partidas_jogadas} | Nível Jogador: {nivel_jogador} | Nível NPC: {nivel_npc}")
    
    while nivel_jogador <= nivel_npc:
        nivel_jogador += 3
        nivel_npc += 1
        partidas_jogadas += 1
        print(f"Partidas Jogadas: {partidas_jogadas} | Nível Jogador: {nivel_jogador} | Nível NPC: {nivel_npc}")

    print("Jogador passou nível do NPC!")

#partidas_ate_ultrapassar()

# EX.2: Crie um algoritmo que calcule a divisão inteira de dois números fornecidos pelo usuário, a por b,
# através de subtrações sucessivas. Mostre o resultado do quociente (o div) e do resto (o mod).

def divisao_inteira(numA: int, numB: int) -> None:
    resto : int = numA
    quociente : int = 0 #quantas vezes conseguimos subtrair o numB do numA
    while resto >= numB:
        resto -= numB
        quociente += 1
    print(f"Divisão inteira de {numA} por {numB} = {quociente} | Resto = {resto}")
    
# numA : int = int(input("Digite o dividendo (inteiro): "))
# numB : int = int(input("Digite o divisor (inteiro): "))
# divisao_inteira(numA, numB)

# EX.3: Elabore um algoritmo que leia o dano de n ataques realizados numa partida, 
# sendo n informado pelo jogador. Mostre qual foi o ataque mais forte e o mais fraco.

def class_ataque(n: int) -> None:
    dano = int(input("Digite o dano do ataque (inteiro)"))
    maior : int = dano
    menor : int = dano
    for i in range(0, n - 1, 1):
        dano = int(input("Digite o dano do ataque (inteiro)"))
        if dano < menor:
            menor = dano
        if dano > maior:
            maior = dano
    print(f"Ataque mais forte: {maior}")
    print(f"Ataque mais fraco: {menor}")
    
# n : int = int(input("Digite quantos ataques foram realizados (inteiro): "))
# class_ataque(n)

# EX.4: Leia 10 valores de dano causado por um jogador. Mostre a média apenas dos ataques 
# considerados críticos. Todo dano ímpar é considerado crítico.

def media_critico() -> None:
    soma : int = 0
    ataques_critico : int = 0
    for i in range(1, 11, 1):
        dano = int(input("Digite o dano do ataque (inteiro): "))
        if (dano % 2) != 0: #impar = crítico
            print(f"Dano {i}: {dano} -> Ataque Crítico!")
            soma += dano
            ataques_critico += 1
        else:
            print(f"Dano {i}: {dano} -> Ataque Normal!")
    
    if ataques_critico != 0:
        media_criticos = soma / ataques_critico
        print(f"Média dos Ataques Críticos: {media_criticos}")
    else:
        print(f"Não teve Ataques Críticos!")
    
#media_critico()

# EX.5: Leia uma sequência de itens coletados (valores positivos = power-ups, negativos = armadilhas)
# e só termine a leitura quando o jogador tiver coletado 3 power-ups. Informe qual foi o 
# power-up de maior valor.

# Usa random.randint() em vez de input() propositalmente, aproveitei pra praticar automação/simulação
# de dados em vez de digitar manualmente a cada teste.

def sistema_power_ups() -> None:
    power_ups : int = 0
    tentativas : int = 0
    maior_power_up = 0
    while power_ups < 3:
        item_coletado = random.randint(-10, 10)
        print(f"Item coletado: {item_coletado}")
        if item_coletado < 0:
            print("Armadilha!")
        else:
            print("Power Up!")
            if item_coletado > maior_power_up:
                maior_power_up = item_coletado
            power_ups += 1
        tentativas += 1
    
    print(f"3 Power Ups Coletados! | Maior Power Up: {maior_power_up} | Tentativas Necessárias: {tentativas}")
    
#sistema_power_ups()

# EX.6: Leia uma sequência de danos de golpes em combo e só termine quando aparecer uma sequência
# de 3 golpes em ordem crescente de dano (combo perfeito). Mostre a média desses 3 golpes finais.

def combo_perfeito():
    soma : int = 0
    dano_anterior : int = 0
    golpes_combo : int = 0
    while golpes_combo < 3:
        dano = random.randint(1, 10) #randomiza
        print(f"Dano do golpe: {dano}")
        if dano > dano_anterior: #valida
            dano_anterior = dano #guarda
            golpes_combo += 1
            soma += dano
        else: #não é crescente a ordem
            dano_anterior = dano
            golpes_combo = 1
            soma = dano
        
    print(f"Combo Perfeito! Golpes: {golpes_combo} | Soma: {soma} | Média: {soma/golpes_combo:.2f}")
            
#combo_perfeito()

# EX.7: O número de inimigos por onda segue uma progressão do tipo Fibonacci (1, 1, 2, 3, 5, 8, 13...).
# Mostre quantos inimigos aparecem em cada onda enquanto o total for menor que 500.

def inimigos_fibonacci() -> None:
    num = 1
    inimigos_total : int = 1
    onda_ultima : int = 0
    onda_penultima : int = 1
    proximo_termo : int = 0
    while inimigos_total < 500:
        proximo_termo = onda_ultima + onda_penultima
        onda_ultima, onda_penultima = proximo_termo, onda_ultima
        inimigos_total += proximo_termo
        print(f"Onda: {num} Inimigos: {proximo_termo}")
        num += 1
        
#inimigos_fibonacci()

# EX.8: Um mago tem 200 pontos de mana. Cada feitiço lançado consome uma quantidade de mana informada pelo 
# usuário. Elabore um algoritmo que leia o custo de cada feitiço lançado e pare automaticamente quando a mana não 
# for mais suficiente para o próximo feitiço, informando quantos feitiços foram lançados e quanta mana sobrou

def mana_mago() -> None:
    mana : int = 200
    feiticos_lancados : int = 0
    mana_suficiente : bool = True
    while mana_suficiente:
        custo_feitico = int(input("Digite o custo do feitiço (inteiro): "))
        if mana >= custo_feitico:
            mana -= custo_feitico
            feiticos_lancados += 1
            print(f"Feitiço Lançado! Mana Restante: {mana}")
        else:
            mana_suficiente = False

    print(f"Não possui mana suficiente! | Feitiços Lançados: {feiticos_lancados} | Mana restante: {mana}")

#mana_mago()

# EX.9: A série de Ricci difere da série de Fibonacci (1, 1, 2, 3, 5, ...) porque os dois primeiros termos podem ser definidos 
#pelo usuário. Imprima os n primeiros termos da série de Ricci, sendo que n e o valor dos dois primeiros termos são 
#fornecidos pelo usuário.

def serie_ricci(qntd_termos: int, termoA: int, termoB: int) -> None:
    num = 2
    proximo_termo: int = 0
    if qntd_termos == 1:
        print(f"1o. termo = {termoA}")
    elif qntd_termos <= 0:
        print("Quantidade de termos inválida!")
        return
    else:
        print(f"1o. termo = {termoA}")
        print(f"2o. termo = {termoB}")
    while num < qntd_termos:
        proximo_termo = termoA + termoB
        termoB, termoA = proximo_termo, termoB
        print(f"{num+1}o. termo = {proximo_termo}")
        num += 1
    
# qntd_termos: int = int(input("Digite a quantidade de termos da série Ricci (inteiro): "))
# termoA: int = int(input("Digite o valor do primeiro termo (inteiro): "))
# termoB: int = int(input("Digite o valor do segundo termo (inteiro): "))
#serie_ricci(qntd_termos, termoA, termoB)

# EX.10: A série de Fetuccine difere da série de Ricci porque o termo de posição par é resultado da subtração dos dois 
# anteriores.  Os  termos  ímpares  continuam  sendo  resultado  da  soma  dos  dois  elementos  anteriores.  Imprima  os  n 
# primeiros termos da série de Fetuccine, sendo que n e o valor dos dois primeiros termos são fornecidos pelo usuário.

def serie_fetuccine(qntd_termos: int, termoA: int, termoB: int) -> None:
    num = 2
    proximo_termo: int = 0
    if qntd_termos == 1:
        print(f"1o. termo = {termoA}")
    elif qntd_termos <= 0:
        print("Quantidade de termos inválida!")
        return
    else:
        print(f"1o. termo = {termoA}")
        print(f"2o. termo = {termoB}")
    
    while num < qntd_termos:
        if (num + 1) % 2 == 0: #termo par
            proximo_termo = termoB - termoA
            termoB, termoA = proximo_termo, termoB
            print(f"{num+1}o. termo = {proximo_termo}")
        else: #termo ímpar
            proximo_termo = termoA + termoB
            termoB, termoA = proximo_termo, termoB
            print(f"{num+1}o. termo = {proximo_termo}")
        num += 1
        
#serie_fetuccine(qntd_termos, termoA, termoB)

# EX.11: Elabore um algoritmo que calcule o valor de S, em que: 
#S = 1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + ... – 10/100

def serie_s() -> None:
    s = 0
    for i in range(1, 11, 1):
        if i % 2 == 0:
            s -= i / pow(i, 2)
        else:
            s += i / pow(i, 2)
            
    print(s)

#serie_s()

# EX.12: Elabore um algoritmo que o valor da série S abaixo, sendo que o valor inteiro de n é fornecido pelo usuário.
# S = 1/3 + 3/6 + 5/9 + 7/12 + ... + (2n - 1)/3n

def serie_S(n: int) -> None:
    s = 0
    
    for i in range(1, n+1):
        num = 2 * i - 1
        den = 3 * i
        termo = num/den
        s = s + termo
        print(f"{i}o. termo =  {num}/{den} = {termo:.2f}")
        print(f"Série até agora = {s:.2f}\n")
 
#n : int = int(input("Digite quantos termos (inteiro): "))
#serie_S(n)

# EX.13: O valor de π pode ser calculado usando como base a seguinte série:
# S = 1 - 1/3³ + 1/5³ - 1/7³ + 1/9³ - ... +-?
# Sendo, π = cbrt(S * 32) Elabore um algoritmo que calcule e mostre o valor 
# de π com base em uma série S de 50 termos.

def valor_pi() -> None:
    s = 0
    for i in range(1, 51, 1):
        den = pow(2 * i - 1, 3)
        if i % 2 == 0:
            s -= 1/den
        else:
            s += 1/den

    pi = math.cbrt(s * 32)
    print(pi)
    
valor_pi()