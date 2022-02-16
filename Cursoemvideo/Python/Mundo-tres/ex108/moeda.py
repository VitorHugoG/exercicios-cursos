
import math


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

def moeda(p):
    valor_arredondado = '%.2f' % round(p,2)
    tirando_ponto = str(valor_arredondado).replace(".",',')
    return f'R${tirando_ponto}'