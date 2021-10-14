import random
resposta = False
tentativas = 0
numeroAleatorio = random.randint(0, 10)

while not resposta:
    numero = int(input('digite o numero entre 0 e 10 , e vamos ver se você adivinha haha: '))

    tentativas = tentativas + 1

    if numero == numeroAleatorio:
        resposta = True
        print('\33[32m você venceu!\33[m')
    else:
        if numero < numeroAleatorio:
            print('\33[31m você perdeu, é maior \33[m')
        elif numero > numeroAleatorio:
            print('\33[31m você perdeu, é menor \33[m')


print(f'você tentou {tentativas} vezes')
print('-- fim ---')

