palavras  = ('Bailarina','Futebol', 'Estátua')

#seleciona uma palavra por vez da tupla
for palavra in palavras:
    print(f'\n{palavra}', end='')
    for letra in palavra:
        #verifica se há uma vogal dentro da palavra
        if letra in 'aeiou':
            print(f' {letra}',end = "")