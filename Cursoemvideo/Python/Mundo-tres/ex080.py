lista = []
for i in range(0 , 5):
    numero = int(input('digite um numero: '))
    if i == 0 or numero > max(lista):
        lista.append(numero)
        print('adicionado ao final da lista')
    else:
       # posicoes
       pos = 0 
       # fazer um loop na lista pra ficar cada indice
       while pos < len(lista):
           #verifica qual é a posição do numero maior que o numero e
           # adiciona o numero naquela posição 
           if numero < lista[pos]:
               #insere o numero naquela posição e empurra o resto pra frente
               lista.insert(pos, numero)
               print(f'o numero foi adicionado na posição {pos} da lista')
               break
           pos += 1

    
print(lista)
