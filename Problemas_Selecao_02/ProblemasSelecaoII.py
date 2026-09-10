#EX.1: Elabore uma algoritmo que leia uma temperatura em graus Celsius e classifique o clima da seguinte forma:
# "Muito Frio" (temp < 0C), "Frio" (temp de 0 a 10C), "Agradável" (11 a 25C), "Quente" (26 a 35C) e "Muito Quente" (temp > 35C)

def classificacao_temperatura(temp: float) -> None:
    if temp <= 0:
        print(f"Temperatura: {temp} | Classificação: MUITO FRIO")
    elif temp <= 10:
        print(f"Temperatura: {temp} | Classificação: FRIO")
    elif temp <= 25:
        print(f"Temperatura: {temp} | Classificação: AGRADÁVEL")
    elif temp <= 35:
        print(f"Temperatura: {temp} | Classificação: QUENTE")
    else:
        print(f"Temperatura: {temp} | Classificação: MUITO QUENTE")

# temp : float = float(input("Digite a temperatura em Celsius: "))
# classificacao_temperatura(temp)

#EX.2: Crie um algoritmo que leia a velocidade de um carro e a velocidade máxima da via. Classificar e mostrar sua situação entre
# as seguintes possíveis: sem multa, multa leve (até 20% acima), grave (até 50% acima) ou gravíssima (>50% acima).


#EX.3: Escreva um algoritmo que leia a média final de um estudante e então classifique essa nota adotando o padrão de conceitos:
# A(>= 90), B(>= 80), C(>= 70), D(>= 40), E(<40).

#EX.4: A partir da leitura da idade de uma pessoa, elabore um algoritmo que informe a sua classe eleitoral, sabendo que menores de
# 16 anos não votam (não votante), que o voto é obrigatório para adultos entre 18 e 70 anos (eleitor obrigatório) e que o voto é opcional
# para eleitores entre 16 e 18, ou maiores de 70 anos (eleitor facultativo). 

#EX.5: Em uma loja de poções, o jogador informa a quantidade de poções que deseja comprar (cada poção custa R$ 8,00)
# e a quantidade de moedas de ouro que possui. Se a quantidade de poções for maior ou igual a 10, aplique um desconto de 15%
# sobre o valor total da compra; caso contrário, não há desconto. Calcule o total a pagar e informe se o jogador tem moedas suficientes, 
# exibindo também o saldo restante (ou o valor que falta, caso não seja suficiente).

def loja_pocoes(pocoes:int, moedas:int) -> None:
    if pocoes >= 10: #verificar se tem desconto
        custo = pocoes * 8
        desconto = custo * 0.15 #desconto de 15%
        custo_final = custo - desconto #aplica desconto
        print(f"Para comprar {pocoes} poções, o valor final é: {custo}")
        print(f"Ganha desconto de {desconto} pois está comprando mais de 10 poções. Valor final: {custo_final}")
    else:
        custo_final = pocoes * 8
        print(f"Para comprar {pocoes} poções, sem desconto, o valor final é: {custo_final}")

    if moedas >= custo_final: #verificar se tem moedas suficientes
        saldo = moedas - custo_final
        print(f"Parabéns pela compra! Agora seu saldo é: {saldo}")
    else:
        print(f"SALDO INSUFICIENTE")
        falta = custo_final - moedas
        print(f"Faltam {falta} moedas")

# pocoes = int(input("Quantas poções você quer comprar? "))
# moedas = int(input("Quantas moedas você possui? "))

#EX.6: Em uma batalha de RPG, leia o poder de ataque do jogador e o poder de defesa do inimigo. Se o ataque for maior que a defesa, o dano
# causado será igual à diferença entre ataque e defesa; caso contrário, o dano será igual a apenas 10% do ataque (golpe de raspão). Em seguida,
# leia o HP atual do inimigo, subtraia o dano calculado e exiba o HP restante do inimigo, informando tambémm se ele foi derrotado (HP menor ou igual a zero).

#EX.7: Um jogador deseja carregar um item em sua mochila. Leia a capacidade máxima de peso da mochila, o peso já ocupado e o peso do novo item.
# Se a classe do personagem for "guerreiro", sua capacidade máxima recebe um bônus de 20%; caso contrário, a capacidade permanece a mesma.
# Calcule a capacidade final e verifique se o item cabe na mochila, exibindo a mensagem "Item Adicionado" com o espaço restante, ou "Mochila Cheia" caso não caiba.

#EX.8: Em um sistema de experiência, leia a quantidade de XP ganha em uma missão e a classe do personagem. Se a classe for "mago",
# o XP ganho é multiplicado po 1.5 (bônus mágico); caso contrário, o XP é mantido normal. Em seguida, leia o XP atual acumulado do personagem,
# some com o XP calculaddo e verifique se o total atingiu 1000 pontos ou mais. Exiba o XP total e a mensagem "Subiu de Nível!" ou "Ainda
# não subiu de nível", conforme o caso.

def sistema_XP(exp:float, classe: str) -> None:
    if classe == "mago" or classe == "Mago":
        bonus_xp = exp * 1.5
        print(f"Classe Mago! Ganhou Bônus Mágico!")
    else:
        print(f"Não Ganhou Bônus Mágico!")

    exp_atual = float(input("Digite o XP atual: "))
    exp_atual += bonus_xp

    if exp_atual >= 1000:
        print(f"XP TOTAL: {exp_atual} | Subiu de Nível!")
    else:
        print(f"XP TOTAL: {exp_atual} | Não Subiu de Nível!")

exp : float = float(input("Digite a quantidade de XP que você possui: "))
classe : str = str(input("Digite a classe do seu personagem: "))
sistema_XP(exp, classe)

#EX.9: Em uma loja de itens raros, leia o preço original do item e se o jogador possui "Battle Pass Premium" (S ou N). 
# Se possuir o passe, aplique 25% de desconto sobre o preço; caso contrário, aplique apenas 5% de desconto (promoção padrão).
# Em seguida, leia a quantidade de moedas do jogador, calcule o preço final e informe o troco (moedas restantes) caso a compra seja possível,
# ou a quantia que falta, caso não seja.

#EX.10: Em um jogo de tabuleiro, um dado de 6 faces é lançado duas vezes e os valores somados. Elabore um algoritmo que leia os dois valores 
# sorteados e informe o resultado da jogada: se a soma for igual a 7 ou 11, exiba "Jogada Especial, avance duas casas!"; se a soma
# for igual a 2, 3 ou 12, exiba "Jogada de Azar, perca a vez!"; caso contrário, exiba "Jogada Normal, avance conforme a soma".

#EX.11: Desenvolva um algoritmo que calcule as raízes de uma equação polinominal de grau dois cuja forma geral é ax² + bx² + c (a != 0),
# levando em consideração a existência de raízes reais e empregando a fórmula de Bhaskara (use o valor de delta para construir a seleção).