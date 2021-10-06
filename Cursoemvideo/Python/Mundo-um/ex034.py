salario = float(input('digite o seu salario: '))

if salario > 1250:
    salarioFinal = salario + (salario * 0.10)
    print(salarioFinal)
else:
    salarioFinal = salario + (salario * 0.15)
    print(salarioFinal)
