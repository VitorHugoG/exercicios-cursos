
def moeda(p):
    valor_arredondado = '%.2f' % round(p,2)
    tirando_ponto = str(valor_arredondado).replace(".",',')
    return f'R${tirando_ponto}'

def metade(p, formatado=False):
    if formatado:
        valor = p/2
        return moeda(valor)
    else:  
      return p/2

def dobro(p, formatado=False):
    if formatado: 
      valor = p * 2
      return moeda(valor)
    else:
      return p*2

def aumentar(p,porcentagem , formatado=False):
    novo_preco = (p) + (p * porcentagem/100)
    if formatado:
      return moeda(novo_preco)
    else:
      return novo_preco

def diminuir(p,porcentagem ,formatado=False):
    novo_preco = p - (p * porcentagem/100)
    if formatado:
      return moeda(novo_preco)
    else:
      return novo_preco

