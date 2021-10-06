numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))
numero3 = int(input('digite o terceiro numero:'))

maior = 0
menor = 0

# Maior

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3

#menor
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3

print('maior é {}'.format(maior))

print('menor é {}'.format(menor))