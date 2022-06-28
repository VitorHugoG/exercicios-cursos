from random import randint

def jogar():
    print("=" * 30)
    print('\033[32m{:^30}\033[m'.format('Jogo da Adivinhação'))
    print("=" * 30)

    numero_aleatorio = randint(1,100)

    print(numero_aleatorio)

    tentativas = 0

    pontos = 1000

    print (
        """
    (1) Fácil
    (2) Médio
    (3) Difícil
        """
        )

    escolha = int(input('digite a opção desejada : '))

    if escolha == 1:

        tentativas = 20

    elif escolha == 2:

        tentativas = 10

    else:

        tentativas = 5
    

    for i in range(1, tentativas + 1) :
        
        print(f'tentativa {i} de {tentativas}')
    
        chute_usuario = int(input('digite um numero entre 1 e 100: '))

        '''
        Define se o chute for entre 1 e 100 incluindo os dois
        '''
        while True:
            if(chute_usuario < 1 | chute_usuario > 100):
                print('Você digitou um número inválido !')
                chute_usuario = int(input('digite novamente :'))
            else:
                break


        acertou = chute_usuario == numero_aleatorio
        maior = chute_usuario > numero_aleatorio
        menor = chute_usuario < numero_aleatorio

        if (acertou):
            print(f'você acertou e sua pontuação foi {pontos}!')
            
        else:
            if(maior):
                print('Você errou ! o número que você digitou é maior')
            elif(menor):
                print('Você errou ! o número que você digitou é menor')
            pontos_perdidos = abs(chute_usuario - numero_aleatorio)
            pontos = pontos - pontos_perdidos
        
    print('Fim jogo !')

# se for executado pelo terminal, ou seja diretamente
if __name__ == "__main__":
    jogar()

