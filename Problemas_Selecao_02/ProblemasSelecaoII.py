import math

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

def classificacao_velocidade(velCarro: float, velMax: float) -> None:
    if velCarro <= velMax:
        print(f"Abaixo da Velocidade Máxima da Via | Sem Multa")
    elif velCarro <= velMax * 1.2:
        print(f"20% Acima da Velocidade Máxima da Via | Multa Leve")
    elif velCarro <= velMax * 1.5:
        print(f"50% Acima da Velocidade Máxima da Via | Multa Grave")
    else:
        print(f"Acima de 50% da Velocidade Máxima da Via | Multa Gravíssima")

# velCarro : float = float(input("Digite a velocidade do carro: "))
# velMax : float = float(input("Digite a velocidade máxima da via: "))
# classificacao_velocidade(velCarro, velMax)

#EX.3: Escreva um algoritmo que leia a média final de um estudante e então classifique essa nota adotando o padrão de conceitos:
# A(>= 90), B(>= 80), C(>= 70), D(>= 40), E(<40).

def media_final(notaFinal: int) -> None:
    if notaFinal >= 90:
        print(f"Nota A")
    elif notaFinal >= 80:
        print(f"Nota B")
    elif notaFinal >= 70:
        print(f"Nota C")
    elif notaFinal >= 40:
        print(f"Nota D")
    else:
        print(f"Nota E")

# notaFinal : int = int(input("Digite a média final do estudante (inteiro entre 0 e 100): "))
# media_final(notaFinal)       

#EX.4: A partir da leitura da idade de uma pessoa, elabore um algoritmo que informe a sua classe eleitoral, sabendo que menores de
# 16 anos não votam (não votante), que o voto é obrigatório para adultos entre 18 e 70 anos (eleitor obrigatório) e que o voto é opcional
# para eleitores entre 16 e 18, ou maiores de 70 anos (eleitor facultativo). 

def classe_eleitoral(idade: int) -> None:
    if idade < 16:
        print(f"Idade: {idade} | Classe Eleitoral: NÃO VOTANTE")
    elif idade >= 18 and idade <= 70:
        print(f"Idade: {idade} | Classe Eleitoral: ELEITOR OBRIGATÓRIO")
    else:
        print(f"Idade: {idade} | Classe Eleitoral: ELEITOR FACULTATIVO")

# idade : int = int(input("Digite a idade da pessoa: "))
# classe_eleitoral(idade)

#EX.5: Em uma loja de poções, o jogador informa a quantidade de poções que deseja comprar (cada poção custa R$ 8,00)
# e a quantidade de moedas de ouro que possui. Se a quantidade de poções for maior ou igual a 10, aplique um desconto de 15%
# sobre o valor total da compra; caso contrário, não há desconto. Calcule o total a pagar e informe se o jogador tem moedas suficientes, 
# exibindo também o saldo restante (ou o valor que falta, caso não seja suficiente).

def loja_pocoes(pocoes:int, moedas:int) -> None:
    if pocoes >= 10: #verificar se tem desconto
        custo = pocoes * 8
        desconto = custo * 0.15 #desconto de 15%
        custo_final = custo - desconto #aplica desconto
        print(f"Para comprar {pocoes} poções, o valor sem desconto é: {custo}")
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
# leia o HP atual do inimigo, subtraia o dano calculado e exiba o HP restante do inimigo, informando também se ele foi derrotado (HP menor ou igual a zero).

def batalha_RPG(ataqueJogador: float, defesaInimigo: float) -> None:
    hp_atual = int(input("Digite o HP Atual do inimigo: "))
    
    if ataqueJogador > defesaInimigo:
        dano = ataqueJogador - defesaInimigo
    else:
        dano = ataqueJogador * 0.1
    
    hp_atual -= dano
    
    if hp_atual <= 0:
        print(f"Dano causado: {dano} | HP Inimigo: {hp_atual} | Inimigo Morto!")
    else:
        print(f"Dano causado: {dano} | HP Inimigo: {hp_atual} | Inimigo Ainda Vive!")

# ataqueJogador : float = float(input("Digite o valor do ataque do seu personagem: "))
# defesaInimigo : float = float(input("Digite o valor de defesa do inimigo: "))
# batalha_RPG(ataqueJogador, defesaInimigo)

#EX.7: Um jogador deseja carregar um item em sua mochila. Leia a capacidade máxima de peso da mochila, o peso já ocupado e o peso do novo item.
# Se a classe do personagem for "guerreiro", sua capacidade máxima recebe um bônus de 20%; caso contrário, a capacidade permanece a mesma.
# Calcule a capacidade final e verifique se o item cabe na mochila, exibindo a mensagem "Item Adicionado" com o espaço restante, ou "Mochila Cheia" caso não caiba.

def mochila(cap_max: float, peso_ocupado: float, peso_item: float, classe: str) -> None:
    if classe == "guerreiro" or classe == "Guerreiro":
        cap_max *= 1.2
        print(f"Classe Guerreiro! Capacidade Máxima com Bônus: {cap_max}")
    else:
        print(f"Capacidade Máxima: {cap_max}")
        
    cap_final = cap_max - peso_ocupado
    
    if peso_item <= cap_final:
        cap_restante = cap_final - peso_item
        peso_ocupado += peso_item
        print(f"Item Adicionado! | Espaço ocupado: {peso_ocupado} | Espaço Restante na Mochila: {cap_restante}")
    else:
        print(f"Mochila Cheia! | Não é possível adicionar o item.")

# cap_max : float = float(input("Digite a capacidade máxima da mochila: "))
# peso_ocupado : float = float(input("Digite o peso já ocupado na mochila: "))
# peso_item : float = float(input("Digite o peso do item que deseja adicionar: "))
# classe : str = str(input("Digite a classe do personagem: "))
# mochila(cap_max, peso_ocupado, peso_item, classe)

#EX.8: Em um sistema de experiência, leia a quantidade de XP ganha em uma missão e a classe do personagem. Se a classe for "mago",
# o XP ganho é multiplicado po 1.5 (bônus mágico); caso contrário, o XP é mantido normal. Em seguida, leia o XP atual acumulado do personagem,
# some com o XP calculaddo e verifique se o total atingiu 1000 pontos ou mais. Exiba o XP total e a mensagem "Subiu de Nível!" ou "Ainda
# não subiu de nível", conforme o caso.

def sistema_XP(exp:float, classe: str) -> None:
    if classe == "mago" or classe == "Mago":
        bonus_xp = exp * 1.5
        print(f"Classe Mago! Ganhou Bônus Mágico!")
    else:
        bonus_xp = 0
        print(f"Não Ganhou Bônus Mágico!")

    exp_atual = float(input("Digite o XP atual: "))
    exp_atual += bonus_xp

    if exp_atual >= 1000:
        print(f"XP TOTAL: {exp_atual} | Subiu de Nível!")
    else:
        print(f"XP TOTAL: {exp_atual} | Não Subiu de Nível!")

# exp : float = float(input("Digite a quantidade de XP que você possui: "))
# classe : str = str(input("Digite a classe do seu personagem: "))
# sistema_XP(exp, classe)

#EX.9: Em uma loja de itens raros, leia o preço original do item e se o jogador possui "Battle Pass Premium" (S ou N). 
# Se possuir o passe, aplique 25% de desconto sobre o preço; caso contrário, aplique apenas 5% de desconto (promoção padrão).
# Em seguida, leia a quantidade de moedas do jogador, calcule o preço final e informe o troco (moedas restantes) caso a compra seja possível,
# ou a quantia que falta, caso não seja.

def loja_itens(preco_original: float, possui_passe: str) -> None:
    if possui_passe == "S" or possui_passe == "s":
        valor_final = preco_original * 0.75
        print(f"Comprador possui o Battle Pass Premium, desconto aplicado: {valor_final}")
    else:
        valor_final = preco_original * 0.95
        print(f"Comprador NÃO possui o Battle Pass Premium, desconto padrão aplicado: {valor_final}")

    moedas = (int(input("Digite a quantidade de moedas que você possui: ")))
    if moedas >= valor_final:
        troco = moedas - valor_final
        print(f"Compra pode ser efetuada. Valor do troco: {troco}")
    else:
        valor_faltante = valor_final - moedas
        print(f"Compra não pode ser efetuada. Faltam {valor_faltante} moedas.")

# preco_item : float = float(input("Digite o valor do produto: "))
# possui_passe : str = str(input("Possui Battle Pass Premium? S/N: "))
# loja_itens(preco_item, possui_passe)

#EX.10: Em um jogo de tabuleiro, um dado de 6 faces é lançado duas vezes e os valores somados. Elabore um algoritmo que leia os dois valores 
# sorteados e informe o resultado da jogada: se a soma for igual a 7 ou 11, exiba "Jogada Especial, avance duas casas!"; se a soma
# for igual a 2, 3 ou 12, exiba "Jogada de Azar, perca a vez!"; caso contrário, exiba "Jogada Normal, avance conforme a soma".

def sorteio_dados(num1: int, num2: int) -> None:
    soma = num1 + num2
    
    if soma == 7 or soma == 11:
        print(f"Valor Soma: {soma} | Jogada Especial, avance duas casas!")
    elif soma == 2 or soma == 3 or soma == 12:
        print(f"Valor Soma: {soma} | Jogada de Azar, perca a vez!")
    else:
        print(f"Valor Soma: {soma} | Jogada Normal, avance conforme a soma!")
        
# num1 : int = int(input("Digite o valor tirado no dado (de 1 a 6): "))
# num2 : int = int(input("Digite outro valor tirado no dado (de 1 a 6): "))
# sorteio_dados(num1, num2)

#EX.11: Desenvolva um algoritmo que calcule as raízes de uma equação polinominal de grau dois cuja forma geral é ax² + bx² + c (a != 0),
# levando em consideração a existência de raízes reais e empregando a fórmula de Bhaskara (use o valor de delta para construir a seleção).

def equacao_polinominal(a: int, b: int, c: int) -> None:
    delta = math.pow(b, 2) - (4 * a * c)
    
    if delta > 0:
        raizPos = (-b + math.sqrt(delta)) / (2 * a)
        raizNeg = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes = {raizPos}, {raizNeg}")
    elif delta == 0:
        raiz = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Raíz Dupla = {raiz}")
    else:
        print(f"Raíz Negativa! Não existe raiz real.")
        
# a : int = int(input("Digite um valor para A: "))
# b : int = int(input("Digite um valor para B: "))
# c : int = int(input("Digite um valor para C: "))
# equacao_polinominal(a, b, c)

# EX.12: Dados três valores A, B e C, verificar se eles podem ser os comprimentos dos lados de um triângulo empregando a regra 
# que cada um deve ser menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas
# (ou seja, |B - C| < A < B + C). Caso as medidas fornecidas possam formar um triângulo, verificar se elas compõem um triângulo 
# equilátero, isósceles ou escaleno. Informar se elas não compuserem um triângulo.

def class_triangulo(ladoA: int, ladoB: int, ladoC: int) -> None:
    ver1 = ladoA + ladoB
    ver2 = ladoB + ladoC
    ver3 = ladoC + ladoA
    
    if ver1 > ladoC and ver2 > ladoA and ver3 > ladoB:
        print(f"Pode formar um triângulo!")
        
        if ladoA == ladoB and ladoA == ladoC: #3 lados iguais
            print("Triângulo Equilátero.")
        elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
            print("Triângulo Isósceles.")
        else:
            print("Triângulo Escaleno.")
    else:
        print(f"Não pode formar um triângulo!")
        
# ladoA : int = int(input("Digite o comprimento do lado A: "))
# ladoB : int = int(input("Digite o comprimento do lado B: "))
# ladoC : int = int(input("Digite o comprimento do lado C: "))
# class_triangulo(ladoA, ladoB, ladoC)

# EX.13: A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a masse em KG de um boxeador e mostre
# a qual categoria ele pertence. Caso ele não se encaixe, informe "Categora inferior a Super-Médio". Lembrando que 1 kg = 2.20462263 libras.

# >= 201 libras     -> Peso-Pesado
# 176 - 200 libras  -> Cruzador
# 169 - 175 libras  -> Meio-Pesado
# 161 - 168 libras  -> Super-Médio

def class_boxeador(pesoBox: float) -> None:
    pesoLb = pesoBox * 2.20462263
    
    if pesoLb >= 201:
        print(f"Peso do Boxeador em LIBRAS: {pesoLb:.2f} | Categoria: Peso-Pesado")
    elif pesoLb >= 176:
        print(f"Peso do Boxeador em LIBRAS: {pesoLb:.2f} | Categoria: Cruzador")
    elif pesoLb >= 169:
        print(f"Peso do Boxeador em LIBRAS: {pesoLb:.2f} | Categoria: Meio-Pesado")
    elif pesoLb >= 161:
        print(f"Peso do Boxeador em LIBRAS: {pesoLb:.2f} | Categoria: Super-Médio")
    else:
        print(f"Peso do Boxeador em LIBRAS: {pesoLb:.2f} | Categoria: Inferior a Super-Médio")
        
pesoBoxeador : float = float(input("Digite o peso (em KG) do boxeador: "))
class_boxeador(pesoBoxeador)