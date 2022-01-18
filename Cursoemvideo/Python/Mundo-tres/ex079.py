lista = []

resp = 's'
while resp in 'sS':
    valor = int(input('digite um valor: '))
    if valor in lista:
        print('Não posso adicionar este número pois é repetido')
    else:
        #adicionando o valor ao final da lista
        lista.append(valor)
        # ordenando o valor em ordem crescente
        lista.sort()
        print('valor adicionado com sucesso')

    resp = input('Deseja continuar ? [S / N]: ')

print('-='*20)

print(f'a sua lista ficou {lista}')
