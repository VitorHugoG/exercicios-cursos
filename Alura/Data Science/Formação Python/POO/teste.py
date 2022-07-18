'''
Conta: Saldo, titular, numero, limite 
'''

def criar_conta(saldo, titular, numero, limite):

  conta = {"saldo": saldo, "titular": titular, "número": numero, "limite": limite}

  return conta

def sacar(conta, valor):

  conta['saldo'] -= valor

def depositar(conta, valor):

  conta['saldo'] += valor

def imprimir_extrato(conta):

  print(f"o seu saldo é {conta['saldo']}")



conta_vitor = criar_conta(100.00, "Vitor Hugo", 13546578, 5000.00)

imprimir_extrato(conta_vitor)