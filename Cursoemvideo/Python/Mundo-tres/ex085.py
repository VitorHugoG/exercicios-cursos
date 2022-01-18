valores = [[], []]
temporario  = list()

for i in range(0, 7):
    temporario.append(int(input('digite um valor: ')))

    if temporario[0] % 2 == 0:
        valores[0].append(temporario[:])
    else:
        valores[1].append(temporario[:])
    
    temporario.clear()

valores[0].sort()
valores[1].sort()

print(f'Os valores pares são {valores[0]}')

print(f'Os valores impares são {valores[1]}')