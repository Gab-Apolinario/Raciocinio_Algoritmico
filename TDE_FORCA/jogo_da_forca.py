import random
import time
import os

ARVORE : list = [r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                              .                             
                           .-"-.                           
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                             \ /                            
                              |                             
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                             \|/                            
                            \_|_/                           
                              |                             
                              |                             
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                           ,@%@@@,                          
                         @@%@@@@@%@@                        
                         @@@%@@@@%@@                        
                           `@@%@@'                          
                             |||                            
                             |||                            
                            /|||\                           
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                          ,@%@@@@%,                         
                       @@%@@@@@%@@@@%@                      
                     @@@%@@@@%@@@@@%@@@@                    
                     @@@%@@@@@%@@@@%@@@@                    
                       @@@@%@@@@%@@@@@                      
                          `@@@%@@@'                         
                            \|||/                           
                             |||                            
                  *         /|||\           *               
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                         ,@%@@@@%@@,                        
    v                @@%@@@@@%@o@@%@@@@@            v       
       v          @@@%@@o@%@@@@@%@@@@%@@@@@                 
                 @@@%@@@@@%@@@@%@@@@o%@@@@%@                
                 @@@o%@@@@%@@@@@%@@@@%@@o@@%                
                   @@@@%@@@@o%@@@o%@@@@@%@                  
                      `@@@@%@@@@%@@@@@'                     
                            \|||/                           
        *                    |||                   *        
          *     *     \|/   /|||\   \|/     *     *         
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''']

MURCHAR_ESTAGIO_0 : list = [r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                              .                             
                            .-"-.                           
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                 '                          
                            .-"-.                           
,.'^.,'.,^'.,,.'^.,'_,-._/\-.__.-/\_,-._.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                            .-'-.                           
,.'^.,'.,^/\-.__.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                         .        ,                         
                            .-x-.                           
_.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-._''']

MURCHAR_ESTAGIO_1 : list = [r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                             \ ,                            
                              |  .                          
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                               ,                            
                           .  |  ,                          
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                               _,                           
                          .   /   ,                         
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                          ,  _, .  '                        
_.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-._''']

MURCHAR_ESTAGIO_2 : list = [r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                             \|,                            
                            \_|_                            
                              |                             
                              |   .                         
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                               ,                            
                             _|_                            
                         `    |                             
                           .  |   ,                         
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                 _,                         
                               _/                           
                              /                             
                        ` .   |    ,                        
,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.,^'.,,.'^.,'.''',
r'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                               _,                           
                        ` ,  '|   .                         
_.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-.__.-/\_,-._/\-._''']

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal", "Mata Atlantica", "Manguezal", "Savana", "Tundra"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar", "Compostagem", "Coleta Seletiva", "Biodiversidade", "Preservacao"],
                'Animal Ameacado': ["Onca-pintada", "Mico-leao-dourado", "Arara-azul", "Tamandua-bandeira", "Lobo-guara", "Ariranha", "Peixe-boi"],
                'Problema Ambiental': ["Desmatamento", "Queimada", "Poluicao", "Aquecimento Global", "Enchente", "Lixo Plastico"]}

VIDAS_MAX : int = 6
ERRO : int = -1
REPETIDA : int = 0
ACERTO : int = 1
vidas : int = VIDAS_MAX

def escolher_categoria() -> str:
    list_temas = list(TEMAS) # retorna lista com as CHAVES do dict
    tam_temas = len(list_temas) # retorna quantidade de elementos nessa lista de chaves
    rand_tema = random.randint(0, tam_temas - 1) # sorteia um int até o comprimento da lista - 1
    categoria_escolhida = list_temas[rand_tema] # seleciona a sorteada
    # print(f"CATEGORIA SORTEADA: {categoria_escolhida}")    # DEBUG
    return categoria_escolhida


def escolher_palavra(categoria: str) -> str:
    tam_palavras = len(TEMAS[categoria]) # retorna quantidade de elementos na lista dos VALORES da CHAVE escolhida
    rand_palavra = random.randint(0, tam_palavras - 1) # sorteia um int até o comprimento da lista de valores - 1
    palavra_escolhida = TEMAS[categoria][rand_palavra] # seleciona a sorteada
    # print(f"PALAVRA SORTEADA: {palavra_escolhida}")   # DEGUB
    return palavra_escolhida


def gerar_tracinhos(palavra_escolhida: str) -> list: # var tracinhos como lista de '_' já convertendo espaços e hífen
    tracinhos = ["_"] * len(palavra_escolhida)
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i] == " " or palavra_escolhida[i] == "-":
            tracinhos[i] = palavra_escolhida[i]
    return tracinhos


def mostrar_palavra(categoria: str, tracinhos: list): # printa palavra sem ser em formato de lista
    print(f"\nCATEGORIA: {categoria}\n") # visual
    print("Palavra: ", end = " ") # visual
    for i in range(len(tracinhos)):
        print(tracinhos[i], end = "") # visual -> mais bonito de mostrar do que com ['_']
    print()


def pedir_letra() -> str:
    input_jogador : str = str(input("Digite uma letra: ").lower())
    while not validar_letra(input_jogador):
        print("Caractere inválido. Por favor digite apenas uma letra.")
        input_jogador : str = str(input("Digite uma letra: ").lower())
    input_jogador = remover_acento(input_jogador)
    return input_jogador


def verificar_letra(input_jogador: str, palavra_escolhida: str) -> bool: # retorna se tem a letra na palavra sorteada
    if input_jogador in palavra_escolhida.lower():
        return True
    else:
        return False


def validar_letra(input_jogador: str) -> bool: # usada para validar input do jogador
    if input_jogador.isalpha() and len(input_jogador) <= 1: # é caractere alpha e só tem um caractere
        return True
    return False


def remover_acento(input_jogador: str) -> str: # como .isalpha() permite acentos, função remove para respeitar regra do jogo
    com_acento : str = "áàâãéêíóôõúç"
    sem_acento : str = "aaaaeeiooouc"
    
    if input_jogador in com_acento:
        pos = com_acento.index(input_jogador) # registra posição na string com_acento para usar na substituição
        input_jogador = sem_acento[pos] # substitui
    return input_jogador


def registrar_letra(input_jogador: str, testadas: list) -> None: # adiciona na lista de letras já registradas
    if input_jogador not in testadas:
        testadas.append(input_jogador)


def adicionar_letra(tracinhos: list, palavra_escolhida: str, input_jogador: str): # em tracinhos -> substitui '_' pela letra
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i].lower() == input_jogador:
            tracinhos[i] = palavra_escolhida[i] # retorna letra original para pegar as iniciais maiúsculas


def mostrar_usadas(testadas: list) -> None: # visual
    print("\nLetras já tentadas:", end = " ")
    for i in range(len(testadas)):
        print(testadas[i], end = " - ")


def processar_letra(input_jogador: str, testadas: list, palavra_escolhida: str, tracinhos: list) -> int: # devolve ERRO, REPETIDA ou ACERTO
    if input_jogador in testadas:
        return REPETIDA
    else:
        registrar_letra(input_jogador, testadas)
        if verificar_letra(input_jogador, palavra_escolhida):
            adicionar_letra(tracinhos, palavra_escolhida, input_jogador)
            return ACERTO
        else:
            return ERRO


def verificar_vitoria(tracinhos: list) -> bool:
    if "_" not in tracinhos: # se não tem mais '_' -> acertou tudo
        return True
    return False


def verificar_derrota(vidas: int) -> bool:
    if vidas <= 0:
        return True
    return False


# -------------------------------
# ARTE
# -------------------------------

## Quantas letras o jogador precisa acertar?
def contar_letras(palavra_escolhida: str) -> int:
    contador_letras : int = 0
    for i in range(len(palavra_escolhida)):
        if palavra_escolhida[i] not in [" ", "-"]:
            contador_letras += 1
    #print(f"Palavra: {palavra_escolhida} | Tamanho: {len(palavra_escolhida)} | Contador: {contador_letras}") # DEBUG
    return contador_letras


def estagio_arte(contador_letras: int, tracinhos: list) -> int:
    # contador_letras = 100%
    contador_reveladas : int = 0
    
    # saber quantas já foram acertadas = fraçao
    for letra in tracinhos:
        if letra not in [" ", "-", "_"]:
            contador_reveladas += 1
    #print(f"Letras Reveladas: {contador_reveladas}") # DEBUG
    
    fracao : float = contador_reveladas / contador_letras
    estagio_ascii : int = round(fracao * 5) # multiplica por 5 pois são 5 estágios, convertendo em round() para não ter decimal e com 1 acerto já virar 1 (não 0 como era com int())
    #print(f"Estágio da Arte: {estagio_ascii}") # DEBUG
    return estagio_ascii
    

def desenhar_ascii(estagio_ascii: int, ARVORE: list) -> None:
    pos_desenho = ARVORE[estagio_ascii]
    print(pos_desenho)


def randomizar_secagem_folhas(desenho_estagio: str) -> list: # cria lista com a sequencia de ascii com as folhas secando
    folhas = ["@", "%", "o"] # caracteres considerados folhas
    desenho_list : list = list(desenho_estagio) # transforma o DESENHO em lista para poder substituir os caracteres
    posicoes_folhas : list = [] #folhas -> len(posicoes_folhas) = quantidade de folhas no desenho
    
    # passa por todas as folhas no desenho
    for i in range(len(desenho_estagio)):
        if desenho_estagio[i] in folhas:
            posicoes_folhas.append(i) # guarda as POSIÇÕES das folhas
    
    folhas_frame : int = len(posicoes_folhas) // 4 #total de folhas // frames
    qntd_tirar : int = folhas_frame #qntd a retirar por frame
    frames_secagem : list = []
    for i in range(4): # FRAMES -> 4
        # diminuir gradualmente
        if i == 3: # se for o ultimo frame
            qntd_tirar = len(posicoes_folhas) #tira todas as folhas restantes da divisão inteira em folhas_frame

        for _ in range(qntd_tirar): # quantas folhas por frame
            rand = random.randint(0, len(posicoes_folhas) - 1)
            pos_substituir : int = posicoes_folhas[rand]
            #percorre e substitui a posição(folhas) rand sorteada
            desenho_list[pos_substituir] = " "
            posicoes_folhas.pop(rand)
            
        frames_secagem.append("".join(desenho_list)) # junta de novo numa string e adiciona o desenho na lista
    return frames_secagem


def secar_arvore(estagio_ascii: int, ARVORE: list) -> None:
    # Decide qual sequencia de ascii usar
    if estagio_ascii >= 3 and estagio_ascii <= 5:
        frames_secagem = randomizar_secagem_folhas(ARVORE[estagio_ascii])
        animar_desenho(frames_secagem)
    elif estagio_ascii == 0:
        animar_desenho(MURCHAR_ESTAGIO_0)
    elif estagio_ascii == 1:
        animar_desenho(MURCHAR_ESTAGIO_1)
    else:
        animar_desenho(MURCHAR_ESTAGIO_2)


def animar_desenho(lista_desenho: list) -> None:
    for frame in lista_desenho:
        os.system("cls")
        print(frame)
        time.sleep(0.7)


# -------------------------------
# LOOP JOGO
# -------------------------------

ganhou : bool = False
perdeu : bool = False

categoria = escolher_categoria()
palavra_escolhida = escolher_palavra(categoria)
tracinhos = gerar_tracinhos(palavra_escolhida)
testadas : list = []
contador_letras = contar_letras(palavra_escolhida) #chamado uma vez pois só sorteia a palavra uma vez

while not ganhou and not perdeu:
    estagio_ascii = estagio_arte(contador_letras, tracinhos)
    desenhar_ascii(estagio_ascii, ARVORE) # mostra árvore no estágio atual
    mostrar_palavra(categoria, tracinhos)
    
    input_jogador = pedir_letra()
    resultado = processar_letra(input_jogador, testadas, palavra_escolhida, tracinhos)
    
    if resultado == ERRO:
        vidas -= 1
    elif resultado == REPETIDA:
        print("\nLetra já verificada anteriormente!")
        
    print("\n-----------------------------------------")
    mostrar_usadas(testadas)
    print(f"\nVIDAS RESTANTES: {vidas}/{VIDAS_MAX}")
    perdeu = verificar_derrota(vidas)
    ganhou = verificar_vitoria(tracinhos)

if ganhou:
    animar_desenho(ARVORE)
    print("\n-----------------------------------------")
    print("\nPARABÉNS! VOCÊ ACERTOU A PALAVRA!")
    print("\n-----------------------------------------")
    print(f"A palavra era: {palavra_escolhida}\n")
else:
    secar_arvore(estagio_ascii, ARVORE)
    print("\n-----------------------------------------")
    print("\nPERDEU TODAS AS VIDAS!")
    print("\n-----------------------------------------")
    print(f"A palavra era: {palavra_escolhida}\n")