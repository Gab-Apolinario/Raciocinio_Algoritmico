import tkinter as tk
import campo_minado as cm

gabarito = []
estado = []
botoes = []

def ao_clicar():
    #label.config(text="CLICADO")
    label.destroy()
    botao.destroy()
    iniciar_jogo(9)


def clicar(linha, coluna):
    print(linha, coluna)


def criar_grid(tabuleiro: tk.Frame, tam_tab: int):
    tam_col : int = tam_tab
    if tam_tab == 30:
        tam_col = 16

    botoes = [] #lista de linhas
    for linha in range(tam_tab):
        linha_botoes = []
        for coluna in range(tam_col):
            botao = tk.Button(tabuleiro, width=2, height=1, command=lambda linha=linha, coluna=coluna: clicar(linha, coluna))
            botao.grid(row=linha, column=coluna)
            linha_botoes.append(botao)
        botoes.append(linha_botoes)
    return botoes


def iniciar_jogo(tam_tab: int):
    global gabarito, estado, botoes
    gabarito = cm.criar_matriz(tam_tab, 0) #gabarito -> começa tudo 0 (livre)
    estado = cm.criar_matriz(tam_tab, cm.FECHADA)
    botoes = criar_grid(tabuleiro, tam_tab)
    estado[0][0] = cm.ABERTA
    estado[0][1] = cm.BANDEIRA
    gabarito[0][0] = 3
    atualizar_tela(gabarito, estado)


def atualizar_tela(gabarito: list, estado: list):
    for linha in range(len(estado)):
        for coluna in range(len(estado[linha])):
            casa = botoes[linha][coluna]
            if estado[linha][coluna] == cm.FECHADA:
                #clicavel
                casa.config(text="", relief="raised", bg="SystemButtonFace")
            elif estado[linha][coluna] == cm.BANDEIRA:
                #vermelha
                casa.config(text="#", relief="raised", bg="red")
            else: #abertas
                #clicadas
                if gabarito[linha][coluna] == cm.BOMBA:
                    casa.config(text="*", relief="sunken", bg="lightgray")
                elif gabarito[linha][coluna] == 0:
                    casa.config(text="", relief="sunken", bg="lightgray")
                else:
                    casa.config(text=str(gabarito[linha][coluna]), relief="sunken", bg="lightgray")


root = tk.Tk() #cria janela
root.title("CAMPO MINADO") #nome da janela
root.state("zoomed") #tela cheia

layout = tk.Frame(root) #passa o pai como parâmetro
tabuleiro = tk.Frame(layout)
tabuleiro.pack()

label = tk.Label(layout, font=("Segoe UI", 20), text="Label Teste")
botao = tk.Button(layout, font=("Segoe UI", 20), text="Iniciar Botão", command=ao_clicar)
layout.pack() #.pack() -> mostra na tela
label.pack()
botao.pack()

root.mainloop() #loop principal para rodar -> SEMPRE NO FINAL