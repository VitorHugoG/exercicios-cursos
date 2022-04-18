def jogar():
   
    print("=" * 30)
    print('\033[32m{:^30}\033[m'.format('Jogo da Forca'))
    print("=" * 30)

    palavra_secreta = 'morango'
    lista_palavra = ['_','_','_','_','_','_','_']

    acertou = False
    enforcou = False

    while not enforcou and not acertou:
        
        chute = input('digite um letra para a forca: ')
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            # chute do usuário igual a letra da palavra secreta
            if (chute.upper() == letra.upper()):
                lista_palavra[index] = letra
            
            index += 1
        print()
        for i in lista_palavra:
            print(f' {i} ', end='')
        print('\n\n')
    print('Fim jogo !')


if __name__ == "__main__":
  jogar()


