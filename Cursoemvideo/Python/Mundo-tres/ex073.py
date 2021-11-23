top20 = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Cuiba', 'Athlectic-PR', 'Atlético - GO', 'São Paulo', 'América MG','Ceara SC', 'Santos', 'Bahia', 'Juventude', 'Sport Recife','Grêmio', 'Chapecoense')

# 5 primeiros colocados
print("="*5, " Cinco primeiros colocados ", "="*5)

for i in range(0 , 5):
    print(f"{i + 1}° {top20[i]}")

# 4 últimos colocados
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

