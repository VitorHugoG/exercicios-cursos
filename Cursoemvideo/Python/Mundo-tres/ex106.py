def sistema():
  
  while True:
    func = str(input('funcao ou biblioteca:'))
    if func == "Fim":
      break
    help(func)
    

print('~'*20)
print(' \033[1;30;42m SISTEMA PYHELP \033[m')
print('~'*20)

sistema()