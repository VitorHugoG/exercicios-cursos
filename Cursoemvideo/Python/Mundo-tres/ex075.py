valor1 = int(input("digite seu primeiro valor: "))
valor2 = int(input("digite seu segundo valor: "))
valor3 = int(input("digite seu terceiro valor: "))
valor4 = int(input("digite seu quarto valor: "))

tupla = (valor1, valor2, valor3, valor4)

print(tupla.count(9))
print(tupla.index(3))


if tupla.index(3) :
    print(f"A posição do numero 3 foi {tupla.index(3) + 1}")
else:
    print("nenhum numero 3 foi digitado")

contador = 0
for i in tupla:
    if i % 2 == 0:
        contador += 1

print(f"os numero pares foram {contador}")