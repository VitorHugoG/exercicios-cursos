razao = int(input('digite um numero na PA:'))
termo = int(input('digite o primeiro termo: '))
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print(i)
