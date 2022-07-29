'''
Autor: Vitor Hugo
Exercicios do curso de Orientação a Objetos com python

'''
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

  #para criação de metodos privados colocasse "__" antes do nome do metodo
  def __pode_sacar(self, valor_solicitado):

    valor_disponivel = self.__saldo + self.__limite

    return valor_solicitado <= valor_disponivel 

  def sacar(self, valor):
    #se o valor for menor ou igual a quantidade de dinheiro disponivel
    #criação de um metodo para facilitar a compreensão do código

      if self.__pode_sacar(valor):

        self.__saldo -= valor

        print('operação realizada com sucesso')

      else:

        print ('não foi possivel realizar operação')

  def transferir(self, valor, destino):

    self.sacar(valor)
    destino.depositar(valor)
    
  #metodo get que irá retornar o valor da propriedade.
  @property
  def limite(self):
    return self.__limite

  #metodo get que irá retornar o valor da propriedade.
  @property
  def titular(self):
    return self.__titular

  #criando um metodo set que irá alterar o valor de uma propriedade.
  @limite.setter 
  def limite(self, valor):
     self.__limite = valor

  @staticmethod
  def codigos_banco():
     return {"santander": "00654"}
