preco = float(input('digite o preço do produto: '))
formaDePagamento = int(input(F'Opções de pagamento \n 1 - Á vista no dinheiro ou cheque \n 2 - Á vista no cartão \n 3 - 2x no cartão \n 4 - 3x ou mais no cartão \n '))

if formaDePagamento == 1:
    preco = preco - (preco * 0.10)
    print(F'Parabéns você teve 10% de desconto, o valor final ficou {preco}')
elif formaDePagamento == 2:
    preco = preco - (preco * 0.05)
    print(F'Parabéns você teve 5% de desconto, o valor final ficou {preco}')
elif formaDePagamento == 3:
    print(F'O valor final ficou {preco}')
elif formaDePagamento == 4:
    preco = preco + (preco * 0.20)
    print(F' o valor final ficou {preco}, com 30% de juros')