import statistics

alunos = []
notas = list()
auxiliar = list()
resp= "s"
media = 0
while True:

    if resp in "Nn":
        break
    else:
        auxiliar.append(str(input('nome do aluno: ')))

        for i in range(0, 2):
            notas.append(int(input('digite sua nota: ')))
        
        media = statistics.mean(notas)

        auxiliar.append(notas[:])
        auxiliar.append(media)

        alunos.append(auxiliar[:])
    
        auxiliar.clear()
        notas.clear()

        resp = str(input('deseja continuar [ S / N ]: '))

for a,i in enumerate(alunos):
    print(f'{a} {i[0]} {i[2]}')

while True:
    opcao = int(input("digite o indice do aluno que você quer ver ou digite 999: "))

    if opcao == 999:
        break
    else:
        print(f'[{alunos[opcao][0]}] {alunos[opcao][1]} [{alunos[opcao][2]}]')


    
