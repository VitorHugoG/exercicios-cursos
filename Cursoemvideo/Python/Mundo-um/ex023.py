numero = int(input('digite um numero de 0 a 9999:'))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade:', unidade)
print('dezena:', dezena)
print('centena:', centena)
print('milhar:', milhar)




