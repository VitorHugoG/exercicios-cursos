import math

anguloNormal = int(input("digite uma valor de um angulo: "))
angulo = math.radians(anguloNormal)
print("o valor digitado foi {:2f}° \nseu seno: {:2f} \nseu cosseno: {:2f} \ne sua tangente : {:2f} ".format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))
