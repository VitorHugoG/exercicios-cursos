kilometros = int(input('digite a quantidade de kilometros rodados:'))

if kilometros <= 200:
    passagem = kilometros * 0.50
    print('A sua passagem ficou R$ {}'.format(passagem))
else:
    passagem = kilometros * 0.45
    print('A sua passagem ficou R$ {}'.format(passagem))
