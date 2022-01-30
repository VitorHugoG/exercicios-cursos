aluno = {}

aluno["nome"] = input('Nome: ')
aluno["média"] = float(input(f'A média de {aluno["nome"]} : '))

if aluno['média'] >= 7:
    aluno['situacao'] = "Aprovado"
else:
    aluno['situacao'] = "Reprovado"


for a, i in aluno.items():
    print(f'{a} é igual a {i}')