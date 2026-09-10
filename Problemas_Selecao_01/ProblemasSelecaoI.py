
import math
from datetime import date
#EX.1: Em uma determinada papelaria a fotocópia custa R$0,25, caso sejam tiradas menos de 100 cópias.
# A partir de 100 cópias, o valor de cada fotocópia trada reduz para R$0,20.
# Elabore um algoritmo que leia o número de cópias que serão feitas e mostre o valor a pagar pelo serviço.

def preco_copias(qtdeCopias: int) -> None:
    if (qtdeCopias >= 100):
        valorPagar = qtdeCopias * 0.2
    else:
        valorPagar = qtdeCopias * 0.25

    print(f"Para {qtdeCopias} cópias, vai custar R${valorPagar:.2f}")

# quantidadeCopias : int = int(input("Digite quantas cópias você quer imprimir: "))
# preco_copias(quantidadeCopias)
# preco_copias(quantidadeCopias)

#EX.2: Crie um algoritmo que leia o valor total de uma compra. Caso seja maior ou igual a R$ 500,00, aplique 5% de desconto
# e mostre o valor final; caso contrário, informe que não há desconto e o valor original da compra

def valor_compra(valor_total: float) -> None:
    if valor_total >= 500:
        valor_total *= 0.95
        print(f"Sua compra ganhou desconto! Valor total com desconto: {valor_total:.2f}")
    else:
        print(f"Sua compra não ganha desconto! Valor total: {valor_total:.2f}")

# total_compra : float = float(input("Digite o valor da sua compra: "))
# valor_compra(total_compra)

#EX.3: Escreva um algoritmo que leia a idade de uma pessoa. Se a idade for menor igual a 15 ou maior que 65, o preço do
# ingresso de um evento será de R$ 19,90. Caso contrário, o preço do ingresso será de R$ 25,90. Exiba o preço a ser pago.

def validacao_idade_ingresso(idade: int) -> None:
    if idade <= 15 or idade > 65:
        print(f"Preço do ingresso para essa faixa etária é R$19,90")
    else:
        print(f"Preço do ingresso para essa faixa etária é R$25,90")
        
# idade_atual : int = int(input("Digite a sua idade: "))
# validacao_idade_ingresso(idade_atual)

#EX.4: Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada e sua raiz cúbica (informe “Valor
# inválido” para números negativos). Veja como usar o módulo math do Python para ambas as operações
    
def raiz_qrd_cub(valor: int) -> None:
    if valor >= 0:
        sqrt_valor = math.sqrt(valor)
        print(f"Raiz Quadrada de {valor} é {sqrt_valor:.2f}")
        cubic_valor = math.cbrt(valor)
        print(f"Raiz Cubica de {valor} é {cubic_valor:.2f}")
    else:
        print(f"Valor inválido (negativo)")
        
# num : int = int(input("Digite um número inteiro: "))
# raiz_qrd_cub(num)

#EX.5: Crie um algoritmo que leia dois números inteiros e verifique se o primeiro é divisível pelo segundo. Se for, exiba "O
# primeiro número é divisível pelo segundo". Caso contrário, exiba "O primeiro número não é divisível pelo segundo"

def divisivel(num1: int, num2: int) -> None:
    if num1 % num2 == 0:
        print(f"{num1} é divisível por {num2}")
    else:
        print(f"{num1} não é divisível por {num2}")
        
# num1 : int = int(input("Digite o primeiro número: "))
# num2 : int = int(input("Digite o segundo número: "))
# divisivel(num1, num2)

#EX.6: A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe a idade que completará (ou
# já completou) no ano atual (pegar o ano do sistema via Python). Verifique se ele já pode fazer a carteira de motorista ou não, 
# informando sua situação

def ano_nascimento(ano: int) -> None:
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 18:
        print(f"Idade atual é {idade}! Pode fazer a CNH!")
    else:
        print(f"Idade atual é {idade}! Não pode fazer a CNH!")

# nascimento : int = int(input("Digite seu ano de nascimento: "))
# ano_nascimento(nascimento)

#EX.7: Em um jogo de cartas, leia o nível de ataque e o nível de defesa de uma carta. Calcule o 'valor total' da carta somando ataque e defesa.
# Se o ataque for maior que 80 ou a defesa for maior que 80, exiba "Carta Rara! Valor Total: VT".
# Caso contrário, exiba "Carta Comum! Valot Total: VT"

def raridade_carta(ataque: int, defesa: int) -> None:
    valor_total = ataque + defesa

    if (ataque > 80 or defesa > 80):
        print(f"Carta Rara! Valor Total: {valor_total}.")
    else:
        print(f"Carta Comum! Valor Total: {valor_total}.")

# nivel_ataque : int = int(input("Digite o nível de ataque da sua carta: "))
# nivel_defesa : int = int(input("Digite o nível de defesa da sua carta: "))
# raridade_carta(nivel_ataque, nivel_defesa)

#EX.8: Em um jogo de sobrevivência, leia a quantidade de comida e a quantidade de água que o personagem possui. Calcule
# o "índice de sobrevivência" (IS) como a soma dos dois valores. Se a comida for menor que 10 ou a água for menor que 5,
# exiba "Alerta: recursos críticos! Índice de sobrevivência: valor do IS". Caso contrário, exiba "Recursos estáveis. Índice
# de sobrevivência: valor do IS"

def indice_sobrevivencia(comida: int, agua: int) -> None:
    ind_sbrv : int = comida + agua
    if comida < 10 or agua < 5:
        print(f"Alerta: recursos críticos! Índice de sobrevivência: {ind_sbrv}")
    else:
        print(f"Recursos estáveis. Índice de sobrevivência: {ind_sbrv}")

# valor_comida : int = int(input("Digite a quantidade de comida que você possui: "))
# valor_agua : int = int(input("Digite a quantidade de água que você possui: "))
# indice_sobrevivencia(valor_comida, valor_agua)

#EX.9: O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula: IMC = massa / altura²
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e mostre o valor do IMC e se
# ele está na faixa considerada “normal” segundo o critério apresentado na tabela da OMS (Organização Mundial de Saúde):
# 18,5 ≤ IMC < 25. Caso não esteja, calcule sua massa máxima considerada normal (usando o IMC igual a 24,9)

def calculo_IMC(massa: float, altura: float) -> None:
    IMC : float = massa / (math.pow(altura, 2))
    
    if IMC >= 18.5 and IMC < 25:
        print(f"Seu IMC é {IMC:.2f}. Está na faixa considerada normal.")
    else:
        massa_maxima : float = 24.9 * (math.pow(altura, 2))
        print(f"Seu IMC é {IMC:.2f}. Não está na faixa considerada normal. Sua massa máxima considerada normal é: {massa_maxima:.2f} kg.")
    
# valor_massa : float = float(input("Digite sua massa (em kg): "))
# valor_altura : float = float(input("Digite sua altura (em metros): "))
# calculo_IMC(valor_massa, valor_altura)
    
#EX.10: Em um jogo de estratégia, leia a quantidade de soldados e a quantidade de armamento (unidades) do exército do jogador.
# Calcule "o poder de combate" (PC) multiplicando soldados por armamento. Se o número de soldados for maior que 50 e o armamento 
# for maior que 20, exiba "Exército pronto para o ataque! Poder de Combate: PC". Caso contrário, exiba "Exército Fraco Ainda! Poder de Combate: PC".

def poder_combate(soldados: int, armamento: int) -> None:
    poder_combate = soldados * armamento

    if (soldados > 50 and armamento > 20):
        print(f"Exército pronto para o ataque! Poder de Combate: {poder_combate}")
    else:
        print(f"Exército Fraco Ainda! Poder de Combate: {poder_combate}")

# quantidadeSoldados : int = int(input("Digite a quantidade de soldados do se exército: "))
# quantidadeArmamento : int = int(input("Digite a quantidade de armamento do se exército: "))
# poder_combate(quantidadeSoldados, quantidadeArmamento)

#EX.11: Crie um algoritmo que leia o comprimento de três lados e verifique se eles podem formar um triângulo. Para que
# três lados formem um triângulo, a soma do comprimento de quaisquer dois lados deve ser maior que o comprimento do
# terceiro. Se puderem formar, exiba "Pode formar um triângulo." Caso contrário, exiba "Não pode formar um triângulo."

def verificacao_triangulo(ladoA: int, ladoB: int, ladoC: int) -> None:
    ver1 = ladoA + ladoB
    ver2 = ladoB + ladoC
    ver3 = ladoC + ladoA
    
    if ver1 > ladoC and ver2 > ladoA and ver3 > ladoB:
        print(f"Pode formar um triângulo!")
    else:
        print(f" Não pode formar um triângulo!")

# ladoA : int = int(input("Digite o comprimento do lado A: "))
# ladoB : int = int(input("Digite o comprimento do lado B: "))
# ladoC : int = int(input("Digite o comprimento do lado C: "))
# verificacao_triangulo(ladoA, ladoB, ladoC)


# EX.12: Em um determinado estacionamento a primeira hora custa R$ 20,00, que é o valor mínimo praticado. Após uma hora
# o valor é fracionado, R$ 3,50 a cada 15 minutos. Elabore um algoritmo que leia um número inteiro correspondente a
# quantidade de minutos usados por um determinado cliente do estacionamento e mostre a mensagem “Valor mínimo, R$ 20,00” 
# ou “Valor fracionado, R$ x”, no qual x será o valor a pagar calculado pelo algoritmo.

def sistema_estacionamento(minEstacionados: int) -> None:
    valor_minimo : float = 20.0
    valor_fracionado : float = 3.50
    if minEstacionados <= 60:
        print(f"Menos de uma hora estacionado. Valor mínimo: R${valor_minimo:.2f}")
    else:
        horas_estacionado = minEstacionados // 60
        min_a_mais = minEstacionados % 60
        fracao_a_pagar = math.ceil(min_a_mais / 15) + (horas_estacionado - 1) * 4
        valor_pagar = valor_minimo + (valor_fracionado * fracao_a_pagar)
        print(f"Mais de uma hora estacionado. Valor a pagar: R${valor_pagar:.2f}")
        
minEstacionados : int = int(input("Digite os minutos que ficou estacionado: "))
sistema_estacionamento(minEstacionados)

#substituir valor de variáveis uma pela outra, sem precisar criar outra
# a, b = b, a