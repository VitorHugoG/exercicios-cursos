fatorial = int(input('digite um numero para calcular o fatorial: '))
armazena = 1
while fatorial >= 1:
    armazena *= fatorial
    fatorial = fatorial - 1

print(f'o fatorial é  {armazena}')