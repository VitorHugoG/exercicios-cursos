def metade(p):
    return p/2

def dobro(p):
    return p*2

def aumentar(p,porcentagem):
    novo_preco = (p) + (p * porcentagem/100)
    return novo_preco

def diminuir(p,porcentagem):
    novo_preco = p - (p * porcentagem/100)
    return novo_preco

