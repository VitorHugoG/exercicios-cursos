casa = float(input('qual é o valor da casa?'))
salario = float(input('qual é o seu salário?'))
anos = int(input('em quantos anos você pretende pagar?'))


valorMensal = casa / (12 * anos)
porcentagemSalario = salario * 0.30

if valorMensal <= porcentagemSalario:
    print('você pode pagar')
else:
    print('você não pode pagar')

print('o valor mensal ficou {}'.format(valorMensal))
print('seu salário é {}'.format(salario))


