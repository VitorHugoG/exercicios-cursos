from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = "pessoas.txt"

if not arquivo_existe(arquivo):
  criar_arquivo(arquivo)

while True:
  resposta = menu(['ver pessoas cadastradas','cadastrar pessoas', 'sair do sistema'])

  if resposta == 1:
     # ler pessoas cadastradas
     ler_arquivo(arquivo)
  elif resposta == 2:
    cabecalho("Cadastro de pessoa")
    nome = str(input("digite o seu nome: "))
    idade = leiaInt("Digite a sua idade : ")
    cadastrar_pessoa(arquivo, nome, idade)
  elif resposta == 3:
     print("encerrando o programa...")
     break
  else:
     print("\033[31mestá não é uma opção válida\033[m")
  sleep(1.2)