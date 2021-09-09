kilometros = float(input("qual foi a quantidade de quilometros percorridos?"))
diasAlugado = int(input("Quantos dias o carro foi alugado?"))

totalPagar = (kilometros * 0.15) + (diasAlugado * 60)

print("O total a pagar é de R$ {}" .format(totalPagar))

