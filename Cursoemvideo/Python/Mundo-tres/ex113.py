'''
Try and exception (tentativa e exceção)
'''
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

def leiaFloat(msg):
  while True:
    try:
     real = float(input(f"{msg}"))
    except (TypeError, ValueError):
      print("\033[31mERRO: por favor, digite um numero real válido.\033[m")
    except KeyboardInterrupt:
     real = 0
     print("O usuario decidiu encerrar programa ")
     return real
    else:
      return real

valor_inteiro = leiaInt("Digite um Inteiro: ")
valor_real = leiaFloat("Digite um Real: ")

print(f"O valor digitado foi {valor_inteiro} e o real foi {valor_real:.2f}")