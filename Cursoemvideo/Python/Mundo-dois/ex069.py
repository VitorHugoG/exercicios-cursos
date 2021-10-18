total = maisDeMil = maisBaratoPreco = flag = 0
nomeMaisBarato = ' '
while True:
    nome = str(input('digite o nome do produto: '))
    preco = float(input('digite o preco do produto: '))

    resp = ' '
    if preco > 1000:
        maisDeMil += 1

    if flag == 0 or preco < maisBaratoPreco:
        maisBaratoPreco = preco
        nomeMaisBarato = nome
        flag += 1

    total += preco

    while resp not in 'SNsn':
        resp = str(input('deseja continuar [S / N]:'))
    if resp in 'Nn':
        break

print(f'o mais barato foi {maisBaratoPreco} e o nome do produto foi {nomeMaisBarato}')
print(f'O numeor de produtos que custam mais de mil reais {maisDeMil}')