maior = 0
menor  = 0

for i in range(1, 6):
    peso = float(input(f'qual é o peso da {i}° pessoa?'))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso foi {maior}Kg e o menor foi {menor}Kg')