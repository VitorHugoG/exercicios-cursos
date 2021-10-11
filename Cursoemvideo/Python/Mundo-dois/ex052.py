numero = int(input('digite um numero: '))
contadorDeDivisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\33[32m {}'.format(i))
        contadorDeDivisores = contadorDeDivisores + 1
    else:
        print('\33[33m {}'.format(i))

#se o total de divisores for igual a dois ele é um numero primo

if contadorDeDivisores == 2:
    print('ele é um primo')
else:
    print('não é primo')

