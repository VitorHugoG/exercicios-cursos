termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao que tu irá usar: '))

contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais

    while contador <= 10:
        print(f'{termo}', end=' ')
        termo += razao
        contador += 1
    print('pausa')
    mais = int(input('quer adicionar mais quantos numeros?'))
    contador -= mais

print(f'você colocou {total} termos')
print('fim')
