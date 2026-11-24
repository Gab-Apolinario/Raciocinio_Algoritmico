import tkinter as tk

def ao_clicar():
    #label.config(text="CLICADO")
    label.destroy()
    botao.destroy()
    criar_grid(tabuleiro, 30)


def clicar(linha, coluna):
    print(linha, coluna)


def criar_grid(tabuleiro: tk.Frame, tam_tab: int):
    tam_col : int = tam_tab
    if tam_tab == 30:
        tam_col = 16
    for linha in range(tam_tab):
        for coluna in range(tam_col):
            botao = tk.Button(tabuleiro, width=2, height=1, command=lambda linha=linha, coluna=coluna: clicar(linha, coluna))
            botao.grid(row=linha, column=coluna)


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