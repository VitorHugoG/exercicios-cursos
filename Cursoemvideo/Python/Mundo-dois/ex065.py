soma = contador = 0

while True:
    numero = int(input('digite um valor:'))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'a soma de todos os numero ficou {soma} e a contagem foi {contador}')