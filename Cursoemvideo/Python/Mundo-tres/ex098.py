def contador(inicio, fim, passo):
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')

    #TODO: verificar o motivo do erro
    if inicio > fim:
      passo = passo * -1
    for i in range(inicio, fim+1 , passo):
      print(i, end=" ")
    print()

print('Letra A)')
contador(1,10,1)

print('Letra B)')
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem')
inicio = int(input('inicio :'))
fim = int(input('fim: '))
passo = int(input('passo: '))

print('Letra C)')
contador(inicio,fim,passo)