import tkinter as tk
import campo_minado as cm

# ---------- VISUAL ----------
COR_FUNDO    = "#1e1f26"   #janela e frames
COR_PAINEL   = "#2a2c36"   #botões
COR_HOVER    = "#3a3d4d"   #botão com o mouse em cima
COR_TEXTO    = "#e8e8ea"
COR_DESTAQUE = "#4ade80"   #verde: títulos e clique
COR_FECHADA  = "#4a4e5f"   #casa fechada
COR_ABERTA   = "#16171d"   #casa aberta
COR_BOMBA    = "#e5484d"
COR_BANDEIRA = "#f5a524"

COR_NUMEROS = {
    1: "#5aa9ff", 2: "#4ade80", 3: "#ff6b6b", 4: "#b388ff",
    5: "#ff9f43", 6: "#2dd4bf", 7: "#e8e8ea", 8: "#9ca3af",
}

FONTE_TITULO = ("Impact", 44)
FONTE_TITULO_JOGO = ("Impact", 28)
FONTE_TEXTO  = ("Segoe UI", 16)
FONTE_BOTAO  = ("Segoe UI", 18, "bold")
FONTE_CASA   = ("Consolas", 13, "bold")

# ---------- VARIÁVEIS ----------
tela_atual : tk.Frame = None #Frame sendo mostrado atualmente
label : tk.Label = None
gabarito = []
estado = []
botoes = []
primeira_jogada : bool = True
jogadas : int = 0
label_jogadas : tk.Label = None
fim_de_jogo : bool = False

# ---------- FUNÇÕES ----------
def criar_botao_menu(pai, texto, comando, largura=24):
    botao = tk.Button(pai, text=texto, command=comando, width=largura,
                      font=FONTE_BOTAO, bg=COR_PAINEL, fg=COR_TEXTO,
                      activebackground=COR_DESTAQUE, activeforeground=COR_FUNDO,
                      relief="flat", bd=0, pady=8, cursor="hand2")
    botao.bind("<Enter>", lambda e: botao.config(bg=COR_HOVER))
    botao.bind("<Leave>", lambda e: botao.config(bg=COR_PAINEL))
    return botao


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
        label.config(text="VOCÊ EXPLODIU!", fg=COR_BOMBA)
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
        
    fonte_casa = FONTE_CASA
    if tam_tab == 30:
        fonte_casa = ("Consolas", 9, "bold")

    for coluna in range(tam_col): #letras das colunas -> linha 0 do grid (coluna + 1 para pular o canto vazio)
        letra = tk.Label(tabuleiro, text=chr(ord('A') + coluna), width=2, font=fonte_casa, bg=COR_FUNDO, fg=COR_TEXTO)
        letra.grid(row=0, column=coluna + 1)

    for linha in range(tam_tab): #números das linhas -> coluna 0 do grid (linha + 1 para pular a linha das letras)
        numero = tk.Label(tabuleiro, text=str(linha + 1), width=2, font=fonte_casa, bg=COR_FUNDO, fg=COR_TEXTO)
        numero.grid(row=linha + 1, column=0)

    botoes = [] #lista de linhas
    for linha in range(tam_tab):
        linha_botoes = []
        for coluna in range(tam_col):
            botao = tk.Button(tabuleiro, width=2, height=1, font=fonte_casa, relief="flat", bd=0,
                  bg=COR_FECHADA, fg=COR_TEXTO, activebackground=COR_HOVER, command=lambda linha=linha, coluna=coluna: clicar(linha, coluna))
            botao.bind("<Button-3>", lambda event, linha=linha, coluna=coluna: clicar_direito(linha, coluna)) #clique com o botão direito
            botao.grid(row=linha + 1, column=coluna + 1, padx=1, pady=1) #+1 por causa das letras e dos números
            linha_botoes.append(botao)
        botoes.append(linha_botoes)
    return botoes


def iniciar_jogo(tam_tab: int):
    global gabarito, estado, botoes, primeira_jogada, fim_de_jogo, tela_atual, label, jogadas, label_jogadas
    
    limpar_tela()
    jogo_frame = tk.Frame(root, bg=COR_FUNDO)
    tela_atual = jogo_frame
    
    
    label = tk.Label(tela_atual, text= "CAMPO MINADO", font=FONTE_TITULO_JOGO, bg=COR_FUNDO, fg=COR_DESTAQUE)
    label.pack()
    
    label_jogadas = tk.Label(tela_atual, text= "Jogadas = 0", font=FONTE_TEXTO, bg=COR_FUNDO, fg=COR_TEXTO)
    label_jogadas.pack()
    
    tabuleiro = tk.Frame(tela_atual, bg=COR_FUNDO)
    tabuleiro.pack(pady=15)
    
    botao_menu = criar_botao_menu(tela_atual, "MENU", mostrar_menu, largura = 10)
    botao_menu.pack()
    tela_atual.pack(expand=True)
    
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
                casa.config(text="", bg=COR_FECHADA, relief="flat")
            elif estado[linha][coluna] == cm.BANDEIRA:
                #vermelha
                casa.config(text="#", bg=COR_FECHADA, fg=COR_BANDEIRA, relief="flat")
            else: #abertas
                #clicadas
                if gabarito[linha][coluna] == cm.BOMBA:
                    casa.config(text="*", bg=COR_BOMBA, fg=COR_TEXTO, relief="flat")
                elif gabarito[linha][coluna] == 0: #vazias
                    casa.config(text="", bg=COR_ABERTA, relief="flat")
                else:
                    casa.config(text=str(gabarito[linha][coluna]), bg=COR_ABERTA, fg=COR_NUMEROS[gabarito[linha][coluna]], relief="flat")


def limpar_tela():
    if tela_atual != None:
        tela_atual.destroy()


def mostrar_menu():
    global tela_atual
    limpar_tela()
    
    tela_atual = tk.Frame(root, bg=COR_FUNDO)
    tela_atual.pack(expand=True) #centraliza na vertical
    
    tk.Label(tela_atual, text="CAMPO MINADO", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_DESTAQUE).pack(pady=(0, 5))
    tk.Label(tela_atual, text="Escolha a Dificuldade", font=FONTE_TEXTO, bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(0, 25))
    
    criar_botao_menu(tela_atual, "Iniciante  (9x9)", lambda: iniciar_jogo(9)).pack(pady=6)
    criar_botao_menu(tela_atual, "Intermediário  (16x16)", lambda: iniciar_jogo(16)).pack(pady=6)
    criar_botao_menu(tela_atual, "Especialista  (30x16)", lambda: iniciar_jogo(30)).pack(pady=6)
    criar_botao_menu(tela_atual, "SAIR", root.destroy).pack(pady=(25, 6))


root = tk.Tk() #cria janela
root.title("CAMPO MINADO") #nome da janela
root.config(bg=COR_FUNDO)
root.state("zoomed") #tela cheia

mostrar_menu()
root.mainloop() #loop principal para rodar -> SEMPRE NO FINAL