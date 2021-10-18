while True:
    numero = int(input('digite o numero que você quer fazer tabuada: '))

    if numero < 0:
        break
    else:
        for i in range (1, 11):
            print(f'{numero} x {i} = {numero * i}')

print('Programa tabuada encerrado')