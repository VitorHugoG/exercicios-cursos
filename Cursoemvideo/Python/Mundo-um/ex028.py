import random

numero = int(input('digite o numero entre 0 e 5 , e vamos ver se você adivinha haha: '))

numeroAleatorio = random.randint(0, 5)

if numero == numeroAleatorio:
    print('você venceu!')
else:
    print('você perdeu')

print('-- fim ---')
