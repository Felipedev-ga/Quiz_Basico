import random

'''
Anotações:

1 - O while TRUE coloca uma condição infinita mas deve se criar uma
condição para parar.
'''
Pontos_Usuario = 0
Pontos_Maquina = 0

opc = ['r', 'p', 't']

while True:
    Escolha_Usuario = input('Escolha R (Pedra)\n P (Papel) \n T (Tesoura)\n Q para sair.').lower()
    
    if Escolha_Usuario == 'q':
        break
    
    Escolha_Computador = random.randint(0, 2)
    
    Computador_opc = opc[Escolha_Computador]
    
    print(f'O computador escolheu {Computador_opc}')
    
    if Escolha_Usuario == Computador_opc:
        print('EMPATE')
        
    elif Escolha_Usuario == 'r' and Computador_opc == 't':
        print('Você ganhou!!')
        Pontos_Usuario += 1
        
    elif Escolha_Usuario == 'p' and Computador_opc == 'r':
        print('Você ganhou!!')
        Pontos_Usuario += 1
        
    elif Escolha_Usuario == 't' and Computador_opc == 'p':
        print('Você ganhou!!')
        Pontos_Usuario += 1
    
    else:
        print('Você perdeu!!')
        Pontos_Maquina += 1
        
    print('Volte assim que desejar jogar!!')
    
    print(f'Sua pontuação {Pontos_Usuario}')
    print(f'Pontuação do computador {Pontos_Maquina}')
    
    if Pontos_Usuario > Pontos_Maquina:
        print('Você ganhou')
    elif Pontos_Usuario == Pontos_Maquina:
        print('EMPATE')
    else:
        print('DERROTA')
