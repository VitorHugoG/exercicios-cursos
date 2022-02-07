def area_terreno(largura, comprimento):
  area = largura * comprimento
  print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')

print(' Controle de Terrenos')
print('-'*20)


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area_terreno(largura, comprimento)