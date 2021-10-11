print('='*8, ' CONVERSOR DE BASES ', '='*8)

numero = int(input('Digite um numero:'))
print('''
      Suas opções são: \n
      1 - Binário \n
      2 - Octa \n
      3 - Hexadecimal 
''')
opcao = int(input('digite a sua opção: '))

if opcao == 1:
    print(F'o valor digitado foi {numero} e sua conversão para binário ficou {bin(numero)}')
elif opcao == 2:
    print(F'o valor digitado foi {numero} e sua conversão para hexadecimal ficou {hex(numero)}')
elif opcao == 3:
    print(F'o valor digitado foi {numero} e sua conversão para Octa ficou {oct(numero)}')
else:
    print('Opção Inválida')