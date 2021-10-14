sexo = input('digite o seu sexo [M / F]:').lower()

#not in = não estiver entre os caracteres citados
while sexo not in 'mf':
    sexo = input('dado inválido. Digite novamente: ').lower()

print(f'o sexo  {sexo} é aceito')