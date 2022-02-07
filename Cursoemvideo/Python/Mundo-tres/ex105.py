from statistics import mean

def notas(* nota,sit=False):
  dicionario = {}
  dicionario['total'] = len(nota)
  dicionario['maior'] = max(nota)
  dicionario['menor'] = min(nota)
  dicionario['média'] = mean(nota)

  if sit:
    if dicionario['média'] <= 4:
      dicionario['situação'] = "RUIM"
    elif dicionario['média'] <= 6:
      dicionario['situação'] = "RAZOAVEL"
    else:
      dicionario['situação'] = "BOA"
  return dicionario

dicionario = notas(5,6,4,8,9,4,6,sit=True)
print(dicionario)
