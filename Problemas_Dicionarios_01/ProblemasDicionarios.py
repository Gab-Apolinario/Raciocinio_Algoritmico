thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}

# EX. 4: Crie um dicionário onde palavras são chaves e emojis são os valores. O programa deve receber uma frase do usuário,
# separar a frase em palavras, substituir todas as palavras reconhecidas pelo emoji correspondente e manter as palavras não encontradas.

frase = input("Digite sua frase: ")
for palavra in frase.split(): #separa em cada espaço
    if palavra in emojis.keys(): #gera lista com as chaves do dict
        chave = palavra.strip(",").lower()
        print(emojis[chave], end = " ")
    else:
        print(palavra, end = " ")
        