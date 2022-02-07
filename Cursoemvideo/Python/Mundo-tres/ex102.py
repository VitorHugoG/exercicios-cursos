def fatorial(numero, show=False):
  i = 1
  for n in range(numero,0,-1):
      i*=n

  if show:
    for n in range(numero,0,-1):
      if n == 1:
        print(f'{n}',end=" = ")
      else:  
        print(f'{n}',end=" x ")
  print(i)

fatorial(5)

