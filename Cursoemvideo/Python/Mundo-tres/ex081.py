lista = []

resp = 's'
contador = 0
while resp in 'Ss':
    valor  = int(input('digite um valor: '))
    contador += 1

    lista.append(valor)

    lista.sort(reverse = True)

    resp = input('Deseja continuar? [S / N]')


print(f'tiveram {contador} valores registrados')

if 5 in lista:
    print('o numero cinco está na lista!!!')
else:
    print('o numero cinco não está na lista')

