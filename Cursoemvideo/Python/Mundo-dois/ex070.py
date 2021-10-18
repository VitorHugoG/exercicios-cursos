print('=' * 30)
print('{:^30}'.format('BANCO VITOR'))
print('=' * 30)

saque = int(input('digite um valor inteiro que deseja sacar: '))
cedulas = 50
quantidadeCedulas = 0

while True:
    if saque >= cedulas:
        saque -= cedulas
        quantidadeCedulas += 1
    else:
        print(f'foram necessários {quantidadeCedulas} cedulas de {cedulas}')

        if cedulas == 50:
            cedulas = 20
            quantidadeCedulas = 0
        elif cedulas == 20:
            cedulas = 10
            quantidadeCedulas = 0
        elif cedulas == 10:
            cedulas = 1
            quantidadeCedulas = 0

        if saque == 0:
            break