nome = input('digite o seu nome:')

primeiroNome = nome.split()[0]

print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(' '))
print(len(primeiroNome))
