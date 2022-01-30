matriz_tres_tres = []
primeiro = list()
temporario =list()
soma= soma_terceira_coluna =  0

for i in range (0,3):

    for v in range(0,3):
        primeiro.append(int(input(f'digite um valor [{i}, {v}]: ')))
        
    matriz_tres_tres.append(primeiro[:])
    primeiro.clear()

print("-="*30)

for matriz in matriz_tres_tres:
    for i in range(0, len(matriz)):
        temporario.append(matriz[i])

        if matriz[i] % 2 == 0:
            soma+= matriz[i]
        if i == 2:
            soma_terceira_coluna += matriz[i]
    print(temporario)
    temporario.clear()

print(f'a soma dos pares é: {soma}')
print(f'a soma dos valores na terceira coluna é: {soma_terceira_coluna}')
print(f'o maior valor da segunda linha é: {max(matriz_tres_tres[1])}')