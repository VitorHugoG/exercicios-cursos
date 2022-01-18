lista = []

for i in range(0 , 10):
    lista.append(int(input('digite um valor: ')))

#imprime a lista inteira
print(f'você digitou os valores {lista}')

#maior valor da lista e as posições em que ele aparece
print(f'o maior valor foi {max(lista)} na posição ',end="")

# verificando se o valor na posição X é igual ao maior valor da lista
for i in range(0 , len(lista)):
     if lista[i] == max(lista):
        print(f'{i}.. ', end="")

#menor valor da lista e as posições em que ele aparece
print(f'\no menor valor foi {min(lista)} na posição ',end="")

# verificando se o valor na posição X é igual ao menor valor da lista
for i in range(0 , len(lista)):
     if lista[i] == min(lista):
        print(f'{i}.. ', end="")        








