from datetime import datetime

trabalhador = {}
ano_atual = datetime.now().year

trabalhador['nome'] = input('nome: ')
trabalhador['nascimento'] = int(input('digite o seu ano de nascimento: '))
trabalhador['idade'] =  ano_atual - trabalhador['nascimento'] 
trabalhador['ctps'] = int(input('digite sua carteira de trabalho: '))

if trabalhador['ctps'] != 0:
  trabalhador['ano de contratação'] = int(input('digite o ano que você foi contratado: '))
  trabalhador['salario']  = float(input('qual foi o seu salário? '))
  trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano de contratação'] + 35) - ano_atual)
  

for i , a in trabalhador.items():
  print(f'{i} é {a}')