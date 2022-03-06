# laços de repetiçã: For e While

#Verificando numeros primos

'''
Regra:
  Basicamente se o numero for divisivel duas vezes (por ele e por um)
  ex: 
   o numero 5  só é divisivel por ele e por 1 
'''
for i in range (101):
    contador_divisivel = 0
    for a in range(1,i+1):
      resto = i % a
      if resto == 0:
        contador_divisivel += 1
    
    if contador_divisivel == 2:
      print(i)


