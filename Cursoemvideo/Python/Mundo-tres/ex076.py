produtos  = ("fone de ouvido" , 130.50,
             "carro", 140.000, 
             "moto", 40.000)
print('='*50)
print(f'{"PRECOS":^50}')
print('='*50)
for produto in range(0, len(produtos)):

    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30} R$ ', end= "")
    else: 
        print(f'{produtos[produto]:<7}')
    