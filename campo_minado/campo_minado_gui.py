import tkinter as tk
import campo_minado as cm

gabarito = []
estado = []
botoes = []
primeira_jogada : bool = True
fim_de_jogo : bool = False

def ao_clicar():
    #label.config(text="CLICADO")
    botao.destroy()
    iniciar_jogo(9)


def clicar(linha: int, coluna: int):
    global primeira_jogada, fim_de_jogo
    if fim_de_jogo:
        return None
    
    casa_escolhida : tuple = linha, coluna
    tam_tab : int = len(estado)
    
    if primeira_jogada:
        qntd_bombas : int = cm.quantidade_bombas(tam_tab)
        cm.sortear_bombas(gabarito, qntd_bombas, tam_tab, casa_escolhida)
        cm.calcular_dicas(gabarito)
        primeira_jogada = False
        if cm.DEBUG: #só mostra gabarito na primeira jogada
            estado_teste = cm.criar_matriz(tam_tab, cm.ABERTA) #TESTE
            print("======= GABARITO =======")
            cm.mostrar_matriz(gabarito, estado_teste)
    
    resultado = cm.abrir_vazias(casa_escolhida, gabarito, estado)
    
    if resultado == cm.EXPLODIU:
        for linha in range(len(estado)):
            for coluna in range(len(estado[linha])):
                if gabarito[linha][coluna] == cm.BOMBA:
                    estado[linha][coluna] = cm.ABERTA
        fim_de_jogo = True
        label.config(text="VOCÊ EXPLODIU!")
    elif resultado == cm.SEGURA:
        ganhou = cm.checar_vitoria(gabarito, estado)
        if ganhou:
            fim_de_jogo = True
            label.config(text="VOCÊ GANHOU!")

    atualizar_tela(gabarito, estado)


def clicar_direito(linha: int, coluna: int):
    global fim_de_jogo
    casa_escolhida : tuple = linha, coluna
    if fim_de_jogo or primeira_jogada:
        return None

    if estado[linha][coluna] == cm.FECHADA:
        cm.colocar_bandeira(casa_escolhida, estado)
    elif estado[linha][coluna] == cm.BANDEIRA:
        cm.retirar_bandeira(casa_escolhida, estado)
    else:
        return None
    
    ganhou = cm.checar_vitoria(gabarito, estado)
    if ganhou:
        fim_de_jogo = True
        label.config(text="VOCÊ GANHOU!")
    atualizar_tela(gabarito, estado)


def criar_grid(tabuleiro: tk.Frame, tam_tab: int):
    tam_col : int = tam_tab
    if tam_tab == 30:
        tam_col = 16

    for coluna in range(tam_col): #letras das colunas -> linha 0 do grid (coluna + 1 para pular o canto vazio)
        letra = tk.Label(tabuleiro, text=chr(ord('A') + coluna), width=2)
        letra.grid(row=0, column=coluna + 1)

    for linha in range(tam_tab): #números das linhas -> coluna 0 do grid (linha + 1 para pular a linha das letras)
        numero = tk.Label(tabuleiro, text=str(linha + 1), width=2)
        numero.grid(row=linha + 1, column=0)

    botoes = [] #lista de linhas
    for linha in range(tam_tab):
        linha_botoes = []
        for coluna in range(tam_col):
            botao = tk.Button(tabuleiro, width=2, height=1, command=lambda linha=linha, coluna=coluna: clicar(linha, coluna))
            botao.bind("<Button-3>", lambda event, linha=linha, coluna=coluna: clicar_direito(linha, coluna)) #clique com o botão direito
            botao.grid(row=linha + 1, column=coluna + 1) #+1 por causa das letras e dos números
            linha_botoes.append(botao)
        botoes.append(linha_botoes)
    return botoes


def iniciar_jogo(tam_tab: int):
    global gabarito, estado, botoes, primeira_jogada, fim_de_jogo
    primeira_jogada = True
    fim_de_jogo = False
    gabarito = cm.criar_matriz(tam_tab, 0) #gabarito -> começa tudo 0 (livre)
    estado = cm.criar_matriz(tam_tab, cm.FECHADA)
    botoes = criar_grid(tabuleiro, tam_tab)


def atualizar_tela(gabarito: list, estado: list):
    for linha in range(len(estado)):
        for coluna in range(len(estado[linha])):
            casa = botoes[linha][coluna]
            if estado[linha][coluna] == cm.FECHADA:
                #clicavel
                casa.config(text="", relief="raised", bg="SystemButtonFace")
            elif estado[linha][coluna] == cm.BANDEIRA:
                #vermelha
                casa.config(text="#", relief="raised", bg="#963636")
            else: #abertas
                #clicadas
                if gabarito[linha][coluna] == cm.BOMBA:
                    casa.config(text="*", relief="sunken", bg="#ab2121")
                elif gabarito[linha][coluna] == 0: #vazias
                    casa.config(text="", relief="sunken", bg="lightgray")
                else:
                    casa.config(text=str(gabarito[linha][coluna]), relief="sunken", bg="lightgray")


root = tk.Tk() #cria janela
root.title("CAMPO MINADO") #nome da janela
root.state("zoomed") #tela cheia

layout = tk.Frame(root) #passa o pai como parâmetro

label = tk.Label(layout, font=("Segoe UI", 20), text="CAMPO MINADO")
botao = tk.Button(layout, font=("Segoe UI", 20), text="Iniciar Botão", command=ao_clicar)
layout.pack() #.pack() -> mostra na tela
label.pack()
botao.pack()

tabuleiro = tk.Frame(layout)
tabuleiro.pack()

root.mainloop() #loop principal para rodar -> SEMPRE NO FINAL