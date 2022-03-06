# If , elif e else

#verficando se um valor é maior que outro
a = int(input('digite o primeiro valor:'))
b = int(input('digite o segundo valor:'))
c = int(input('digite o terceiro valor:'))

#condicionais

if (a > b & a > c ):
  print(f'o maior valor foi {a}')
elif (b > a & b > c):
  print(f'o maior valor foi {b}')
else:
  print(f'o maior valor foi {c}')

# O clássico exercicio de média aritmética 
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if (
  (0 <= nota1 <=10) & 
  (0 <= nota2 <=10) &  
  (0 <= nota3 <=10) & 
  (0 <= nota4 <=10)
  ):
  print(f'A média final foi : {media}')
else: 
  print(f'\033[31m Algum valor foi digitado errado\033[m')

