from random import randint
from time import sleep

numeros_jogos = int(input('digite a quantidade de jogos que você deseja fazer : '))
auxiliar = list()
jogos_completo = []

for i in range(0, numeros_jogos):

    for v in range(0, 6):
        numero = randint(1,60)

        if numero not in auxiliar:
            auxiliar.append(numero)
        else:
            auxiliar.append(randint(1,60))
    jogos_completo.append(auxiliar[:])

    auxiliar.clear()

for jogo in range(0, len(jogos_completo)):
    jogos_completo[jogo].sort()

    print(f'jogo n {jogo + 1}  = {jogos_completo[jogo]}')
    sleep(2)
