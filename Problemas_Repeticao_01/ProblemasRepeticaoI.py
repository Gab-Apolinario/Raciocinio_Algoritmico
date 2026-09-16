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

# EX.7: Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela de conversão
# de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 kilômetros.

def conversao_milhas_while() -> None:
    km = 20
    
    while (km <= 160):
        milhas = (km * 1000) / 1609.34 #transforma kms em metros e depois em milhas
        print(f" Kilometros: {km} | Milhas: {milhas:.2f}")
        km += 10
        
conversao_milhas_while()

def conversao_milhas_for() -> None:
    for km in range(20, 161, 10):
        milhas = (km * 1000) / 1609.34 #transforma kms em metros e depois em milhas
        print(f" Kilometros: {km} | Milhas: {milhas:.2f}")
        
conversao_milhas_for()