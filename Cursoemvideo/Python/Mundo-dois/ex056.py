media = 0
somaIdade = 0
nomeMaisVelho = ''
maiorIdadeMasculino = 0
contadorMulheres = 0

for i in range(1, 5):
    print('=='*5, f'{i}° pessoa', '=='*5)
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('SEXO[M / F]:').strip().lower()

    if sexo == 'm':
        if idade > maiorIdadeMasculino:
            maiorIdadeMasculino = idade
            nomeMaisVelho = nome

    elif sexo == 'f':
        if idade < 20:
            contadorMulheres = contadorMulheres + 1

    somaIdade = somaIdade + idade

media = somaIdade / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maiorIdadeMasculino} e se chama {nomeMaisVelho}')
print(f'Ao todo são {contadorMulheres} mulheres com menos de 20 anos')




