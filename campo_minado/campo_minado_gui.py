import tkinter as tk
import campo_minado as cm

tela_atual : tk.Frame = None #Frame sendo mostrado atualmente
label : tk.Label = None
gabarito = []
estado = []
botoes = []
primeira_jogada : bool = True
jogadas : int = 0
label_jogadas : tk.Label = None
fim_de_jogo : bool = False

def clicar(linha: int, coluna: int):
    global primeira_jogada, fim_de_jogo, jogadas
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
        jogadas += 1
        label_jogadas.config(text=f"Jogadas = {jogadas}")
        ganhou = cm.checar_vitoria(gabarito, estado)
        if ganhou:
            fim_de_jogo = True
            label.config(text="VOCÊ GANHOU!")

    atualizar_tela(gabarito, estado)


def clicar_direito(linha: int, coluna: int):
    global fim_de_jogo, jogadas
    casa_escolhida : tuple = linha, coluna
    if fim_de_jogo or primeira_jogada:
        return None

    if estado[linha][coluna] == cm.FECHADA:
        cm.colocar_bandeira(casa_escolhida, estado)
        jogadas += 1
        label_jogadas.config(text=f"Jogadas = {jogadas}")
    elif estado[linha][coluna] == cm.BANDEIRA:
        cm.retirar_bandeira(casa_escolhida, estado)
        jogadas += 1
        label_jogadas.config(text=f"Jogadas = {jogadas}")
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
    global gabarito, estado, botoes, primeira_jogada, fim_de_jogo, tela_atual, label, jogadas, label_jogadas
    
    limpar_tela()
    jogo_frame = tk.Frame(root)
    tela_atual = jogo_frame
    
    label = tk.Label(tela_atual, font=("Segoe UI", 20), text= "CAMPO MINADO")
    label.pack()
    label_jogadas = tk.Label(tela_atual, font=("Segoe UI", 20), text= "Jogadas = 0")
    label_jogadas.pack()
    
    botao_menu = tk.Button(tela_atual, font=("Segoe UI", 20), text= "MENU", command=mostrar_menu)
    tabuleiro = tk.Frame(tela_atual)
    tabuleiro.pack()
    
    tela_atual.pack()
    botao_menu.pack()
    
    primeira_jogada = True
    jogadas = 0
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


def limpar_tela():
    if tela_atual != None:
        tela_atual.destroy()


def mostrar_menu():
    global tela_atual
    limpar_tela()
    menu_frame = tk.Frame(root)
    tela_atual = menu_frame
    titulo = tk.Label(menu_frame, text="CAMPO MINADO")
    titulo.pack()
    botao_iniciante = tk.Button(menu_frame, font=("Segoe UI", 20), text="Modo Iniciante (9x9)", command=lambda: iniciar_jogo(9))
    botao_intermediario = tk.Button(menu_frame, font=("Segoe UI", 20), text="Modo Intermediário (16x16)", command=lambda: iniciar_jogo(16))
    botao_especialista = tk.Button(menu_frame, font=("Segoe UI", 20), text="Modo Especialista (30x16)", command=lambda: iniciar_jogo(30))
    botao_sair = tk.Button(menu_frame, font=("Segoe UI", 20), text="SAIR", command=root.destroy)
    botao_iniciante.pack()
    botao_intermediario.pack()
    botao_especialista.pack()
    botao_sair.pack()
    
    menu_frame.pack()


root = tk.Tk() #cria janela
root.title("CAMPO MINADO") #nome da janela
root.state("zoomed") #tela cheia

mostrar_menu()
root.mainloop() #loop principal para rodar -> SEMPRE NO FINAL