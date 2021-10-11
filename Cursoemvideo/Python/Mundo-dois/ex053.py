palavra = input('digite uma palavra')
inicio = 0
palavraSemEspaco = palavra.replace(" ", "").lower()
fim = len(palavraSemEspaco) - 1
condicao = True

for i in range(len(palavraSemEspaco) // 2):
    if palavraSemEspaco[fim] != palavraSemEspaco[inicio]:
        condicao = False
        break
    inicio = inicio + 1
    fim = fim - 1

if condicao:
    print(f'palavra {palavra.lower()} é um palindromo')
else:
    print(f'a palavra {palavra.lower()} não é um palindromo')