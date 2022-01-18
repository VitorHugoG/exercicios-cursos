from random import randint
maior = menor = flag = 0

valoresAleatorios = (randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8))

print(menor,maior, flag)

for valor in valoresAleatorios:
    if (flag == 0):
        menor = valor
        maior = valor
        flag += 1
    elif(valor < menor):
        menor = valor
    elif(valor > maior):
        maior = valor

print('os valores digitados foram: ' , valoresAleatorios )
print(f'O maior valor foi {maior} e menor foi {menor}')