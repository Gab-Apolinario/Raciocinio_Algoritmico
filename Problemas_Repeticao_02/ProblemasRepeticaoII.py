import random

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
    
    print(f"3 Power Ups Coletados! Maior Power Up: {maior_power_up} Tentativas Necessárias: {tentativas}")
    
#sistema_power_ups()


# EX.12: Elabore um algoritmo que o valor da série S abaixo, sendo que o valor inteiro de n é fornecido pelo usuário.
# S = 1/3 + 3/6 + 5/9 + 7/12 + ... + (2n - 1)/3n

def serie_S(n: int) -> None:
    s = 0
    
    for i in range(1, n+1):
        num = 2*i - 1
        den = 3*i
        termo = num/den
        s = s + termo
        print(f"{i}o. termo =  {num}/{den} = {termo:.2f}")
        print(f"Série até agora = {s:.2f}\n")
 
#n : int = int(input("Digite quantos termos (inteiro): "))
#serie_S(n)