#EX.1: Elabore um algoritmo que leia a quantidade de XP de que um jogador tem e o XP necessário para o próximo nível.
#      Calcule e mostre quanto XP ainda falta para o jogador subir de nível. 
XP_atual = int(input("Digite seu XP atual: "))
XP_proximo_nivel = int(input("Digite o XP necessário para o próximo nível: "))
XP_faltante = XP_proximo_nivel - XP_atual
print(f"Quantidade de XP para o próximo nível: {XP_faltante}")

#EX.2: Contrua um algoritmo que leia o valor do salário de um funcionário,
#      calcule e mostre quantos salários-mínimos este funcionário recebe.

salario_minimo = 1621
salario_funcionario = float(input("Digite seu salário: "))

resto = salario_funcionario // salario_minimo
print(resto)

#EX.3: Escreva um algoritmo que leia o peso (em KG) e a altura (em metros) de uma pessoa,
#      calcule e exiba o seu inddice de massa corporal (IMC), usanod a fórmula: IMC = peeso / altura²

peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / pow(altura, 2)
print(IMC)

#EX. 4: Faça um algoritmo que leia o diâmetro de um círculo e calcule a área
diametro = float(input("Digite o diâmetro do círculo: "))
raio = (diametro/2)
area = 3.14 * pow(raio, 2)
print(area)

#EX.5: Escreva um algoritmo que dado o horário fornecido pelo usuário(hora, minuto e segundo),
#      calcule e mostre o total de segundos que transcorreram desde o início do dia

hora = int(input("Digite a hora: ")) # 1 hora = 3600 segundos
minutos = int(input("Digite os minutos: ")) # 1 minutos = 60 segundos
segundos = int(input("Digite os segundos: "))

total_segundos = (hora * 3600) + (minutos * 60) + segundos
print(f"Total de segundos desde o início do dia é: {total_segundos}")

#EX.6: Crie um algoritmo que leia o valor dos dois catetos de um triângulo retângulo e calcule a respectiva hipotenusa.
catA = int(input("Digite o valor do cateto A: "))
catB = int(input("Digite o valor do cateto B: "))
hip = pow(catA, 2) + pow(catB, 2)
hip = pow(hip, 0.5) #raiz quadrada
print(hip)

#EX.7: Elabore um algoritmo que leia quantos reais um individuo possui para converter,
#      calcule e mstre o valor que ele pode obter em dólares, euros e libras esterlinas.

reais = float(input("Digite quantos reais você deseja converter: "))
dolar = 5.18
euro = 6.04
libra = 7.04

conversao_dolar = print(f"Valor convertido em dólares: {reais / dolar}")
conversao_euro = print(f"Valor convertido em euro: {reais / euro}")
conversao_libra = print(f"Valor convertido em libra esterlina: {reais / libra}")

#EX.8: Escreva um algoritmo para calcular o volume de uma esfera de raio r, sendo que r é um valor fornecido pelo usuário, dado que volume = (4/3)PIr³
raio = float(input("Digite o raio da esfera: "))
volume = (4/3) * 3.14 * pow(raio, 3)
print(volume)

#EX.9: Elabore um algoritmo que leia uma temperatura em Celsius, converta e exiba seu valor em Fahrenheit e em Kelvim, usando as fórmulas:
# F = (9/5)*C+32
# K = C + 273.15

tempCelsius = float(input("Digite a temperatura em Celsius: "))
tempFahr = (9/5) * tempCelsius + 32
tempKelvin = tempCelsius + 273.15
print(tempFahr)
print(tempKelvin)

#EX.10: Escreva um algoritmo que leia dois números inteiros, a e b, e troque os seus valores. No final, mostre o novo valor de a e b.
numA = int(input("Digite o valor de A: "))
numB = int(input("Digite o valor de B: "))
aux = 0
aux = numA
numA = numB
numB = aux
print(f"Número A trocado: {numA}")
print(f"Número B trocado: {numB}")

#EX.11: Crie um algoritmo que leia a nota de duas provas e de um trabalho, calcule a média ponderada
#       considerando pesos 4, 4 e 2, respectivamente. mostre a média com duas casa decimais.

#média ponderada = [(valor * peso) + (valor1 * peso1)] / SomaPesos
prova1 = float(input("Digite a nota da prova 1 (inteiro): "))
prova2 = float(input("Digite a nota da prova 2 (inteiro): "))
trabalho1 = float(input("Digite a nota do trabalho 1 (inteiro): "))

peso1 = 4
peso2 = 4
peso3 = 2
mCima = (prova1 * peso1) + (prova2 * peso2) + (trabalho1 * peso3)
mBaixo = (peso1 + peso2 + peso3)
m = mCima / mBaixo 
print(f"{m:.2f}")

#EX.12: Escreva um algoritmo que leia a vida máxima (HP) de um personagemm e a vida atual.
#       Calcule e mostre a porcentagem de vida restante do personagem, com duas casas decimais.
HP_max = 100
HP_atual = int(input("Digite a vida atual do personagem: "))
HP_restante = (HP_atual * 100) / HP_max
print(f"{HP_restante:.2f}")

#EX.13: Elabore um algoritmo que leia o preço desse produto e então mostre as opções de compra disponiveis calculadas, que são:
# 5% de acréscimo em 3 parcelas
# Preço de tabela em 2 parcelas
# Preço à vista com 5% de desconto

precoProduto = float(input("Digite o valor do produto(float): "))
p1 = (precoProduto * 1.05) / 3
p2 = precoProduto / 2
p3 = precoProduto - (precoProduto * 0.05)
print(f"Preço de cada parcela, em 3x com 5% de acréscimo: {p1}")
print(f"Preço de tabela parcelado em 2x: {p2}")
print(f"Valor à vista, com 5% de desconto: {p3}")

#EX.14: Elabore um programa Python que leia o nome do usuário e então mostre: "Bem-vindo NOME! Seu nome tem X letras",
#       ou seja, mostre o nome com caracteres maiúsculos e o total de letras

nome = str(input("Digite seu nome: "))
letras = len(nome.replace(" ", ""))  # Retorna letras sem espaço
print(f"Bem-vindo {nome.upper()}! Seu nome tem {letras} letras.")

#EX.15: Crie um algoritmo que leia o tempo total de cooldown de uma habilidade em segundos e mostre esse tempo convertido em minutos e segundos.
        #Por exemplo: 125 segundos = 2 minutos e 5 segundos

cooldown = int(input("Digite o cooldown da habilidade em segundos: "))
cd_minutos = cooldown // 60
cd_segundos = cooldown % 60
print(f"{cooldown} segundos = {cd_minutos} minutos e {cd_segundos} segundos.")