soma = 0

for i in range(0, 6):
    valor = int(input('digite um valor: '))
    if valor % 2 == 0:
        soma += valor

print(soma)
