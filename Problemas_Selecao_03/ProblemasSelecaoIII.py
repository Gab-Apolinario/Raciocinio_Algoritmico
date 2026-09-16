# Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais fofi escoolhido, através de perguntas e respostas.
# Animais possíveis: leão, cavalo, homem, macacoo, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.
# A ideia é usar seleção encadeada e fazer perguntas de acordo com as respostas do usuário e concluir qual é o animal selecionado.
# Exemplos:
# É mamífero? Sim
# É quadrúpede? Sim
# É carnívoro? Não
# É herbívoro? Sim
# Então o animal escolhido foi cavalo.

# Mamíferos
# ├── Quadrúpedes
# │   ├── Carnívoros   → Leão
# │   └── Herbívoros   → Cavalo
# ├── Bípedes
# │   ├── Onívoros     → Homem
# │   └── Frutívoros   → Macaco
# │
# ├── Voadores  → Morcego
# └── Aquáticos → Baleia
#
# Aves
# ├── Nadadoras  → Pato
# └── De rapina  → Águia
#
# Não-voadoras
# ├── Tropicais  → Avestruz
# └── Polares    → Pinguim
#
# Répteis
# ├── Com casco  → Tartaruga
# ├── Carnívoros → Crocodilo
# └── Sem patas  → Cobra

def identificar_animal() -> None:
    mamifero = input("É mamífero? (S/N): ").strip().lower()
    if mamifero[0] == "s":
        quadrupede = input("É quadrúpede? (S/N): ").strip().lower()
        if quadrupede[0] == "s":
            carnivoro = input("É carnívero? (S/N): ").strip().lower()
            if carnivoro[0] == "s":
                print("Você pensou em um Leão!")
            else: #não pode ser elif pois precisa da pergunta primeiro
                herbivoro = input("É herbívoro? (S/N): ").strip().lower()
                if herbivoro[0] == "s":
                    print("Você pensou em um Cavalo!")
        else: #ramificação BÍPEDES
            #continuar todos os bípedes, voadores e aquaticos
            pass
    else: #não é mamífero, testar as AVES
        ave = input("É ave? (S/N): ").strip().lower()
        if ave[0] == "s":
            nadadora = input("É uma ave nadadora? (S/N): ").strip().lower()
            if nadadora[0] == "s":
                print("Você pensou em um Pato!")
            else:
                rapina = input("É uma ave de rapina? (S/N): ").strip().lower()
                if rapina[0] == "s":
                    print("Você pensou em uma Águia!")
                    
identificar_animal()