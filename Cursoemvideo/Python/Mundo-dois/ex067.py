import random
contador = 0
while True:
    numero = int(input('digite um valor: '))
    opcao = input("P = par e I = impar").upper()

    maquina = random.randint(1, 6)
    soma = numero + maquina
    contador += 1

    if opcao == 'P':
        if soma % 2 == 0:
            print('Você venceu')
        else:
            print('A maquina ganhou')
            break

    if opcao == 'I':
        if soma % 2 != 0:
            print('Você venceu')
        else:
            print('A maquina ganhou')
            break