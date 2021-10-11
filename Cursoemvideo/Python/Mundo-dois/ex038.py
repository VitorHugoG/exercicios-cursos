numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))

if numero1 < numero2:
    print('numero {} é maior que {}'.format(numero2, numero1))
elif numero2 < numero1:
    print('numero {} é maior que {}'.format(numero1, numero2))
else:
    print('os numeros são iguais')


