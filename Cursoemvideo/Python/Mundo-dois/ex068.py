print("="*25)
print(" Cadastre uma Pessoa ")
print("="*25)

maiorDezoito = quantidadeHomens = mulherMenorVinte = 0

while True:
    idade = int(input('idade: '))
    sexo = input('sexo = [M / F]: ')

    resp = input('deseja continuar [S /N]: ')

    if resp == 'N':
        break
    else:
        if idade > 18:
            maiorDezoito += 1
        elif sexo == "M":
            quantidadeHomens +=1
        elif sexo == "F" and idade < 20:
            mulherMenorVinte +=1
print(f'Total de pessoas com mais de 18 anos: {maiorDezoito}')
print(f'Quantidade de Homens: {quantidadeHomens}')
print(f'Mulheres com a idade abaixo de 20: {mulherMenorVinte}')