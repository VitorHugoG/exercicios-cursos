from random import randint 
from time import sleep
rank = 1
jogadores = {}

print("Valores sorteados")

for i in range(1,5):
    jogadores[f"jogador {i}"] = randint(1,7)

for a, i in jogadores.items():
    print(f"{a} jogou {i}")
    sleep(1)

print("\n",'-='*30, "\n")

print("Ranking dos jogadores \n")

for i in sorted(jogadores, key= jogadores.get , reverse=True):
    print(f"{rank}° lugar: {i} com {jogadores[i]}")
    rank+=1
