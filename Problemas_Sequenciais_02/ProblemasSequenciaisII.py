from math import pi
from enum import Enum

#EX.1: Elabore um agoritmo que leia um numero total de segundos e converta0o para
# horas, minutos e segundos, mostrando o serultado no formato hh:mm:ss

def converter_segundos(segundos: int) -> None:
    """Recebe um numero e tranforma em hh:mm:ss"""
    # 1 hora = 3600 segundos
    horas = segundos // 3600
    resto = segundos % 3600

    # 1 minuto = 60 segundos
    minutos = resto // 60
    segundos_restantes = resto % 60

    print(f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}")

# total_segundos = int(input("Digite o número total de segundos: "))
# converter_segundos(total_segundos)

#EX.2: Escreva um algoritmo que leia o lado de um quadrado e calcule a área do maior círculo que pode ser inscrito dentro desse quadrado.

def quadrado_circulo(ladoSqr: int) -> None:
    """Recebe o lado de um quadrado e calcula a área do maior
    círculo que pode ser inscrito dentro do quadrado"""

    raio = ladoSqr/2

    areaCirculo = pi * pow(raio, 2)
    print(f"Area do maior círculo que cabe no quadrado: {areaCirculo:.2f}")

# ladoSqr = int(input("Digite o valor inteiro do lado do quadrado: "))
# quadrado_circulo(ladoSqr)

#EX.3: Construa um algoritmo que calcule o valor de uma conta de energia elétrica de uma cidade hipotética considerando:
#       leitura do mês anterior (em Kwh) e leitura do mês atual (em Kwh). O valor do kWh é de R$0,636
#       e o valor final conta com taxa extra de ICMS de 27%

def conta_energia(kwhMesAnterior: float, kwhMesAtual: float) -> float:
    KWH: float = 0.636
    ICMS: float = 1.27

    consumoMes = kwhMesAtual - kwhMesAnterior
    consumoMensalReais = consumoMes * KWH * ICMS
    return consumoMensalReais

# leituraAnterior = float(input("Digite a leitura do mês anteiror (kWh): "))
# leituraAtual = float(input("Digite a leitura do mês atual (kWh): "))
# valorConta = conta_energia(leituraAnterior, leituraAtual)
# print(f"Valor da conta de energia: R${valorConta:.2f}")

#EX.4: Um item de loot tem uma "pontuação de raridade" (de 0 a 1000) que precisa ser convertida em três atributos do item:
# Poder = pontuação * 0.5;
# Durabilidade = pontuação * 0.3;
# Valor de Venda (em moedas) = pontuação* 2.75 -> arredodndado para o inteiro mais próximo
# Além disso, o jogo cobra uma taxa de mercado de 8% sobre o valor de venda ao negociar o item.
# Elabora um algoritmo que leia a pontuação de raridade de um item e mostra:
# o Poder, a Durabilidade, o Valor de Venda bruto e o valor líquido recebido após a taxa de mercado.

def pontuacao_raridade_item(raridade: int, nomeItem: str) -> None:
    TAXA_MERCADO: float = 0.92

    poder = raridade * 0.5
    durabilidade = raridade * 0.3
    valorVendaBruto = raridade * 2.75 #round(x) para arredondar

    print(f"Item {nomeItem} | Poder = {poder:.2f} | Durabilidade = {durabilidade:.2f} | Valor Bruto = {round(valorVendaBruto):.2f} | Valor com Taxa = {round(valorVendaBruto) * TAXA_MERCADO:.2f}")

# nomeItem = str(input("Digite o nome do item: "))
# raridadeItem = int(input("Digite a raridade do item (0 a 1000): "))
# pontuacao_raridade_item(raridadeItem, nomeItem)

#EX.5: Um jogo de RPG converte tempo de jogo em "dias de aventura":
# 1 dia de aventura = 8 horas reais
# 1 hora real = 60 minutos
# cada minuto de jogo rende 12 moedas de ouro (int)
# Elabore um algoritmo que leia quantos minutos totais o jogador já jogou e calcule:
# Quantos dias, horas e minutos de AVENTURA isso representa
# Quantas moedas de outo o jogador acumulou nesse tempo

def dias_aventura(minutosJogados: int) -> None:
    DIA_AVENTURA: int = (60 * 8)
    diaAventura = minutosJogados // DIA_AVENTURA
    resto = minutosJogados % DIA_AVENTURA
    horasAventura = resto // 60
    minutosAventura = resto % 60

    moedas = minutosJogados * 12

    print(f"Dias de Aventura: {diaAventura} | Horas de Aventura: {horasAventura} | Minutos de Aventura: {minutosAventura} | Moedas Acumuladas: {moedas} ")

# minutos_totais = int(input("Digite quantos minutos totais você já jogou: "))
# dias_aventura(minutos_totais)

#EX.6: Elabora um algoritmo que leia um número inteiro e considerando que este possui exatamente três algarismos,
# mostre o valor da centena, da dezena e da unidade(use apenas operações matemáticas, sem condicionais)

def num_tres_algarismos(numeroTresCasas: int) -> None:
    centenas = numeroTresCasas // 100
    resto = numeroTresCasas % 100
    dezenas = resto // 10
    unidades = resto % 10

    print(f"Centenas: {centenas} | Dezenas: {dezenas} | Unidades: {unidades}")

# numero = int(input("Digite um número de três algarismos: "))
# num_tres_algarismos(numero)

#EX.7: 

#EX.8: Elabore um algoritmo que leia três valores inteiros a, b e c. Em seguida, encontre e mostre o maior dos 3 valores usando a fórmula:
# maiorAB = (a + b + abs(a - b)) / 2
def maior_de_dois(x, y):
    return (x + y + abs(x - y)) / 2

def maior_valor_ABC(a: int, b: int, c: int) -> int:
    maiorAB = maior_de_dois(a, b)
    maiorNum = maior_de_dois(maiorAB, c)
    return int(maiorNum)

# valor_a = int(input("Digite o valor de A: "))
# valor_b = int(input("Digite o valor de B: "))
# valor_c = int(input("Digite o valor de C: "))

# resultado = maior_valor_ABC(valor_a, valor_b, valor_c)
# print(f"O maior valor é: {resultado}")

#EX.9: Um caixa automático possui as seguintes cédulas disponíveis: 50, 20, 10, 5, 2 e 1.
# Faça um algoritmo que leia o valor de um saque e mostre a quantidade de bilhetes de cada nota necessários para comporem
# o valor solicitado pelo usuário (use apenas operações matemáticas)

def cedulas_caixa(valorSaque: int) -> None:
    cedulas50 = valorSaque // 50
    resto50 = valorSaque % 50
    cedulas20 = resto50 // 20
    resto20 = resto50 % 20
    cedulas10 = resto20 // 10
    resto10 = resto20 % 10
    cedulas5 = resto10 // 5
    resto5 = resto10 % 5
    cedulas2 = resto5 // 2
    resto2 = resto5 % 2
    cedulas1 = resto2 // 1

    print(f"Notas de 50: {cedulas50} | Notas de 20: {cedulas20} | Notas de 10: {cedulas10} | Notas de 5: {cedulas5} | Notas de 2: {cedulas2} | Notas de 1: {cedulas1}")

valorSaque = int(input("Digite o valor que deseja sacar: "))
cedulas_caixa(valorSaque)