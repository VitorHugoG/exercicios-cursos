def leia_int(texto):
  num = input(f'{texto}')
  num = str(num)
  while True:
    if num.isnumeric():
      if num in "0123456789":
        return num  
    else:
      print('ERRO POURA')
      num = input(f'{texto} ')
numerot = leia_int("digite um numero:")
print(f'O numero que você digitou foi {numerot}')
  
    