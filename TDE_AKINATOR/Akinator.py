# AKINATOR DE LENTES FOTOGRÁFICAS

# 1. Você vai fotografar pessoas?
# ├── S → 2. Quer o fundo bem desfocado, com a pessoa em destaque?
# │       ├── S → 3. Costuma fotografar em lugares escuros (interior, noite)?
# │       │       ├── S → Fixa 85mm f/1.2 (entra muita luz)
# │       │       └── N → Zoom 70-200mm f/4 (retrato ao ar livre, fundo desfocado, versátil)
# │       └── N → 4. Vai fotografar em espaços pequenos ou grupos grandes?
# │               ├── S → 5. As pessoas se movem muito (festas, família)?
# │               │       ├── S → Zoom 24-70mm f/2.8
# │               │       └── N → Fixa 35mm f/1.8
# │               └── N → Fixa 50mm f/1.8
# │
# └── N → 6. Vai fotografar animais?
#         ├── S → 7. São animais muito pequenos (insetos)?
#         │       ├── S → Macro 90-105mm (lembre de usar flash!)
#         │       └── N → 8. Ficam longe de você (aves, vida selvagem)?
#         │               ├── S → 9. Precisa de alcance extremo (aves em voo)?
#         │               │       ├── S → Super telezoom 150-600mm
#         │               │       └── N → Telezoom 70-300mm
#         │               └── N → Zoom versátil 24-105mm (pets, zoológico)
#         │
#         └── N → 10. Vai fotografar paisagens ou arquitetura?
#                 ├── S → 11. Quer um efeito super distorcido e criativo?
#                 │       ├── S → Fish-eye 8-15mm
#                 │       └── N → 12. Vai fotografar o céu à noite (estrelas)?
#                 │               ├── S → Grande angular 14-24mm f/2.8
#                 │               └── N → Grande angular 16-35mm f/4
#                 │
#                 └── N → 13. É uso geral / hobby (viagem, dia a dia)?
#                         ├── S → 14. Quer gastar pouco?
#                         │       ├── S → 15. Quer fundo desfocado?
#                         │       │       ├── S → Fixa 50mm f/1.8
#                         │       │       └── N → Lente kit 18-55mm
#                         │       └── N → Zoom versátil 24-105mm
#                         └── N → Zoom 24-70mm f/2.8 (profissional versátil)


def verificar_resposta(pergunta: str) -> bool:
    resposta : str = str(input(f"{pergunta} S/N: ")).strip().lower()
    while resposta[:1] not in ["s", "n"]:
        print("Resposta inválida! Digite S ou N (pode ser minúsculo)!")
        resposta : str = str(input(f"{pergunta} S/N: ")).strip().lower()
    if resposta[0] == "s":
            return True
    return False
    
def recomendar_lente() -> None:
    print("<------------------------------------->\n")
    print("Bem-vindo ao sistema de seleção de lente fotográfica!\n")
    print("Aparentemente você se interessa por fotografia e precisa de ajuda para decidir qual lente comprar.\n")
    print("Bom, eu posso te ajudar! Responda algumas perguntas e, no final, você saberá a lente certa para o seu uso!\n")
    print("Vamos começar:")

    if verificar_resposta("Você vai fotografar pessoas?"):
        #SIM, vai fotografar pessoas
        if verificar_resposta("Quer um fundo bem desfocado, com a pessoa em destaque?"):
            #SIM, quer fundo desfocado
            if verificar_resposta("Costuma fotografar em lugares escuros (dentro de lugares fechados, fotos de noite)?"):
                #SIM, lugar escuro
                print("Uma lente fixa então! 85mm f/1.2 seria uma ótima!")
            #NÃO, lugar claro
            else:
                print("Uma lente 70-200mm f/4 seria uma ótima! Ela é versátil, boa para retratos ao ar livre e ainda desfoca o fundo!")
        #NÃO, não quer fundo desfocado
        else:
            if verificar_resposta("Vai fotografar em espaços pequenos e/ou grupos grandes?"):
                #SIM, espaço pequeno
                if verificar_resposta("As pessoas se movimentam muito nesse ambiente (festas, família, crianças)?"):
                    #SIM, há movimento
                    print("Aqui vale a pena uma 24-70mm f/2.8. Você consegue capturar um ângulo maior, com mais pessoas e ainda consegue dar zoom caso queira!")
                #NÃO, não há muito movimento
                else:
                    print("Lente fixa 35mm f/1.8! Fica no meio termo das grande angulares!")
            #NÃO, não é espaço pequeno
            else:
                print("50mm f1.8! Ótima qualidade, barata e super leve.")
    
    #NÃO vai fotografar pessoas
    else:
        if verificar_resposta("Você vai fotografar animais?"):
            #SIM, vai fotografar animais
            if verificar_resposta("São animais muito pequenos?"):
                #SIM, animamis pequenos
                print("Lente Macro 90-105mm. Você vai conseguir detalhes incríveis dos insetos, mas lembre-se de usar um flash para esse tipo de fotografia!")
            #NÃO, não são animais pequenos
            else:
                if verificar_resposta("São animais que ficam longe de você (aves, vida selvagem)?"):
                    #SIM, ficam longe
                    if verificar_resposta("Precisa de alcance extremo?"):
                        #SIM, alcance extremo
                        print("Nesse caso você precisa de uma lente super telezoom. 150-600mm vai ser ótima para essa situação.")
                    #NÃO, sem alcance extremo
                    else:
                        print("Uma lente Telezoom 70-300mm já é o suficiente!")
                #NÃO, não ficam longe
                else:
                    print("Uma lente com zoom versátil vai suprir sua necessidade, 24-105mm é ótima para fotografar pets ou um passeio no zoológico!")
        #NÃO, não vai fotografar animais
        else:
            if verificar_resposta("Pretende fotografar paisagens ou arquitetura?"):
                #SIM, paisagens e arquitetura
                if verificar_resposta("Quer um efeito super distorcido e criativo?"):
                    #SIM, efeito distorcido
                    print("Uma lente Fish-eye 8-15mm vai te ajudar a criar fotos bem diferentes e criativas.")
                #NÃO, sem distorção
                else:
                    if verificar_resposta("Vai fotografar o céu à noite (estrelas)?"):
                        #SIM, céu noturno
                        print("Uma grande angular 14-24mm f/2.8 vai ser ideal para fazer fotos das estrelas. Se quiser aquele efeito de rastro, lembre-se de usar um tripé e fazer longa exposição!")
                    #NÃO, foto de dia
                    else:
                        print("Grande angular 16-35mm f/4 vai bastar!")
            #NÃO, sem paisagens e arquitetura
            else:
                if verificar_resposta("É uso para hobby (viagens, dia a dia)?"):
                    #SIM, hobby
                    if verificar_resposta("Quer gastar pouco?"):
                        #SIM, gastar pouco
                        if verificar_resposta("Quer fundo bem desfocado?"):
                            #SIM, barato e fundo desfocado
                            print("Melhor opção aqui é uma lente fixa 50mm f/1.8. Ótimo custo-benefício e geralmente a primeira lente de todo fotógrafo!")
                        #NÃO, gastar pouco sem fundo muito desfocado
                        else:
                            print("Nesse caso, creio que a lente que já veio com sua câmera (lente do kit) já va te servir bem. Uma 18-55mm!")
                    #NÃO, posso gastar mais
                    else:
                        print("Então vale a pena gastar um pouco e comprar uma 24-105mm. Ela é super versátil e vai te ajudar na maior dos casos.")
                #NÃO, uso profissional
                else:
                    print("Vale a pena pegar uma lente zoom versátil para uso geral. A 24-70mm f/2.8 é uma ótima opção.")
                    
recomendar_lente()