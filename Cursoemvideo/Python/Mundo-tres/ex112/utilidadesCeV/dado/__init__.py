
def leia_dinheiro(str):
  
  
  while True:
    num = input(f'{str}')

    if num.isnumeric():
      return float(num)
    else:
      print(f'ERRO "{num}" é um preço inválido !')