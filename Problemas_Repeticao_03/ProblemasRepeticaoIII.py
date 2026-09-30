import random

# EX.1: Escreva um programa que leia um conjunto de números inteiros até que o usuário forneça o valor 0 (zero).  
# Para cada número par, some-o com a soma dos anteriores, para cada número ímpar, subtraia-o da soma dos anteriores. 
# Exemplo: para a entrada: 2 + 4 - 3 + 2 -1 0, o resultado é 4.  
# Mostre então o resultado desta soma, a quantidade total de números fornecidos assim como a porcentagem de números 
# ímpares e de números pares (desconsiderando o finalizador 0).

def numeros() -> None:
    soma : int = 0
    num_par : int = 0
    num_impar : int = 0
    num_fornecido : int = 1
    total_numeros : int = 0
    while num_fornecido != 0:
        num_fornecido = int(input("Digite um número inteiro: "))
        if num_fornecido != 0:
            if num_fornecido % 2 == 0: #par
                soma += num_fornecido
                num_par += 1
            else: #impar
                soma -= num_fornecido
                num_impar += 1
                
    total_numeros = num_par + num_impar
    if total_numeros == 0:
        print("Nenhum número válido foi fornecido!")
    else:
        print(f"Valor total da soma = {soma} | Total de Números: {total_numeros} | Porcentagem Pares: {(num_par * 100)/total_numeros} | Porcentagem Ímares: {(num_impar * 100/total_numeros)}")

#numeros()

# EX.2: Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a leitura quando atingir um 
# total de 5 números lidos válidos. Serão considerados inválidos os números múltiplos de 3. Informe então qual é a média 
# do conjunto.

def numeros_validos() -> None:
    num : int = 0
    num_validos : int = 0
    soma : int = 0
    media : float = 0
    while num_validos < 5:
        num = int(input("Digite um valor inteiro: "))
        if num % 3 != 0: #NÃO é multiplo de 3
            soma += num
            num_validos += 1
    media = soma / num_validos
    print(f"A média dos números válidos é: {media}")
    
#numeros_validos()

# EX.3: Elabore um algoritmo que leia um conjunto de números inteiros e somente termine a leitura quando for fornecida 
# uma sequência de dois números iguais. Mostre então qual a média do conjunto desconsiderando os últimos dois números 
# (os finalizadores).

def seq_inteiros() -> None:
    contador : int = 0
    num_antigo : int = int(input("Digite um número inteiro: "))
    num_novo : int = int(input("Digite um número inteiro: "))
    soma : int = 0
    media : float = 0
    while num_novo != num_antigo:
        soma += num_antigo
        contador += 1
        num_antigo = num_novo
        num_novo = int(input("Digite um número inteiro: "))
        
    if contador == 0:
        print("Nenhum número válido foi fornecido!")
    else:
        media = soma / contador
        print(f"Média dos valores sem os finalizadores: {media}")

#seq_inteiros()

# EX.4: Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a leitura quando for fornecido 
# como finalizador o mesmo valor fornecido no início da sequência. Informe então qual é a soma do conjunto, excluindo 
# o primeiro e o último.

def soma_inteiros() -> None:
    contador : int  = 0
    num_inicial : int = int(input("Digite um número inteiro (inicial): "))
    num_novo : int = int(input("Digite um número inteiro: "))
    soma : int = 0
    while num_novo != num_inicial:
        soma += num_novo
        contador += 1
        num_novo = int(input("Digite um número inteiro: "))
    
    if contador == 0:
        print("Segundo número fornecido igual ao primeiro, sem valores para somar!")
    else:
        print(f"Soma dos valores entre o primeiro e o último (iguais): {soma}")

#soma_inteiros()
 
# EX.5: Escreva um algoritmo que leia um conjunto de números inteiros e que somente termine a leitura quando for fornecido 
# um valor 0 (zero) imediatamente após um número ímpar. Informe então qual foi o menor número impar fornecido.

def impares() -> None:
    num_anterior : int = int(input("Digite um número inteiro: "))
    num_novo : int = int(input("Digite um número inteiro: "))
    menor_num_impar : int = float('inf') #inicializa com infinito, para que qualquer número impar seja menor que ele
    while not (num_anterior % 2 != 0 and num_novo == 0): # preciso continuar o loop enquanto a dupla (anterior impar + novo igual a zero) não tiver acontecido ainda
        num_anterior = num_novo
        
        if num_novo % 2 != 0: #é impar?
            if num_novo < menor_num_impar:
                menor_num_impar = num_novo
        num_novo = int(input("Digite um número inteiro: "))

        print(menor_num_impar)
    
#impares()
            
# EX.6: Uma base espacial começa com 50 tripulantes saudáveis. A cada minuto, uma infecção alienígena contamina 3 
# tripulantes. A cada 4 minutos, a equipe médica consegue curar uma quantidade sorteada entre 5 e 10 tripulantes — mas 
# a cura só funciona se ainda houver pelo menos 10 tripulantes saudáveis (caso contrário, a equipe médica não tem 
# recursos suficientes e a cura falha). Simule minuto a minuto e informe quantos minutos a 
# base resistiu até não sobrar nenhum tripulante saudável.

def base_espacial() -> None:
    tripulantes_saudaveis : int = 50
    min : int = 0
    curar : int = random.randint(5, 10)
    curas_efetuadas : int = 0
    
    while tripulantes_saudaveis > 0:                        #tem alguém saudável = continua
        min += 1                                            #cada loop = 1 minuto passa
        tripulantes_saudaveis -= 3                          #a cada min, 3 ficam doentes
        print(f"Minuto: {min} | Tripulantes Saudáveis: {tripulantes_saudaveis}/50")
        
        if (min % 4 == 0) and tripulantes_saudaveis >= 10:  #minuto multiplo de 4
            curar = random.randint(5, 10)
            tripulantes_saudaveis += curar
            curas_efetuadas += 1
            print(f"Tripulantes curados: {curar} | Tripulantes Saudáveis: {tripulantes_saudaveis}/50")
        else:
            print("Cura não aconteceu!")

    print(f"Levou {min} para todos da base ficarem doentes!")

#base_espacial()

# EX.7: Em uma determinada competição esportiva cada participante recebe notas (de 0 a 10.0) de seis juízes. A melhor e a 
# pior nota são eliminadas, sendo a nota do participante a média das outras quatro notas. Elabore um algoritmo que leia 
# as seis notas de um atleta e depois informe qual foi seu resultado final.

#cada loop comparar a nota atual com a menor nota até agora. Se for menor, troca. Salvar a primeira nota como menor
def competicao_esportiva() -> None:
    nota_final : float = 0
    nota_um = float(input("Digite a nota (o a 10.0): "))
    soma : float = nota_um
    menor_nota : float = nota_um
    maior_nota : float = nota_um
    for i in range(1, 6, 1):
        nota = float(input("Digite a nota (o a 10.0): "))
        if nota < menor_nota:
            menor_nota = nota
        elif nota > maior_nota:
            maior_nota = nota
        soma += nota
    
    nota_final = (soma - menor_nota - maior_nota) / 4
    print(f"Nota final do atleta (sem menor e maior): {nota_final}")

#competicao_esportiva()

# EX.8: Escreva um algoritmo que mostre as tabuadas de multiplicação dos números 1 até 10.

def tabuada() -> None:
    for i in range(1, 11, 1): # i = qual tabuada
        print(f"Tabuada {i}:")
        for j in range(1, 11, 1): # j = multiplicador
            print(f"{j * i}", end = " | ")
        print()
#tabuada()

# EX.9: Crie um algoritmo que leia 10 números inteiros. Quando o número fornecido for positivo, mostre uma contagem 
# regressiva até 0; quando ele for negativo, uma contagem normal até 0; quando for nulo mostre “não atendido pelo programa”. 

def contagem() -> None:
    for i in range(1, 11, 1):
        print(f"Número {i}:")
        num = int(input("Digite um número inteiro: "))
        if num > 0:
            print("Número positivo. Contagem regressiva:")
            while num >= 0:
                print(num)
                num -= 1
        elif num < 0:
            print("Número negativo. Contagem progressiva:")
            while num <= 0:
                print(num)
                num += 1
        else:
            print("Número não atendido pelo programa.")
            
#contagem()

# EX.10: Um cofre em um jogo tem um código secreto de 3 dígitos gerado aleatoriamente (cada dígito entre 0 e 9). O jogador 
# tenta adivinhar dígito por dígito, um valor por vez, e o algoritmo informa, a cada tentativa, apenas quantos dígitos ele 
# acertou na posição correta — sem usar variáveis compostas, apenas comparando um dígito de cada vez com variáveis 
# simples. O algoritmo deve continuar até o jogador acertar os 3 dígitos, contando e exibindo ao final o número total de 
# tentativas usadas até conseguir abrir o cofre.

def cofre() -> None:
    senha : int = random.randint(100, 999)
    senha_um : int = senha // 100
    senha_dois : int = (senha % 100) // 10
    senha_tres : int = (senha % 10)
    tentativas : int = 0
    acertou : bool = False
    
    #print(senha, senha_um, senha_dois, senha_tres) #teste
    
    print("Tente adivinhar a senha de 3 dígitos")
    while not acertou:
        dig_um : int = int(input("Digito um (0 a 9): "))
        dig_dois : int = int(input("Digito dois (0 a 9): "))
        dig_tres : int = int(input("Digito três (0 a 9): "))
    
        if dig_um == senha_um:
            print("Acertou o primeiro número")
        
        if dig_dois == senha_dois:
            print("Acertou o segundo número")
            
        if dig_tres == senha_tres:
            print("Acertou o terceiro número")
            
        if dig_um == senha_um and dig_dois == senha_dois and dig_tres == senha_tres:
            acertou = True
            
        tentativas += 1
        
    print(f"Acertou a senha '{senha}' com {tentativas} tentativas!")

#cofre()

# EX.11: Um número natural é um número primo quando ele tem exatamente dois divisores: o número um e ele mesmo. Em 
# outras palavras, é um número maior que um que não é divisível por nenhum outro número maior que um e menor que 
# ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13, 17, 19 etc. Elabore um algoritmo que mostre os números primos existentes no 
# intervalo de 1 a 500.

def num_primo() -> None:
    primo : bool = True
    
    for i in range(1, 501, 1):
        primo = True #reset a cada número testado
        for j in range(2, i - 1, 1): #checar cada divisor disponível até o n - 1
            if i % j == 0: #divisão exata = NÃO é primo
                primo = False
                break
            
        if i == 1:
            primo = False
            
        if primo: #print só dos primos
            print(f"{i} é primo")
        
num_primo()

# EX.12: Uma nave espacial começa com 1000 unidades de combustível. A cada segundo de viagem, ela consome 10 
# unidades. A cada 7 segundos, ocorre uma tempestade de meteoros que sorteia um dano extra de combustível entre 20 e 
# 50 unidades. Simule a viagem segundo a segundo e informe quantos segundos a nave resistiu até o combustível acabar.

def nave_espacial() -> None:
    combustivel : int = 1000
    segundos_viagem : int = 1
    dano_extra : int = 0
    while combustivel > 0:
        if segundos_viagem % 7 == 0:
            dano_extra = random.randrange(20, 50)
            combustivel -= dano_extra
            print(f"Tempestade de Meteoros! Combustível reduzido em {dano_extra}!")
        else:
            combustivel -= 10
        print(f"Combustível restante: {combustivel}")
        segundos_viagem += 1
    
    segundos_viagem -= 1 #subtrai 1 pois o loop só termina quando o combustível acaba, então o último segundo não conta
    print(f"Nave resistiu {segundos_viagem} segundos de viagem!")
#nave_espacial()