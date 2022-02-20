def leiaInt(msg):
  while True:
    try:
     inteiro = int(input(f"{msg}"))
    except (TypeError, ValueError):
      print("\033[31mERRO: por favor, digite um numero inteiro válido.\033[m")
    except KeyboardInterrupt:
     inteiro = 0
     print("O usuario decidiu encerrar programa ")
     return inteiro
    else:
      return inteiro

def linha(tam=42):
  return "-"*tam

def cabecalho(texto):
  print(linha())
  print(f'{texto}'.center(42))
  print(linha())

def menu(lista):
  cabecalho("MENU PRINCIPAL")

  contador = 1

  for i in lista:
    print(f"\033[32m{contador}\033[m - \033[34m{i}\033[m")
    contador+=1
  
  print(linha())
  resposta = leiaInt("Sua opção: ")

  return resposta