import random
import datetime

#REGRA 1: Ter pelo menos 5 caracteres
def regra_um(senha) -> bool:
    comprimento = len(senha)
    if comprimento >= 5:
        print(f"Sua senha tem {comprimento} caracteres! Passou na regra 1!\n")
        return True
    else:
        print("Erro na regra um: Sua senha não tem pelo menos 5 caracteres!\n")
        return False

#REGRA 2: Ter um número
def regra_dois(senha) -> bool:
    for letra in senha:
        if letra.isdigit():
            print("Sua senha tem um número! Passou na regra 2!\n")
            return True
    print(f"Erro na regra dois: a senha precisa ter um número!\n")
    return False

#REGRA 3: Ter um caractere maiúsculo
def regra_tres(senha) -> bool:
    for letra in senha:
        if letra.isupper():
            print("Sua senha tem um caractere maiúsculo! Passou na regra 3!\n")
            return True
    print(f"Erro na regra três: a senha precisa ter um caractere maiúsculo!\n")
    return False

#REGRA 4: Ter um caractere especial
def regra_quatro(senha) -> bool:
    if not senha.isalnum(): #tem especial
        print("Sua senha tem um caractere especial! Passou na regra 4!\n")
        return True
    else:
        print(f"Erro na regra quatro: a senha precisa ter um caractere especial!\n")
        return False

#REGRA 5: Os números precisam somar 25 (nem mais nem menos)
def regra_cinco(senha) -> bool:
    soma : int = 0
    for letra in senha:
        if letra.isdigit():
            #print(letra, end = " ") TESTE
            soma += int(letra)
        #print(soma) TESTE
    if soma == 25:
        print("Os digitos somam 25! Passou na regra 5!\n")
        return True
    else:
        print(f"Erro na regra cinco: os números da senha precisam somar 25!\n")
        return False
    
#regra_cinco("Gabriel4544125") TESTE

#REGRA 6: Ter um número romano
def regra_seis(senha) -> bool:
    num_romano: list = ["I", "V", "X", "L", "C", "D", "M"]
    has_roman = False
    for letra in senha:
        if letra in num_romano:
            has_roman = True
            break
    if has_roman:
        print("Sua senha tem um número romano! Passou na regra 6!\n")
        return True
    else:
        print("Erro na regra 6: sua senha precisa conter um número romano (maiúsculo)!\n")
        return False
    
#REGRA 7: Incluir número sorteado entre (11...99)
def regra_sete(rand_num, senha) -> bool:
    if str(rand_num) in senha:
        print("Sua senha contém o número gerado aleatoriamente! Passou na regra 7!\n")
        return True
    else:
        print("Erro na regra 7: sua senha precisa conter o número sorteado!\n")
        return False

#REGRA 8: Começa com uma letra e termina com um número
def regra_oito(senha) -> bool:
    if  not senha[0].isalpha():
        print("Erro na regra 8: o primeiro caractere não é uma letra!\n")
        return False
    if not senha[-1].isdigit():
        print("Erro na regra 8: o último caractere não é um número!\n")
        return False
    print("O primeiro caractere é letra e o último é número! Passou na regra 8!\n")
    return True

#REGRA 9: Conter o nome do mês do ano que estamos
def regra_nove(senha) -> bool:
    meses : list = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
                    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    agora = datetime.datetime.now()
    mes_atual = agora.month #número de 1 a 12
    #print(meses[mes_atual - 1]) #TESTE
    #print(mes_atual) #TESTE
    if meses[mes_atual - 1] in senha.lower():
        print("Sua senha contém o mês no qual estamos! Passou na regra 9!\n")
        return True
    else:
        print("Erro na regra 9: a senha precisa conter o NOME do mês atual! (sem acentos)\n")
        return False

#regra_nove("okjOUTUBRObbu") TESTE

#REGRA 10: Precisa contar o nome de uma cor primária ou secundária
def regra_dez(senha) -> bool:
    cores : list = ["vermelho", "amarelo", "azul", "laranja", "verde", "roxo", "violeta"]
    for cor in cores:
        if cor in senha.lower():
            print("Sua senha possui o nome de uma das cores primárias ou secundárias! Passou na regra 10!\n")
            return True
    print("Erro na regra 10: a senha precisa conter o nome de uma cor primária/secundária!\n")
    return False
#regra_dez("oasdhazlkaververdehosldm") TESTE

#REGRA 11: Precisa ter uma letra se repetindo exatamente 3x
def regra_onze(senha) -> bool:
    for letra in senha.lower():
        if letra.isalpha(): #só conta de for letra
            contagem = senha.lower().count(letra)
            #print(letra, contagem) TESTE
            if contagem == 3:
                print("Sua senha possui o mesmo caractere repetido exatamente 3x! Passou na regra 11!\n")
                return True
    print("Erro na regra 11: a senha precisa conter o mesmo caractere exatamente 3x!\n")
    return False
    
#regra_onze("Exatamente") TESTE

#REGRA 12: Conter, pelo menos, 3 letras do seu nome
def regra_doze(nome, senha) -> bool:
    contador : int = 0
    ja_contadas : str = ""
    for letra in nome.lower():
        if letra.isalpha():
            if letra in senha.lower() and letra not in ja_contadas:
                contador += 1
                ja_contadas += letra
    #print(ja_contadas, contador) TESTE
    if contador >= 3:
        print("Sua senha possui pelo menos 3 letras diferentes do seu nome! Passou na regra 12!\n")
        return True
    else:
        print("Erro na regra 12: a senha precisa conter pelo menos 3 letras diferentes do seu nome!\n")
        return False

#regra_doze("Gabriel", "senhasegura") TESTE

# GAME LOOP
def password_game() -> None:
    ganhou : bool = False
    is_regra_sete : bool = False
    rand_num = random.randint(11, 99)
    
    print("Bem vindo ao password game!\n".upper())
    nome : str = (input("Digite o seu primeiro nome: "))
    while len(nome) < 3:
        print("Nome inválido! Precisa ter pelo menos 3 caracteres")
        nome : str = (input("Digite o seu primeiro nome: "))
        
    
    while not ganhou:
        if is_regra_sete:
            print(f" **Número {rand_num} precisa estar na sua senha. Regra 7.**\n")
        senha = input("Digite a senha: ")
        if regra_um(senha):
            if regra_dois(senha):
                if regra_tres(senha):
                    if regra_quatro(senha):
                        if regra_cinco(senha):
                            if regra_seis(senha):
                                is_regra_sete = True
                                if regra_sete(rand_num, senha):
                                    if regra_oito(senha):
                                        if regra_nove(senha):
                                            if regra_dez(senha):
                                                if regra_onze(senha):
                                                    if regra_doze(nome, senha):
                                                        ganhou = True
    print(f"PARABÉNS, {nome}! Você conseguiu completar o jogo e sua senha é muito boa! Agora é só lembrar ela sempre!\n")        

jogar_de_novo : bool = True
while jogar_de_novo:
    password_game()
    resposta : str = input("Gostaria de jogar de novo? (s/n): ").strip().lower()

    while resposta[:1] not in ["s", "n"]:
        print("Resposta inválida! Digite S ou N!")
        resposta : str = input("Gostaria de jogar de novo? (s/n): ").strip().lower()
    if resposta[0] == "s":
        jogar_de_novo = True
    else:
        jogar_de_novo = False