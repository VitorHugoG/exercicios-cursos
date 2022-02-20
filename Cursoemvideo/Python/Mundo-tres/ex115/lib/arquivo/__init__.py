from asyncore import read
from ex115.lib.interface import cabecalho

# "investiga" se aquele arquivo existe
def arquivo_existe(nome_arquivo):
  #tenta abrir o arquivo com o para rt que significa read text
  try:
    arquivo = open(nome_arquivo,"rt")
    arquivo.close()
  # se ele não conseguir encontrar esse arquivo retorna falso
  except FileNotFoundError:
    return False
  # caso encontre o arquivo ele retorna verdadeiro
  else:
    return True

# caso ele não seja encontrado cai nessa função    
def criar_arquivo(nome_arquivo):

  #tenta escrever um arquivo texto com o parametro wt+ que significa write text e o "+" 
  # é pra caso ele não encontre criar um novo com o mesmo nome
  try:
    arquivo = open(nome_arquivo, "wt+")
    arquivo.close()
  except:
    print("houve um erro")
  else:
    print(f"O arquivo {nome_arquivo} foi criado !")

# funcao para ler arquivo
def ler_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, "rt")
  except:
    print("houve um erro !")
  else:
    cabecalho("Pessoas Cadastradas")
    
    for linha in arquivo:
      dado = linha.split(";")
      dado[1] = dado[1].replace("\n","")
      print(f"{dado[0]:<30} {dado[1]:>3} anos")
    print(arquivo.read())
    arquivo.close()

def cadastrar_pessoa(nome_arquivo, nome="Desconhecido", idade=0):
  try:
    arquivo = open(nome_arquivo, "at")
  except:
    print("houve um erro na leitura !")
  else:
    try:
      arquivo.write(f"{nome};{idade}\n")
    except:
      print("houve um erro para escrever no arquivo")
    else:
      print(f'a {nome} foi cadastrada com sucesso !')
      arquivo.close()