def escreva(texto):
  tamanho_texto = len(texto) + 3
  print('~'*tamanho_texto)
  print(f'{texto:^{tamanho_texto}}')
  print('~'*tamanho_texto)

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')