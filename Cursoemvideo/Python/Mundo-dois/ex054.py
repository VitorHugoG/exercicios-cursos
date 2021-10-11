from datetime import date
maior = 0
menor = 0


for i in range(1, 8):
    anoNascimento = int(input(f'em que ano a {i}° nasceu?'))
    idade = date.today().year - anoNascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'existem {menor} pessoas menores de idade')
print(f'existem {maior} pessoas maiores de idade')
