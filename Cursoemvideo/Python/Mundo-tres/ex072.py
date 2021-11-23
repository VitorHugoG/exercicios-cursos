numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
           "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezeoito", "dezenove", "vinte")

numero = int(input("digite um numero entre 0 e 20: "))
while True:
     if 0 <= numero <= 20:
         print(numeros[numero])
         break
     numero = int(input("numero inválido. Tente novamente: "))




