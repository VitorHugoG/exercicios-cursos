pessoas = list()
informacoes = list()
resposta ='s'
contador_pessoas = 0
pessoas_pesadas = list()
pessoas_leves = list()
flag = 0
pesado = leve = 0

while True:

    if resposta in 'Nn':
       
        break

    else:
        informacoes.append(input('digite o seu nome: '))

        informacoes.append(int(input('digite o seu peso: ')))

        pessoas.append(informacoes[:])

        contador_pessoas+=1

        informacoes.clear()
    
    resposta  = input('Deseja continuar [ S / N ] ?')


print(f'você cadastrou {contador_pessoas} pessoas')

for p in pessoas:
    if flag == 0:
        pesado = p[1]
        leve = p[1]
        flag+=1
    
    if p[1] > pesado:
        pesado = p[1]
    if p[1] < leve:
        leve = p[1]

print(f'o maior peso foi {pesado} ',end="")

for i in pessoas:
    if  i[1] == pesado:
        print(f'{i[0]}') 


print(f'o menor peso foi {leve} ',end="")

for i in pessoas:
    if  i[1] == leve:
        print(f'{i[0]}') 



        