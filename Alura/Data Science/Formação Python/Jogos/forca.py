import random
import os

def mensagem_apresentacao():

    print("=" * 30)
    print('\033[32m{:^30}\033[m'.format('Jogo da Forca'))
    print("=" * 30)

def escolhendo_palavra():
# Pega o caminho da pasta onde o script atual está salvo
    pasta_do_script = os.path.dirname(__file__)
    caminho_completo = os.path.join(pasta_do_script, 'teste.txt')

    with open(caminho_completo, 'r') as doc_frutas:
        frutas = doc_frutas.read()
    
    frutas = frutas.strip().split()

    fruta = random.choice(frutas)

    return fruta

def chute_usuario():

    chute = input('digite um letra para a forca: ')
    chute = chute.strip().upper()

    return chute

def revelando_palavra(palavra_secreta, chute, lista_palavra ):

    index = 0
    for letra in palavra_secreta:
                # chute do usuário igual a letra da palavra secreta
                if (chute.upper() == letra.upper()):
                    lista_palavra[index] = letra
                
                index += 1

def jogar():
   
    mensagem_apresentacao()

    fruta = escolhendo_palavra()

    palavra_secreta = fruta.upper()
    #list comprehesion 
    lista_palavra = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erro = 0
    while not enforcou and not acertou:
        
        chute = chute_usuario()

        if(chute in palavra_secreta):
           revelando_palavra(palavra_secreta, chute, lista_palavra )
        else:
            erro += 1
        
        # se erro chegar a 6 ele se enforca
        enforcou = erro == 7

        # se o caractere "_" não existir dentro do array lista_palavra acaba o jogo
        acertou = "_" not in lista_palavra

        for i in lista_palavra:
            print(f' {i} ', end='')
        print('\n\n')

    if (acertou):
        print('você acertou !')
    else:
        print('você perdeu 😔')



if __name__ == "__main__":
  jogar()


