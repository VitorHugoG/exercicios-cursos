matriz_tres_tres = []
primeiro = list()
temporario =list()


for i in range (0,3):

    for v in range(0,3):
        primeiro.append(int(input(f'digite um valor [{i}, {v}]: ')))
    
    matriz_tres_tres.append(primeiro[:])
    primeiro.clear()

print("-="*30)

for matriz in matriz_tres_tres:
    for i in range(0, len(matriz)):
        temporario.append(matriz[i])
    print(temporario)
    temporario.clear()
