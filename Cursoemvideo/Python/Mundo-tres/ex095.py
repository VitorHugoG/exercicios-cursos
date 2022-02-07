jogadores = []
jogador = {}
gols = []
while True:
  jogador['nome'] = input('qual é o nome do jogador: ')
  total_partidas = int(input(f'quantas partidas {jogador["nome"]} jogou ?'))

  for i in range(0, total_partidas):
    gols.append(int(input(f'quantos gols fez na partida {i} ? ')))

  jogador['gols'] = gols[:]
  jogador['total'] = sum(gols)
  jogadores.append(jogador.copy())

  jogador.clear()
  gols.clear()

  resp = input("Deseja continuar? [S/N]")
  if resp in "Nn":
    break
  
for i, a in enumerate(jogadores):
  print(f'{i:>3} {a["nome"]} {a["gols"]} {a["total"]}')

print('-='*30)

while True:
  valor = int(input('digite o numero do jogador que deseja procurar ? (999 para sair): ' ))

  if valor == 999:
    break
  elif valor >= len(jogadores):
    print('este valor não está na lista de jogadores')
  else:
    print(f'Os dados do jogador {jogadores[valor]["nome"]}')
    for k, v in enumerate(jogadores[valor]["gols"]):
      print(f'no jogo {k} fez {v} gols')

