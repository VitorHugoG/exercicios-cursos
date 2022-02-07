def ficha(nomet="<desconhecido>", golst=0):
  print(f"O jogador {nomet} fez {golst} gol(s) no campeonato.")

nome = input('digite o nome do jogador: ')
gols = input('digite quantos gols ele fez: ')

if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0

if nome.strip() == "":
  ficha(golst=gols)
else:
  ficha(nome,gols)

