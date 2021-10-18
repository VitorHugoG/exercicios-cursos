tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezeoito', 'dezenove', 'vinte')

numero = int(input('digite um numero de 0 a 20: '))

while True:
    if 0 <= numero <= 20:
        break
    else:
        numero = int(input('numero não aceito tente novamente : '))
print(f'O numero por extenso ficou {tupla[numero]}')
