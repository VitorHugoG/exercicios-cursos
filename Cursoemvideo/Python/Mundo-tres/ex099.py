from time import sleep

def maior(* valores):
  print('-='*30)
  print("Analisando valores...")
  for i in valores:
    print(i,end=' ', flush= True)
    sleep(.3)
  print(f'Foram informados {len(valores)} valores ao todo.')
  print(f'O maior valor informado foi {max(valores)}')


maior(2,4,8,6,9,7,5,5,4,2,3)
maior(1,8,6,4,3)
maior(50,87,34,2,1,5,69)