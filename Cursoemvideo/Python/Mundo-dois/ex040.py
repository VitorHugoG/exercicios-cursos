nota1 = float(input('digite a sua primeira nota: '))
nota2 = float(input('digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado Cleitin !')
elif media <= 6.9:
    print('Recuperação Cleitin')
else:
    print('Aprovado meu mano !')
