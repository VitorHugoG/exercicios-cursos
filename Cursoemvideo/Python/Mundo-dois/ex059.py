print('=='*8, ' Menu de Opções ', '=='*8)

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
condicao = False

while not condicao:
    print('''
         [ 1 ] somar
         [ 2 ] multiplicar
         [ 3 ] maior
         [ 4 ] novos números
         [ 5 ] sair do programa
    ''')
    opcao = int(input('digite a sua opção: '))

    if opcao == 1:
        print(f'a soma entre {numero1} e {numero2} é {numero1 + numero2}')
    elif opcao == 2:
        print(f'a multiplicao entre {numero1} e {numero2} é {numero1 * numero2}')
    elif opcao == 3:
        if numero1 < numero2:
            print(f'maior valor é {numero2}')
        else:
            print(f'maior valor é {numero1}')
    elif opcao == 4:
        print('digite novamente os valores')
        numero1 = int(input('digite o primeiro numero: '))
        numero2 = int(input('digite o segundo numero: '))
    elif opcao == 5:
        condicao = True
