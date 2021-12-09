top20 = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Cuiba', 'Athlectic-PR', 'Atlético - GO', 'São Paulo', 'América MG','Ceara SC', 'Santos', 'Bahia', 'Juventude', 'Sport Recife','Grêmio', 'Chapecoense')

# 5 primeiros colocados
print("="*5, " Cinco primeiros colocados ", "="*5)
#outra forma de fazer isso seria top20[ : 5]
for i in range(0 , 5):
    print(f"{i + 1}° {top20[i]}")

# 4 últimos colocados
#outra forma de fazer isso seria colocar top20[-4 : ]
print("="*5, " Quatro ultimos colocados ", "="*5)
ultimo = 20
for i in range(-1, -5, -1):
 
    print(f'{ultimo}° {top20[i]} ') 
    ultimo = ultimo - 1

# Ordem alfabetica
print("="*5, " Listas de Times em Ordem Alfabetica ", "="*5)
alfabetica = sorted(top20)

for c in alfabetica:
    print(c)

#Posição do Chapecoense
print("="*5, " Posição da Chapecoense ", "="*5)
print(f"A Chapecoense está em {top20.index('Chapecoense') + 1}°")


