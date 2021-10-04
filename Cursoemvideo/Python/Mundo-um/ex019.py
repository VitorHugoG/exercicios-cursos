import random

aluno1 = input('qual é o primeiro aluno: ')
aluno2 = input('qual é o segundo aluno: ')
aluno3 = input('qual é o terceiro aluno: ')
aluno4 = input('qual é o quarto aluno: ')


#funcao que escolhe aleatoriamente um dos elementos
sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])

print('o aluno sorteado foi {}'.format(sorteado))


