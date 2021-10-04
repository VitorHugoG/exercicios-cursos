n = input('digite o nome completo:').strip()
nome = n.split()

print('primeiro nome {}'.format(nome[0]))
print('ultimo nome {}'.format(nome[len(nome) - 1]))
