numeros = []
pares = []
impares = []

resp = 's'

while resp in 'Ss':
    valor  = int(input('digite um valor: '))
    numeros.append(valor)
    resp = input('deseja continuar? [S / N]')

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'todos os numero {numeros}')
print(f'numeros pares {pares}')
print(f'numeros impares {impares}')
