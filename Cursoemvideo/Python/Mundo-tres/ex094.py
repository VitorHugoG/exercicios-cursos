pessoas = []
mulheres = []
acima_da_media = []
dicionario = {}
soma_idade = 0

while True:
  dicionario['nome'] = input('digite o seu nome: ')
  dicionario['sexo'] = input('digite o seu sexo [M / F]: ').upper()
  dicionario['idade'] = int(input('digite a sua idade: '))

  if dicionario['sexo'] == "F":
    mulheres.append(dicionario['nome'])
  
  pessoas.append(dicionario.copy())
  resp = input('deseja continar [S / N]: ')
  
  if resp in 'Nn':
    break
print("-=" * 30)
print(f'foram cadastradas {len(pessoas)} pessoas')


for i in pessoas:
  soma_idade += i['idade']

media_idade = soma_idade / len(pessoas)

print('-='*30)
print(f'A media de idades foi {media_idade}')
print('-='*30)
print(f'As mulheres cadastradas foram {mulheres}')
print('-='*30)
print('pessoas que estão acima da média')
for v in pessoas:
  if v['idade'] > media_idade:
    print(f"nome = {v['nome']}; idade = {v['idade']}; sexo = {v['sexo']}")
