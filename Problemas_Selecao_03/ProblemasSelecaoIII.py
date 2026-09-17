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

# def verificar_resposta(resposta: str) -> bool:
#     if resposta[0] not in ["s", "n"]:
#         print("Resposta inválida! Digite S ou N.")
#         return False
#     return True

def identificar_animal() -> None:
    mamifero = input("É mamífero? (S/N): ").strip().lower()
    if mamifero[0] == "s":
        quadrupede = input("É um mamífero quadrúpede? (S/N): ").strip().lower()
        if quadrupede[0] == "s":
            carnivoro = input("É um mamífero carnívero? (S/N): ").strip().lower()
            if carnivoro[0] == "s":
                print("Você pensou em um Leão!")
            else: #não pode ser elif pois precisa da pergunta primeiro
                herbivoro = input("É mamífero herbívoro? (S/N): ").strip().lower()
                if herbivoro[0] == "s":
                    print("Você pensou em um Cavalo!")
                else:
                    print("Não foi possível identificar o animal.")
        else: #ramificação BÍPEDES
            bipedes = input("É um bípede? (S/N): ").strip().lower()
            if bipedes[0] == "s":
                onivoro = input("É um mamífero onívoro? (S/N): ").strip().lower()
                if onivoro[0] == "s":
                    print("Você pensou em um Ser Humano!")
                else:
                    frutivoro = input("É um mamífero frutívoro? (S/N): ").strip().lower()
                    if frutivoro[0] == "s":
                        print("Você pensou em um Macaco!")
                    else:
                        print("Não foi possível identificar o animal.")                                                
            else:
                voador = input("É um mamífero voador? (S/N): ").strip().lower()
                if voador[0] == "s":
                    print("Você pensou em um Morcego!")
                else:
                    aquatico = input("É um mamífero aquático? (S/N): ").strip().lower()
                    if aquatico[0] == "s":
                        print("Você pensou em uma Baleia!")
                    else:
                        print("Não foi possível identificar o animal.")                                                
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
                else:
                    ave_nao_voadora = input("É uma ave não-voadora? (S/N): ").strip().lower()
                    if ave_nao_voadora[0] == "s":
                        tropical = input("É uma ave não-voadora tropical? (S/N): ").strip().lower()
                        if tropical[0] == "s":
                            print("Você pensou em um Avestruz!")
                        else:
                            polar = input("É uma ave não-voadora polar? (S/N): ").strip().lower()
                            if polar[0] == "s":
                                print("Você pensou em um Pinguim!")
                            else:
                                print("Não foi possível identificar o animal.")                                                
        else: #não é ave, testar os RÉPTEIS
            reptil = input("É réptil? (S/N): ").strip().lower()
            if reptil[0] == "s":
                casco = input("É um réptil com casco? (S/N): ").strip().lower()
                if casco[0] == "s":
                    print("Você pensou em uma Tartaruga!")
                else:
                    reptil_carnivoro = input("É um réptil carnívoro? (S/N): ").strip().lower()
                    if reptil_carnivoro[0] == "s":
                        print("Você pensou em um Crocodilo!")
                    else:
                        sem_patas = input("É um réptil sem patas? (S/N): ").strip().lower()
                        if sem_patas[0] == "s":
                            print("Você pensou em uma Cobra!")
                        else:
                            print("Não foi possível identificar o animal.")                                                
            else:
                print("Não consigo reconhecer esse animal no meu banco de dados!")

identificar_animal()