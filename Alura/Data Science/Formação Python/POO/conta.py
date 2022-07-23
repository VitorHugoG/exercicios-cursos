

class Conta:

  def __init__(self, numero, titular, saldo, limite):
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  def extrato(self):

    print(f'O saldo disponivel para o titular {self.__titular} é {self.__saldo}')

  def depositar(self, valor):

    self.__saldo += valor

  def sacar(self, valor):

    self.__saldo -= valor

  def transferir(self, valor, destino):

    self.sacar(valor)
    destino.depositar(valor)