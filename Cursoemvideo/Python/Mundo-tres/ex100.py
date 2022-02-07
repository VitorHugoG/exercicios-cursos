from random import randint

def sorteia():
  print('Sorteando 5 valores da lista: ',end='')
  for i in range (0,5):
     valor = randint(1,8)
     print(valor, end=" ")
     valores.append(valor)
  print()
     

def soma_pares():
  soma = 0
  print(f'Somando os valores pares de {valores}, temos ',end="")
  for i in valores:
    if i % 2 == 0:
      soma += i
  print(soma)
  
valores = []

sorteia()
soma_pares()