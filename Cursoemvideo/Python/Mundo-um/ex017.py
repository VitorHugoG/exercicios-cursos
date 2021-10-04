import math

catetoOposto = float(input("digite o valor do cateto oposto: "))
catetoAdjacente = float(input("digite o valor do cateto adjacente: "))

hipotenusa = math.hypot(catetoAdjacente, catetoOposto)

print(math.floor(hipotenusa))
