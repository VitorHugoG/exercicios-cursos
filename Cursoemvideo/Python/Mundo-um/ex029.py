velocidadeCarro = int(input('digite a sua velocidade:'))

if velocidadeCarro > 80:
    acima = velocidadeCarro - 80
    calculoMulta = acima * 7
    print('Você foi multado , e sua multa ficou R${}'.format(calculoMulta))
else:
    print('parabéns por andar no limite de velocidade')
