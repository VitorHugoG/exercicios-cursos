frase = input('digite uma frase:').strip()

print('Aparece {} vezes a letra "A" '.format(frase.upper().count('A')))

print('Primeira vez na posicao {}'.format(frase.upper().find('A') + 1))

print('A ultima vez na posicao {}'.format(frase.upper().rfind('A') + 1))
