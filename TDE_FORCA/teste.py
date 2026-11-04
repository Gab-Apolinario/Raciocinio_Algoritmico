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

TEMAS : dict = {'Biomas': ["Amazonia", "Cerrado", "Caatinga", "Pantanal", "Mata Atlantica", "Manguezal", "Savana", "Tundra"],
                'Solucao': ["Reciclagem", "Reflorestamento", "Energia Solar", "Compostagem", "Coleta Seletiva", "Biodiversidade", "Preservacao"],
                'Animal Ameacado': ["Onca-pintada", "Mico-leao-dourado", "Arara-azul", "Tamandua-bandeira", "Lobo-guara", "Ariranha", "Peixe-boi"],
                'Problema Ambiental': ["Desmatamento", "Queimada", "Poluicao", "Aquecimento Global", "Enchente", "Lixo Plastico"]}

#-------------------------
# TESTES
#-------------------------
# print(TEMAS)
# print(list(TEMAS))
# #print(TEMAS["Animal"])
# print(TEMAS.get("Animal"))
#-------------------------

#-------------------------
# letras = list("casa")
# letras[0] = "m"
# print(letras)
# print("".join(letras))
#-------------------------


#-------------------------
# print("3")
# time.sleep(1)   # espera 1 segundo
# print("2")
# time.sleep(1)
# print("1")
#-------------------------

#-------------------------
# for n in [3, 2, 1]:
#     os.system("cls")
#     print(n)
#     time.sleep(1)
#-------------------------

# for arvore in ARVORE:
#     os.system("cls")
#     print(arvore)
#    time.sleep(1)

for i in range(3, 0, -1):
    print(i, end = "")
    time.sleep(1)