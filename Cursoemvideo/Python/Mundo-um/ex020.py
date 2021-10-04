import random

aluno1 = input('digite o nome do primeiro aluno:')
aluno2 = input('digite o nome do segundo aluno:')
aluno3 = input('digite o nome do terceiro aluno:')
aluno4 = input('digite o nome do quatro aluno:')


novaOrdem = [aluno1, aluno2, aluno3, aluno4]
#embaralha uma lista pre definida
random.shuffle(novaOrdem)

print('a ordem sorteado para apresentação ficou {}'.format(novaOrdem))



