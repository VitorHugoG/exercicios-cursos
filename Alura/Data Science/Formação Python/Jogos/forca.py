import random

def jogar():
   
    print("=" * 30)
    print('\033[32m{:^30}\033[m'.format('Jogo da Forca'))
    print("=" * 30)


    doc_frutas = open('teste.txt', 'r')

    frutas = doc_frutas.read()

    frutas = frutas.strip().split()

    fruta = random.choice(frutas)

    palavra_secreta = fruta.upper()
    #list comprehesion 
    lista_palavra = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erro = 0
    while not enforcou and not acertou:
        
        chute = input('digite um letra para a forca: ')
        chute = chute.strip().upper()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                # chute do usuário igual a letra da palavra secreta
                if (chute.upper() == letra.upper()):
                    lista_palavra[index] = letra
                
                index += 1
        else:
            erro += 1
        
        # se erro chegar a 6 ele se enforca
        enforcou = erro == 6

        # se o caractere "_" não existir dentro do array lista_palavra acaba o jogo
        acertou = "_" not in lista_palavra
        print()
        for i in lista_palavra:
            print(f' {i} ', end='')
        print('\n\n')

    if (acertou):
        print('você acertou !')
    else:
        print('você perdeu 😔')
    print('Fim jogo !')


if __name__ == "__main__":
  jogar()


