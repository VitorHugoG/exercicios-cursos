condicao = True
soma = 0
contador = 0
while condicao:
    numero = int(input('digite um numero inteiro:'))

    if numero != 999:
        soma += numero
        contador += 1
    else:
        condicao = False

print('o total de numero digitados foi: {}'.format(contador))
print('e a soma entre eles ficou {}'.format(soma))
