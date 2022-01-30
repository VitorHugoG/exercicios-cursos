jogador = {}
gols = []
jogador['nome'] = input('digite o seu nome: ')
jogador['partida'] = int(input(f'quantas partidas {jogador["nome"]} jogou?'))

for i in range(0, jogador['partida']):
    gols.append(int(input(f'quantos gols na partida {i}?')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)

for campo, valor in jogador.items():
    print(f'o campo {campo} tem o valor {valor}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas')

for i , a in enumerate(gols):
    print(f'    => Na partida {i}, fez {a} gols')

print(f'foi um total de {jogador["total"]}')

