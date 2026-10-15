# EX.1: Leia uma string do usuário e mostre-a modificada das seguintes formas:
# • Do início para final, alternando as letras entre maiúsculas e minúsculas
# • Do final para o início, também alternando as letras entre maiúsculas e minúsculas

def alternando_crescente(frase: str) -> None:
    for i in range(len(frase)):
        if i % 2 == 0:
            print(frase[i].upper(), end = "")
        else:
            print(frase[i].lower(), end = "")

#alternando_crescente("gabriel")

def alternando_decrescente(frase: str) -> None:
    for i in range(len(frase) - 1, -1, -1): #começa no ultimo indice (len(frase) - 1), vai até -1 (para incluir o 0)
        if i % 2 == 0:
            print(frase[i].upper(), end = "")
        else:
            print(frase[i].lower(), end = "")
        
#alternando_decrescente("gabriel")

# EX.2: Leia uma string do usuário e mostre-a com todas as letras a|A substituídas por um “4”.

def subtituicao_a(frase: str) -> None:
    for letra in frase:
        if letra in ["a", "A"]:
            letra = "4"
            print(letra, end = "")
        else:
            print(letra, end = "")

#subtituicao_a("A dona aranha subiu pela parede")

# EX.3: Leia uma string do usuário, calcule e mostre a quantidade de vogais, consoantes,
# espaços em branco, números e caracteres especiais

def class_string(frase: str) -> None:
    ''' Cuidado com a string: in em string procura pedaços, não só caracteres soltos.
        Por exemplo, "ae" in "aeiou" dá True, mas "ae" in ["a", "e", "i", "o", "u"] dá False.
        Não afeta aqui, porque letra sempre tem um caractere só.
        Mas se o item que for testado puder ter mais de uma letra, a lista é mais segura.'''
    
    vogais : str = "aeiouáàâãéêíóôõúü" #pode ser usado no lugar de lista. Menor e tem o mesmo resultado.
    qntd_vogais : int = 0
    
    consoantes : int = 0 #não precisa de lista, só fazer 'not in [vogais]'
    
    espacos : int = 0
    numeros : int = 0
    especiais : int = 0
    
    for letra in frase.lower():
        if letra in vogais:
            qntd_vogais += 1
        elif letra.isalpha() and letra not in vogais:
            consoantes += 1
        elif letra.isdigit():
            numeros += 1
        elif letra.isspace():
            espacos += 1
        elif not letra.isalnum():
            especiais += 1
    
    print("Essa frase possui:")
    print(f"{qntd_vogais} vogais")
    print(f"{consoantes} consoantes")
    print(f"{espacos} espaços")
    print(f"{numeros} números")
    print(f"{especiais} caracteres especiais")
    
#class_string("14 de março é o dia do PI, devido ao 3.14")

# EX.4: Leia uma string do usuário e mostre a frequência de cada vogal ilustrando esta
# informação com um gráfico horizontal que mostra esta distribuição.

def class_vogais(frase: str) -> None: #DA PARA RESOLVER BEM MENOR COM DICIONARIO!! *estudar*
    class_a : str = "aáàâã"
    class_e : str = "eéê"
    class_i : str = "ií"
    class_o : str = "oóôõ"
    class_u : str = "uúü"
    
    qntd_a : int = 0
    qntd_e : int = 0
    qntd_i : int = 0
    qntd_o : int = 0
    qntd_u : int = 0
    
    for letra in frase.lower():
        if letra in class_a:
            qntd_a += 1
        elif letra in class_e:
            qntd_e += 1
        elif letra in class_i:
            qntd_i += 1
        elif letra in class_o:
            qntd_o += 1
        elif letra in class_u:
            qntd_u += 1
    
    print("Quantidade de Vogais na frase:")
    print(f"A: {"*" * qntd_a}")
    print(f"E: {"*" * qntd_e}")
    print(f"I: {"*" * qntd_i}")
    print(f"O: {"*" * qntd_o}")
    print(f"U: {"*" * qntd_u}")

#class_vogais("Amar a tudo e a todos")

# EX.5: Leia uma string do usuário que será composta apenas pelos números de um CPF 
# e então mostre o CPF com os separadores usuais.

def CPF(frase: str) -> None:
    if not frase.isdigit() or len(frase) != 11:
        print("CPF inválido. CPF deve conter 11 dígitos. Digite apenas números.")
        return

    for num in range(len(frase)):    
        if num == 3 or num == 6 :
            print(".", end = "")
        elif num == 9:
            print("-", end = "")
        print(frase[num], end = "")
            
#CPF("12345678909")

# EX.6: Leia uma string do usuário e mostre suas palavras individualmente e quantos caracteres cada uma possui
# (use o espaço como delimitador/separador das palavras).

def separacao_palavras(frase: str) -> None:
    palavra_atual : str = "" #vai add as letras
    palavras : list = [] #lista com as palavras
    
    for letra in frase:
        if letra.isspace():
            palavras.append(palavra_atual)
            palavra_atual = ""
        elif not letra.isspace():
            palavra_atual += letra
    
    palavras.append(palavra_atual) #como ultima palavra não tem espaço depois, precisa ser adicionada manualmente
    
    print(palavras)
    
    contador : int = 1
    for palavra in palavras:
        print(f"Palavra {contador}: {palavra} ({len(palavra)} letras)")
        contador += 1

separacao_palavras("Joaquim Maria Machado de Assis")