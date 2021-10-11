import random
import time
import pygame

resposta = 'SIM'
while resposta == 'SIM':
    print('''
    [ 1 ]  Pedra 
    [ 2 ]  Tesoura 
    [ 3 ]  Papel 
    ''')
    opcaoJogador = int(input('escolha sua opção: '))

    maquina = random.randint(1, 3)

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('POOO')
    time.sleep(1)

    if opcaoJogador == maquina:
        print('empate')

    elif opcaoJogador == 2 and maquina == 3:
        print('\33[32mVocê venceu')
        pygame.init()
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()

    elif opcaoJogador == 3 and maquina == 2:
        print('\33[31mA maquina ganhou')

    elif opcaoJogador == 1 and maquina == 2:
        print('\33[32mVocê venceu')
        pygame.init()
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()

    elif opcaoJogador == 1 and maquina == 3:
        print('\33[31mA maquina ganhou')

    elif opcaoJogador == 3 and maquina == 1:
        print('\33[32mVocê venceu')
        pygame.init()
        pygame.mixer.music.load('saudio.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()

    elif opcaoJogador == 2 and maquina == 1:
        print('\33[31mA maquina ganhou')

    resposta = input('deseja continuar :').strip().upper()



