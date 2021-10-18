print('''
       ======================
       SEQUENCIA DE FIBONACCI
       ======================
       
''')

termo = int(input('quantos termos você quer mostrar?'))
termo1 = 0
termo2 = 1

print(f'sequencia ficou {termo1} {termo2}', end=' ')
#o contador começa no três porque já havia inicia 3 termos
contador = 3
while contador <= termo:
 somaValores = termo1 + termo2
 print(f'{somaValores}', end=' ')
 #para continuar a sequencia deve-se trocar os termos

 termo1 = termo2
 termo2 = somaValores
 contador += 1

 #Assim ficaram somando sempre com o anterior


