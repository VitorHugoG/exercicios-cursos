resp = 's'
soma = quantidade = media = 0
menor = maior = 0

while resp in 'Ss':
    num = int(input('digite um numero : '))
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    resp = str(input('deseja continuar? [ S/ N]')).upper().strip()

media = soma / quantidade

print('a soma foi {} a quantidade foi {} e a media ficou {}'.format(soma, quantidade, media))