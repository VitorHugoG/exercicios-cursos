import adivinhacao
import forca

print("=" * 30)
print('\033[32m{:^30}\033[m'.format('Escolha de Jogos'))
print("=" * 30)

print(
"""
(1) Jogo da Forca
(2) Jogo de Adivinhação
""")

escolha_usuario = int(input('digite sua escolha: '))

if escolha_usuario == 1:
  forca.jogar()
elif escolha_usuario == 2:
  adivinhacao.jogar()




