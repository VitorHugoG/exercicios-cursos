
def leia_dinheiro(msg):
  
  while True:
    num = str(input(f'{msg}')).replace(",",".")

    if num.isalpha() or num.strip() == "":
       print(f'ERRO "{num}" é um preço inválido !')
    else:
       return float(num)